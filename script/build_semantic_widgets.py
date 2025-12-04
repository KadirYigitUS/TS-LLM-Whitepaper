#!/usr/bin/env python3
"""Convert Semantic Scholar graphs into ConnectedPapers-style widgets and manifests."""

from __future__ import annotations

import argparse
import json
import subprocess
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

ROOT = Path(__file__).resolve().parents[1]
SEMSCHOLAR_DIR = ROOT / "data" / "semantic_scholar"
CONNECTED_DIR = ROOT / "data" / "connected_papers"
NETWORK_DIR = ROOT / "data" / "network_manifests"
NETWORK_DIR.mkdir(parents=True, exist_ok=True)
WIDGET_DIR = SEMSCHOLAR_DIR / "widgets"
WIDGET_DIR.mkdir(parents=True, exist_ok=True)
R_WIDGET_SCRIPT = ROOT / "script" / "network_widgets.R"


def map_category(node: dict) -> str:
    category = node.get("category")
    if category:
        return category
    node_type = (node.get("type") or "").lower()
    if node_type == "seed":
        return "seed"
    if node_type == "citation":
        return "citation"
    if node_type == "reference":
        return "reference"
    return "semantic_scholar"


def convert_semantic_graph(graph_path: Path) -> dict:
    data = json.loads(graph_path.read_text(encoding="utf-8"))
    nodes = data.get("nodes", [])
    edges = data.get("edges", [])

    degree: Dict[str, int] = defaultdict(int)
    incoming_citations: Dict[str, int] = defaultdict(int)
    for edge in edges:
        source = edge.get("source")
        target = edge.get("target")
        if source:
            degree[source] += 1
        if target:
            degree[target] += 1
        if edge.get("relation") == "cited_by" and target:
            incoming_citations[target] += 1

    widget_nodes: List[dict] = []
    for node in nodes:
        node_id = node.get("id")
        node_type = (node.get("type") or "").lower()
        if not node_id:
            continue
        weight = max(degree.get(node_id, 1), 1)
        if node_type == "seed":
            weight = max(weight, incoming_citations.get(node_id, weight), 25)
        widget_nodes.append(
            {
                "id": node_id,
                "title": node.get("title") or node_id,
                "citations": weight,
                "category": map_category(node),
                "doi": node.get("doi"),
                "seed_file_stub": node.get("seed_file_stub"),
            }
        )

    widget_links: List[dict] = []
    for edge in edges:
        src = edge.get("source")
        tgt = edge.get("target")
        if not src or not tgt:
            continue
        relation = edge.get("relation")
        weight = 1.0 if relation == "cited_by" else 0.5
        widget_links.append({"source": src, "target": tgt, "weight": weight})

    return {"nodes": widget_nodes, "links": widget_links}


def run_r_widget(widget_json: Path, widget_html: Path) -> None:
    cmd = ["Rscript", str(R_WIDGET_SCRIPT), str(widget_json), str(widget_html)]
    subprocess.run(cmd, check=True)


@dataclass
class SemanticSummary:
    file_stub: str
    graph_path: Path
    widget_json: Path
    widget_html: Path
    nodes: int
    edges: int


def build_semantic_widgets(force: bool = False) -> List[SemanticSummary]:
    summaries: List[SemanticSummary] = []
    for graph_path in sorted(SEMSCHOLAR_DIR.glob("*_semanticscholar_graph.json")):
        file_stub = graph_path.stem.replace("_semanticscholar_graph", "")
        widget_json = WIDGET_DIR / f"{file_stub}_semanticscholar_widget.json"
        widget_html = WIDGET_DIR / f"{file_stub}_semanticscholar_widget.html"
        if widget_json.exists() and widget_html.exists() and not force:
            data = json.loads(widget_json.read_text(encoding="utf-8"))
            summaries.append(
                SemanticSummary(
                    file_stub=file_stub,
                    graph_path=graph_path,
                    widget_json=widget_json,
                    widget_html=widget_html,
                    nodes=len(data.get("nodes", [])),
                    edges=len(data.get("links", [])),
                )
            )
            continue

        widget_payload = convert_semantic_graph(graph_path)
        widget_json.write_text(json.dumps(widget_payload, indent=2), encoding="utf-8")
        run_r_widget(widget_json, widget_html)
        summaries.append(
            SemanticSummary(
                file_stub=file_stub,
                graph_path=graph_path,
                widget_json=widget_json,
                widget_html=widget_html,
                nodes=len(widget_payload.get("nodes", [])),
                edges=len(widget_payload.get("links", [])),
            )
        )
    return summaries


def write_semantic_manifest(rows: List[SemanticSummary]) -> None:
    manifest_path = SEMSCHOLAR_DIR / "widgets" / "manifest_semanticscholar_widgets.json"
    manifest_csv = SEMSCHOLAR_DIR / "widgets" / "manifest_semanticscholar_widgets.csv"
    manifest_data = [
        {
            "file_stub": row.file_stub,
            "graph_json": str(row.graph_path.relative_to(ROOT)),
            "widget_json": str(row.widget_json.relative_to(ROOT)),
            "widget_html": str(row.widget_html.relative_to(ROOT)),
            "nodes": row.nodes,
            "edges": row.edges,
        }
        for row in rows
    ]
    manifest_path.write_text(json.dumps(manifest_data, indent=2), encoding="utf-8")
    with manifest_csv.open("w", encoding="utf-8") as handle:
        handle.write("file_stub,graph_json,widget_json,widget_html,nodes,edges\n")
        for row in manifest_data:
            handle.write(
                f"{row['file_stub']},{row['graph_json']},{row['widget_json']},{row['widget_html']},{row['nodes']},{row['edges']}\n"
            )


