#!/usr/bin/env python3
"""Clean duplicated Obsidian notes for publication."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List, Optional

ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "Obsidian_Project"
RELATED_NOTES = ["outline", "References", "General_Terminology", "Visual_Assets"]
VISUAL_EMBEDS: Dict[str, str] = {
    "Combined_Primary_and_Secondary_Source_review": "1. The Evolutionary Arc of LLMs",
    "Combined_Primary_and_Secondary_Source_review_table": "1. The Evolutionary Arc of LLMs",
    "Prompt_requirements_in_Prompt-Engineering_-_Similarity_of_Skopos_Theorie_and_Prompting_Practice": "2. The Skopos Prompting Triangle",
    "Discussions": "2. The Skopos Prompting Triangle",
    "Beyond_prompt_engineering_-_What_is_Context_and_Context_Engineering": "3. Context Engineering: The Hallidayan Injection",
    "Future_studies": "3. Context Engineering: The Hallidayan Injection",
    "General_Terminology": "4. The LLM Processing Pipeline (Simplified)",
}

TIP_PATTERN = re.compile(
    r"#\s+Technical Implementation Plan:[\s\S]*?(?:\n---\n|\Z)", re.IGNORECASE
)
TAG_PATTERN = re.compile(r"tags:\s*\[(.*?)\]", re.IGNORECASE | re.DOTALL)


def strip_front_matter(text: str) -> tuple[str, List[str]]:
    if not text.startswith("---"):
        return text, []
    end = text.find("\n---", 3)
    if end == -1:
        return text, []
    front_matter = text[3:end].strip()
    tags: List[str] = []
    match = TAG_PATTERN.search(front_matter)
    if match:
        raw_tags = match.group(1)
        parsed: List[str] = []
        for item in raw_tags.split(","):
            cleaned = item.strip().strip("'\"")
            if cleaned:
                parsed.append(cleaned)
        tags = parsed
    remainder = text[end + 4 :]
    return remainder.lstrip(), tags


def remove_tip(text: str) -> str:
    return TIP_PATTERN.sub("", text, count=1).lstrip()


def remove_comment_lines(text: str) -> str:
    return re.sub(r"^//.*$", "", text, flags=re.MULTILINE)


def format_tags(tags: List[str]) -> str:
    if not tags:
        return ""
    cleaned = []
    for tag in tags:
        token = re.sub(r"[^A-Za-z0-9]+", "_", tag.strip())
        if token:
            cleaned.append(f"#{token}")
    return " ".join(cleaned)


def cross_reference_block(stem: str) -> str:
    links = []
    for note in RELATED_NOTES:
        if note.lower() == stem.lower():
            continue
        links.append(f"[[{note}]]")
    if not links:
        return ""
    bullets = "\n".join(f"- {link}" for link in links)
    return f"\n---\n## Cross-References\n{bullets}\n"


def visual_embed(stem: str) -> str:
    section = VISUAL_EMBEDS.get(stem)
    if not section:
        return ""
    return f"\n![[Visual_Assets#{section}]]\n"


def normalize_stem(path: Path) -> str:
    stem = path.stem
    if stem.endswith(".md"):
        stem = stem[:-3]
    return stem


def process_file(path: Path) -> None:
    original = path.read_text(encoding="utf-8")
    body, tags = strip_front_matter(original)
    body = remove_tip(body)
    body = remove_comment_lines(body)
    body = re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"

    tag_line = format_tags(tags)
    parts: List[str] = []
    if tag_line:
        parts.append(f"> Tags: {tag_line}\n")
    embed = visual_embed(normalize_stem(path))
    if embed:
        parts.append(embed)
    parts.append(body)
    parts.append(cross_reference_block(normalize_stem(path)))
    cleaned = "\n".join(part for part in parts if part).rstrip() + "\n"
    path.write_text(cleaned, encoding="utf-8")
    print(f"Cleaned {path.relative_to(VAULT)}")


def main() -> None:
    if not VAULT.exists():
        raise SystemExit(f"Missing vault: {VAULT}")
    for path in sorted(VAULT.glob("*.md")):
        process_file(path)


if __name__ == "__main__":
    main()
