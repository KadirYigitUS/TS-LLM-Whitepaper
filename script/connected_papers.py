#!/usr/bin/env python3
"""ConnectedPapers workflow: seed JSONs + graph exports per reference cohort."""

from __future__ import annotations

import argparse
import asyncio
import json
import os
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional

ROOT = Path(__file__).resolve().parents[1]
META_PATH = ROOT / "data" / "reference_metadata.json"
OUTPUT_DIR = ROOT / "data" / "connected_papers"

try:  # Optional dependency (installed via pip)
    from connectedpapers import ConnectedPapersClient
    from connectedpapers.connected_papers_client import GraphResponseStatuses
except ImportError:  # pragma: no cover
    ConnectedPapersClient = None  # type: ignore[misc]
    GraphResponseStatuses = None  # type: ignore[misc]

ENV_TOKEN = os.getenv("CONNECTEDPAPERS_TOKEN") or os.getenv("CONNECTED_PAPERS_API_KEY")


@dataclass
class Reference:
    key: str
    category: str
    doi: Optional[str]
    sha_id: Optional[str]
    stage: Optional[str] = None

    @property
    def paper_id(self) -> Optional[str]:
        """Return the Semantic Scholar SHA identifier required by ConnectedPapers."""

        return self.sha_id


def load_metadata() -> List[Reference]:
    records = json.loads(META_PATH.read_text(encoding="utf-8"))
    refs: List[Reference] = []
    for record in records:
        refs.append(
            Reference(
                key=record.get("key") or record.get("file_stub", "unknown"),
                category=record.get("category", ""),
                doi=record.get("doi"),
                sha_id=record.get("sha_id")
                or record.get("paper_id")
                or record.get("semantic_scholar_id"),
                stage=record.get("stage"),
            )
        )
    return refs


def bucketize(refs: List[Reference]) -> Dict[str, List[str]]:
    buckets: Dict[str, List[str]] = {
        "primary": [],
        "secondary": [],
        "tertiary": [],
        "all": [],
    }
    for ref in refs:
        paper_id = ref.paper_id
        if not paper_id:
            continue
        buckets["all"].append(paper_id)
        if "Primary" in ref.category:
            buckets["primary"].append(paper_id)
        elif "Secondary" in ref.category:
            buckets["secondary"].append(paper_id)
        elif "Tertiary" in ref.category:
            buckets["tertiary"].append(paper_id)
    return buckets


def write_seed_files(buckets: Dict[str, List[str]]) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for name, paper_ids in buckets.items():
        path = OUTPUT_DIR / f"{name}_seeds.json"
        payload = {"paper_ids": paper_ids}
        path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        print(
            f"Seed list written: {path.relative_to(ROOT)} ({len(paper_ids)} paper IDs)"
        )


def simplify_graph(graph_dict: dict, category: str) -> dict:
    """Convert ConnectedPapers graph payload to the widget-ready schema."""

    nodes_dict = graph_dict.get("nodes", {})
    edges_raw = graph_dict.get("edges", [])

    nodes = []
    for node_id, node in nodes_dict.items():
        nodes.append(
            {
                "id": node_id,
                "title": node.get("title"),
                "citations": node.get("citations")
                or node.get("numCitations")
                or node.get("citationCount"),
                "category": category,
                "doi": node.get("doi") or node.get("externalIds", {}).get("DOI"),
            }
        )

    links = []
    for edge in edges_raw:
        if len(edge) < 3:
            continue
        links.append({"source": edge[0], "target": edge[1], "weight": edge[2]})

    return {"nodes": nodes, "links": links}