def load_connected_manifest() -> List[dict]:
    manifest_path = CONNECTED_DIR / "graphs_manifest.json"
    if not manifest_path.exists():
        return []
    return json.loads(manifest_path.read_text(encoding="utf-8"))


def build_combined_manifest(semantic_rows: List[SemanticSummary]) -> List[dict]:
    combined: List[dict] = []
    for row in semantic_rows:
        combined.append(
            {
                "source": "semantic_scholar",
                "file_stub": row.file_stub,
                "graph_json": str(row.graph_path.relative_to(ROOT)),
                "widget_json": str(row.widget_json.relative_to(ROOT)),
                "widget_html": str(row.widget_html.relative_to(ROOT)),
                "nodes": row.nodes,
                "edges": row.edges,
            }
        )

    for entry in load_connected_manifest():
        combined.append(
            {
                "source": "connected_papers",
                "file_stub": entry.get("key"),
                "graph_json": entry.get("raw_graph"),
                "widget_json": entry.get("widget_graph"),
                "widget_html": None,
                "nodes": None,
                "edges": None,
                "status": entry.get("status"),
            }
        )

    combined_path = NETWORK_DIR / "graph_manifest_combined.json"
    combined_csv = NETWORK_DIR / "graph_manifest_combined.csv"
    combined_path.write_text(json.dumps(combined, indent=2), encoding="utf-8")
    with combined_csv.open("w", encoding="utf-8") as handle:
        handle.write(
            "source,file_stub,graph_json,widget_json,widget_html,nodes,edges,status\n"
        )
        for item in combined:
            handle.write(
                f"{item.get('source')},{item.get('file_stub')},{item.get('graph_json')},"
                f"{item.get('widget_json')},{item.get('widget_html')},{item.get('nodes')},"
                f"{item.get('edges')},{item.get('status')}\n"
            )
    return combined


def load_widget_graph(widget_path: Path) -> Optional[dict]:
    if not widget_path.exists():
        return None
    return json.loads(widget_path.read_text(encoding="utf-8"))


def append_graph(
    collector: Dict[str, dict], edges: List[dict], payload: dict, provider: str
) -> None:
    for node in payload.get("nodes", []):
        node_id = node.get("id")
        if not node_id:
            continue
        current = collector.setdefault(
            node_id,
            {
                "id": node_id,
                "title": node.get("title"),
                "citations": node.get("citations") or 1,
                "doi": node.get("doi"),
                "category": node.get("category"),
                "sources": set(),
            },
        )
        current_citations = current.get("citations") or 1
        incoming_citations = node.get("citations") or 1
        current["citations"] = max(current_citations, incoming_citations)
        if node.get("title"):
            current["title"] = node.get("title")
        if node.get("doi") and not current.get("doi"):
            current["doi"] = node.get("doi")
        if node.get("category"):
            current["category"] = node.get("category")
        current["sources"].add(provider)

    for edge in payload.get("links", []):
        src = edge.get("source") or edge.get("from")
        tgt = edge.get("target") or edge.get("to")
        if not src or not tgt:
            continue
        edges.append(
            {
                "source": src,
                "target": tgt,
                "weight": edge.get("weight", 1),
                "provider": provider,
            }
        )


def build_combined_network(semantic_rows: List[SemanticSummary]) -> None:
    nodes: Dict[str, dict] = {}
    edges: List[dict] = []

    for row in semantic_rows:
        payload = load_widget_graph(row.widget_json)
        if payload:
            append_graph(nodes, edges, payload, provider="semantic_scholar")

    for entry in load_connected_manifest():
        widget_rel = entry.get("widget_graph")
        if not widget_rel:
            continue
        widget_path = ROOT / widget_rel
        payload = load_widget_graph(widget_path)
        if payload:
            append_graph(nodes, edges, payload, provider="connected_papers")

    combined_nodes = []
    for node_id, data in nodes.items():
        combined_nodes.append(
            {
                "id": node_id,
                "title": data.get("title") or node_id,
                "citations": data.get("citations", 1),
                "category": data.get("category"),
                "doi": data.get("doi"),
                "sources": sorted(data.get("sources", [])),
            }
        )

    combined_payload = {"nodes": combined_nodes, "links": edges}
    combined_json = NETWORK_DIR / "combined_network_widget.json"
    combined_json.write_text(json.dumps(combined_payload, indent=2), encoding="utf-8")
    combined_html = NETWORK_DIR / "combined_network_widget.html"
    run_r_widget(combined_json, combined_html)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build Semantic Scholar widgets and merge manifests."
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Regenerate widget JSON/HTML even if cached versions exist.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    semantic_rows = build_semantic_widgets(force=args.force)
    if not semantic_rows:
        print("No Semantic Scholar graphs found to convert.")
        return
    write_semantic_manifest(semantic_rows)
    build_combined_manifest(semantic_rows)
    build_combined_network(semantic_rows)
    print("Semantic Scholar widgets and combined manifests updated.")


if __name__ == "__main__":
    main()
