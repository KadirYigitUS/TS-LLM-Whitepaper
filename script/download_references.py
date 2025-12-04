#!/usr/bin/env python3
"""Download reference PDFs/HTML assets using metadata from data/reference_metadata.json."""

from __future__ import annotations

import json
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional

import requests

ROOT = Path(__file__).resolve().parents[1]
META_PATH = ROOT / "data" / "reference_metadata.json"
DEST_DIR = ROOT / "references"
REPORT_PATH = ROOT / "data" / "download_report.json"
USER_AGENT = "TranslationStudiesLLM/0.1 (+https://github.com/)"
TIMEOUT = 45


@dataclass
class Reference:
    file_stub: str
    title: str
    doi: Optional[str]
    url: Optional[str]

    def slug(self) -> str:
        return self.file_stub or re.sub(r"[^a-z0-9]+", "_", self.title.lower()).strip(
            "_"
        )


def load_metadata() -> List[Reference]:
    records = json.loads(META_PATH.read_text(encoding="utf-8"))
    refs: List[Reference] = []
    for record in records:
        refs.append(
            Reference(
                file_stub=record.get("file_stub") or "",
                title=record.get("title") or record.get("raw")[:40],
                doi=record.get("doi"),
                url=record.get("url"),
            )
        )
    return refs


def arxiv_pdf(doi: str) -> Optional[str]:
    match = re.search(r"arXiv\.(\d{4}\.\d{5})(?:v\d+)?", doi)
    if not match:
        return None
    return f"https://arxiv.org/pdf/{match.group(1)}.pdf"


def candidate_urls(ref: Reference) -> Iterable[str]:
    seen = set()
    if ref.doi:
        if "arxiv" in ref.doi.lower():
            pdf_url = arxiv_pdf(ref.doi)
            if pdf_url:
                seen.add(pdf_url)
                yield pdf_url
        doi_url = f"https://doi.org/{ref.doi}"
        if doi_url not in seen:
            seen.add(doi_url)
            yield doi_url
    if ref.url and ref.url not in seen:
        seen.add(ref.url)
        yield ref.url


def save_binary(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)


def attempt_download(url: str) -> Optional[Dict[str, str]]:
    try:
        response = requests.get(
            url,
            timeout=TIMEOUT,
            headers={"User-Agent": USER_AGENT},
            allow_redirects=True,
        )
    except requests.RequestException as exc:
        return {"status": "error", "detail": str(exc)}
    content_type = response.headers.get("Content-Type", "").lower()
    if "pdf" in content_type or url.lower().endswith(".pdf"):
        return {
            "status": "pdf",
            "content": response.content,
            "content_type": content_type or "application/pdf",
        }
    return {
        "status": "html",
        "content": response.content,
        "content_type": content_type or "text/html",
    }


def download_all() -> None:
    refs = load_metadata()
    report = {}
    DEST_DIR.mkdir(parents=True, exist_ok=True)

    for ref in refs:
        stub = ref.slug() or "reference"
        pdf_path = DEST_DIR / f"{stub}.pdf"
        html_path = DEST_DIR / f"{stub}.html"
        if pdf_path.exists():
            report[stub] = {"status": "exists", "path": str(pdf_path.relative_to(ROOT))}
            continue
        success = False
        for url in candidate_urls(ref):
            result = attempt_download(url)
            if not result:
                continue
            if result["status"] == "pdf":
                save_binary(pdf_path, result["content"])  # type: ignore[index]
                report[stub] = {
                    "status": "downloaded",
                    "path": str(pdf_path.relative_to(ROOT)),
                    "source": url,
                }
                success = True
                break
            elif result["status"] == "html" and not html_path.exists():
                save_binary(html_path, result["content"])  # type: ignore[index]
                report[stub] = {
                    "status": "html_saved",
                    "path": str(html_path.relative_to(ROOT)),
                    "source": url,
                }
        if not success and stub not in report:
            report[stub] = {
                "status": "missing",
                "reason": "No accessible PDF/HTML",
                "source_attempts": list(candidate_urls(ref)),
            }
        time.sleep(1)

    REPORT_PATH.write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"Download report written to {REPORT_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    download_all()