def export_graph(
    client: ConnectedPapersClient,
    ref: Reference,
    args: argparse.Namespace,
) -> Optional[dict]:
    paper_id = ref.paper_id
    if not paper_id:
        print(f"Skipping {ref.key}: missing Semantic Scholar paper ID (sha_id).")
        return None

    if args.wait:
        response = client.get_graph_sync(  # type: ignore[call-arg]
            paper_id,
            fresh_only=args.fresh_only,
        )
    else:

        async def _get_first_response() -> Optional[object]:
            async for item in client.get_graph_async_iterator(  # type: ignore[attr-defined]
                paper_id,
                fresh_only=args.fresh_only,
                wait_until_complete=False,
            ):
                return item
            return None

        response = asyncio.run(_get_first_response())

    status = getattr(response, "status", None)
    graph_json = getattr(response, "graph_json", None)
    if GraphResponseStatuses is not None and status not in (
        GraphResponseStatuses.FRESH_GRAPH,
        GraphResponseStatuses.OLD_GRAPH,
    ):
        print(f"Warning: {ref.key} returned status {status}; graph may be stale.")
    if graph_json is None:
        print(f"No graph returned for {ref.key} ({paper_id}).")
        return None

    graph_dict = asdict(graph_json)
    out_path = OUTPUT_DIR / f"{ref.key}_graph_raw.json"
    out_path.write_text(json.dumps(graph_dict, indent=2), encoding="utf-8")

    simplified = simplify_graph(graph_dict, ref.category)
    simplified_path = OUTPUT_DIR / f"{ref.key}_graph_widget.json"
    simplified_path.write_text(json.dumps(simplified, indent=2), encoding="utf-8")
    print(
        f"Graph saved for {ref.key}: {out_path.relative_to(ROOT)}, "
        f"widget payload -> {simplified_path.relative_to(ROOT)}"
    )
    return {
        "key": ref.key,
        "paper_id": paper_id,
        "raw_graph": str(out_path.relative_to(ROOT)),
        "widget_graph": str(simplified_path.relative_to(ROOT)),
        "status": status.name if hasattr(status, "name") else str(status),
    }


def fetch_manual_ids(
    client: ConnectedPapersClient,
    manual_ids: Iterable[str],
    args: argparse.Namespace,
) -> List[dict]:
    manifest_entries: List[dict] = []
    for idx, paper_id in enumerate(manual_ids, start=1):
        pseudo_ref = Reference(
            key=f"manual_{idx}",
            category="Manual",
            doi=None,
            sha_id=paper_id,
        )
        result = export_graph(client, pseudo_ref, args)
        if result:
            manifest_entries.append(result)
    return manifest_entries


def run_connectedpapers(refs: List[Reference], args: argparse.Namespace) -> None:
    if ConnectedPapersClient is None:
        print("connectedpapers client not installed; skipping graph fetch.")
        return

    token = args.api_token or ENV_TOKEN or ("TEST_TOKEN" if args.allow_test else None)
    if not token:
        raise SystemExit(
            "Missing API token. Set CONNECTEDPAPERS_TOKEN or use --api-token/--allow-test."
        )

    client = ConnectedPapersClient(access_token=token, verbose=args.verbose)

    manifest: List[dict] = []
    for ref in refs:
        result = export_graph(client, ref, args)
        if result:
            manifest.append(result)

    manifest.extend(fetch_manual_ids(client, args.paper_id or [], args))

    if manifest:
        manifest_path = OUTPUT_DIR / "graphs_manifest.json"
        manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        print(f"Manifest saved to {manifest_path.relative_to(ROOT)}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate ConnectedPapers graphs + widget payloads."
    )
    parser.add_argument(
        "--api-token",
        help="Override API token (defaults to CONNECTEDPAPERS_TOKEN env).",
    )
    parser.add_argument(
        "--allow-test",
        action="store_true",
        help="Fallback to TEST_TOKEN when no API key is supplied.",
    )
    parser.add_argument(
        "--paper-id",
        action="append",
        help="Fetch additional paper IDs (Semantic Scholar ShaIDs).",
    )
    parser.add_argument(
        "--fresh-only",
        action="store_true",
        help="Force ConnectedPapers to rebuild graphs (no cached results).",
    )
    parser.add_argument(
        "--no-wait",
        dest="wait",
        action="store_false",
        help="Return immediately with the current API status (uses async iterator).",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose ConnectedPapers client logging.",
    )
    parser.set_defaults(wait=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.paper_id is None:
        args.paper_id = []
    refs = load_metadata()
    buckets = bucketize(refs)
    write_seed_files(buckets)
    run_connectedpapers(refs, args)


if __name__ == "__main__":
    main()
