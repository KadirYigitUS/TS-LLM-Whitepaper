#!/usr/bin/env python3
"""Aggregate reference metadata for downstream automation."""

from __future__ import annotations

import csv
import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

ROOT = Path(__file__).resolve().parents[1]
REF_FILE = ROOT / "Obsidian_Project" / "References.md"
LLM_TABLE = ROOT / "tables" / "llm_source_review.csv"
TERTIARY_TABLE = ROOT / "tables" / "tertiary_sources.csv"
OUT_JSON = ROOT / "data" / "reference_metadata.json"
OUT_CSV = ROOT / "data" / "reference_metadata.csv"


def _strip_front_matter(text: str) -> str:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return parts[2]
    return text


@dataclass
class ReferenceEntry:
    category: str
    raw: str
    authors: str = ""
    year: str = ""
    title: str = ""
    doi: Optional[str] = None
    url: Optional[str] = None
    stage: Optional[str] = None
    vector: Optional[str] = None
    key: str = field(init=False, default="unknown_0000")
    ordinal: Optional[int] = None
    file_stub: Optional[str] = None

    def refresh_key(self) -> None:
        authors_norm = self.authors.split(",")[0].split("&")[0].strip()
        key_root = _slugify(authors_norm) if authors_norm else "unknown"
        year_part = self.year if self.year else "0000"
        self.key = f"{key_root}_{year_part}"

    def apify(self, ordinal: int) -> None:
        self.ordinal = ordinal
        base = self.authors.split(",")[0].strip().replace(" ", "_") or "ref"
        year_part = self.year or "0000"
        self.file_stub = f"{ordinal:03d}_{base}_{year_part}"


DOI_PATTERN = re.compile(r"(10\.\d{4,9}/[^\s]+)", re.I)
YEAR_PATTERN = re.compile(r"\((\d{4})\)")


def _slugify(text: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "_", text.lower())
    return normalized.strip("_") or "ref"


def parse_references(md_path: Path) -> List[ReferenceEntry]:
    content = _strip_front_matter(md_path.read_text(encoding="utf-8"))
    lines = content.splitlines()
    entries: List[ReferenceEntry] = []
    buffer: List[str] = []
    category = None

    def flush() -> None:
        if buffer and category:
            raw = " ".join(buffer).strip()
            if raw and not raw.startswith("- ["):
                entries.append(ReferenceEntry(category, raw))
        buffer.clear()

    for line in lines:
        if line.startswith("## "):
            flush()
            category = line[3:].strip()
            continue
        if line.startswith("#") or line.strip() == "":
            flush()
            continue
        buffer.append(line.strip())
    flush()

    for entry in entries:
        match = YEAR_PATTERN.search(entry.raw)
        if match:
            entry.year = match.group(1)
            entry.authors = entry.raw[: match.start()].strip().rstrip(".")
            remainder = entry.raw[match.end() :].lstrip(". ")
        else:
            remainder = entry.raw
        # Title extraction (up to double period or two spaces before italic markers)
        title_split = remainder.split(".")
        entry.title = title_split[0].replace("*", "").strip()
        doi_match = DOI_PATTERN.search(entry.raw)
        if doi_match:
            entry.doi = doi_match.group(1)
            entry.url = f"https://doi.org/{entry.doi}"
        entry.refresh_key()
    return entries


def table_key(label: str) -> Optional[str]:
    match = re.search(r"(.+?)\s*\((\d{4})\)", label)
    if not match:
        return None
    author_chunk = match.group(1)
    primary_token = re.split(r"&|and|,", author_chunk)[0].strip()
    primary_token = re.sub(r"et\s+al\.?(?=$|\s)", "", primary_token, flags=re.I).strip()
    first_author = _slugify(primary_token)
    year = match.group(2)
    return f"{first_author}_{year}"


def enrich_from_tables(entries: List[ReferenceEntry]) -> None:
    key_map: Dict[str, ReferenceEntry] = {entry.key: entry for entry in entries}

    def resolve(target_key: Optional[str]) -> Optional[ReferenceEntry]:
        if not target_key:
            return None
        if target_key in key_map:
            return key_map[target_key]
        prefix = target_key.rsplit("_", 1)[0]
        for key, entry in key_map.items():
            if key.startswith(f"{prefix}_"):
                return entry
        return None

    if LLM_TABLE.exists():
        with LLM_TABLE.open(newline="", encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                entry = resolve(table_key(row["Citation"]))
                if entry:
                    entry.stage = row.get("Stage")

    if TERTIARY_TABLE.exists():
        with TERTIARY_TABLE.open(newline="", encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                entry = resolve(table_key(row["Source"]))
                if entry:
                    entry.vector = row.get("Vector")


def write_outputs(entries: List[ReferenceEntry]) -> None:
    sorted_entries = sorted(entries, key=lambda e: (e.authors.lower(), e.year))
    for idx, entry in enumerate(sorted_entries, 1):
        entry.apify(idx)

    OUT_JSON.write_text(
        json.dumps(
            [asdict(entry) for entry in sorted_entries], indent=2, ensure_ascii=False
        ),
        encoding="utf-8",
    )

    with OUT_CSV.open("w", newline="", encoding="utf-8") as fh:
        fieldnames = [
            "ordinal",
            "file_stub",
            "category",
            "authors",
            "year",
            "title",
            "doi",
            "url",
            "stage",
            "vector",
            "raw",
        ]
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for entry in sorted_entries:
            writer.writerow(
                {
                    "ordinal": entry.ordinal,
                    "file_stub": entry.file_stub,
                    "category": entry.category,
                    "authors": entry.authors,
                    "year": entry.year,
                    "title": entry.title,
                    "doi": entry.doi,
                    "url": entry.url,
                    "stage": entry.stage,
                    "vector": entry.vector,
                    "raw": entry.raw,
                }
            )


def main() -> None:
    if not REF_FILE.exists():
        raise SystemExit(f"Missing References.md at {REF_FILE}")
    entries = parse_references(REF_FILE)
    enrich_from_tables(entries)
    write_outputs(entries)
    print(f"Wrote {len(entries)} reference records to {OUT_JSON.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
