#!/usr/bin/env python3
"""Assemble the cleaned Obsidian notes into LaTeX-ready and HTML outputs."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
import textwrap
from html import unescape
from pathlib import Path
from typing import Dict, List, Tuple

try:
    import markdown  # type: ignore
except ImportError:  # pragma: no cover
    markdown = None  # noqa: N816

ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "Obsidian_Project"
OUTLINE = VAULT / "outline.md"
WHITE_PAPER_MD = ROOT / "white_paper.md"
WHITE_PAPER_HTML = ROOT / "white_paper.html"
MANIFEST_COMBINED = ROOT / "data" / "network_manifests" / "graph_manifest_combined.json"
NOTE_HTML_DIR = ROOT / "previews" / "notes"
DEFAULT_ORDER: List[str] = [
    "outline",
    "Combined_Primary_and_Secondary_Source_review_table",
    "Combined_Primary_and_Secondary_Source_review",
    "Beyond_prompt_engineering_-_What_is_Context_and_Context_Engineering",
    "Prompt_requirements_in_Prompt-Engineering_-_Similarity_of_Skopos_Theorie_and_Prompting_Practice.md.md",
    "Criticize_Empiric_TranslationStudies_and_current_use_of_LLMs_in_Translation_Studies_Literature",
    "Discussions",
    "Future_studies",
    "General_Terminology",
    "Visual_Assets",
    "Tertiary_Sources_review_table",
    "Tertiary_Sources_review",
    "Conclusion",
    "References",
]
WIDGET_EMBEDS = [
    {
        "title": "Semantic Scholar + ConnectedPapers Network",
        "description": "Merged citation graph built via script/build_semantic_widgets.py",
        "src": "data/network_manifests/combined_network_widget.html",
    }
]
CONTACT_BLOCK = textwrap.dedent(
    """
    ---
    ## Contact & Credits
    - Kadir Yiğit US — kyigitus@gmail.com
    - Prepared with GPT-5.1-Codex (Preview), Gemini 3.0 Pro, and GitHub Copilot inside VS Code.
    - Download the latest HTML: [white_paper.html](white_paper.html)
    """
)

INDEX_INTRO = textwrap.dedent(
    """
        # TS-LLM Knowledge Base Gateway

        This landing page now serves as the navigation hub for the modular notes that make up the
        Translation Studies × LLM corpus. Use the outline below to understand how the arguments are
        staged, then follow the per-section HTML links to read each module in isolation. Every file is
        still sourced from the Obsidian vault, ensuring that updates to the notes automatically refresh
        the public-facing pages.

        ## How to Use This Page
        - **Start with the outline** to see how the manuscript flows.
        - **Jump into any section** via the Per-Note HTML Library—each entry is a self-contained page
            with Mermaid diagrams fully rendered.
        - **Download** the LaTeX-ready Markdown if you need an offline bundle or want to compile a PDF.
        """
).strip()

WIKI_LINK_PATTERN = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|([^\]]+))?\]\]")

HTML_TEMPLATE = textwrap.dedent(
    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8" />
        <title>{title}</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/github-markdown-css@5.4.0/github-markdown.min.css" />
        <style>
            body {{ margin: 2rem; }}
            .markdown-body {{ max-width: 960px; margin: auto; }}
            header.site-header {{ display: flex; justify-content: flex-end; gap: 1rem; margin-bottom: 1.5rem; }}
            header.site-header a {{ font-size: 0.9rem; color: #0366d6; text-decoration: none; }}
            header.site-header a:hover {{ text-decoration: underline; }}
            iframe.widget {{ width: 100%; height: 520px; border: none; }}
            figure.interactive-widget {{ margin: 2rem 0; }}
            figure.interactive-widget figcaption {{ font-size: 0.9rem; color: #555; }}
            .note-library ul {{ margin-left: 1.2rem; }}
            .note-library li {{ margin-bottom: 0.4rem; }}
            .page-intro {{ background: #f6f8fa; padding: 1rem 1.5rem; border-radius: 0.5rem; margin-bottom: 2rem; }}
        </style>
        <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
        <script>mermaid.initialize({{ startOnLoad: true, securityLevel: 'loose' }});</script>
    </head>
    <body class="markdown-body">
        <header class="site-header">
            {home_link}
            <a class="download-link" href="{download_href}" download>Download Markdown</a>
        </header>
        {widgets}
        {body}
    </body>
    </html>
    """
)


def list_vault_notes() -> List[Path]:
    return sorted(VAULT.glob("*.md"))


def normalize_candidate(raw: str) -> str:
    candidate = raw.strip().strip("`")
    if "#" in candidate:
        candidate = candidate.split("#", 1)[0]
    candidate = candidate.strip().replace("...", "")
    if not candidate:
        return ""
    if not candidate.endswith(".md"):
        candidate = f"{candidate}.md"
    return candidate


def fuzzy_match_note(candidate: str) -> str:
    candidate_norm = re.sub(r"[^a-z0-9]", "", candidate.lower())
    if not candidate_norm:
        return candidate
    for note in list_vault_notes():
        note_norm = re.sub(r"[^a-z0-9]", "", note.stem.lower())
        if note_norm.startswith(candidate_norm):
            return note.name
    return candidate


def extract_order_from_outline() -> List[str]:
    if not OUTLINE.exists():
        return []
    text = OUTLINE.read_text(encoding="utf-8")
    candidates: List[str] = []
    code_refs = re.findall(r"`([^`]+)`", text)
    wiki_refs = re.findall(r"\[\[([^\]]+)\]\]", text)
    for raw in (*code_refs, *wiki_refs):
        normalized = normalize_candidate(raw)
        if not normalized:
            continue
        resolved = fuzzy_match_note(normalized)
        if resolved not in candidates:
            candidates.append(resolved)
    ordered: List[str] = []
    for note in candidates:
        filename = note if note.endswith(".md") else f"{note}.md"
        if (VAULT / filename).exists() and filename not in ordered:
            ordered.append(filename)
    for fallback in DEFAULT_ORDER:
        filename = fallback if fallback.endswith(".md") else f"{fallback}.md"
        if (VAULT / filename).exists() and filename not in ordered:
            ordered.append(filename)
    return ordered


def read_note(name: str) -> str:
    filename = name if name.endswith(".md") else f"{name}.md"
    path = VAULT / filename
    if not path.exists():
        raise FileNotFoundError(f"Missing note: {path}")
    return path.read_text(encoding="utf-8").strip()


def assemble_markdown() -> Tuple[str, List[Tuple[str, str]]]:
    note_order = extract_order_from_outline()
    if not note_order:
        raise RuntimeError("Unable to determine note order from outline.md")
    note_entries: List[Tuple[str, str]] = []
    for name in note_order:
        note_entries.append((name, read_note(name)))
    pieces = [content for _, content in note_entries]
    pieces.append(CONTACT_BLOCK.strip())
    body = "\n\n".join(pieces).strip()
    today = dt.date.today().strftime("%B %d, %Y")
    header = textwrap.dedent(
        f"""
        % Auto-generated white paper
        % Digital Humanities Systems Architect
        % {today}
        """
    ).strip()
    return f"{header}\n\n{body}\n", note_entries


def write_markdown() -> Tuple[str, List[Tuple[str, str]]]:
    content, note_entries = assemble_markdown()
    WHITE_PAPER_MD.write_text(content, encoding="utf-8")
    return content, note_entries


def convert_mermaid_blocks(html_body: str) -> str:
    pattern = re.compile(
        r'<pre><code class="language-mermaid">(.*?)</code></pre>', re.DOTALL
    )

    def _replace(match: re.Match[str]) -> str:
        code = unescape(match.group(1))
        return f'<div class="mermaid">\n{code}\n</div>'

    return pattern.sub(_replace, html_body)


def load_widget_manifest() -> List[dict]:
    if not MANIFEST_COMBINED.exists():
        return []
    try:
        return json.loads(MANIFEST_COMBINED.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []


def build_widget_block() -> str:
    snippets = []
    for widget in WIDGET_EMBEDS:
        src = widget.get("src")
        if not src:
            continue
        path = ROOT / src
        if not path.exists():
            continue
        title = widget.get("title", "Interactive Widget")
        caption = widget.get("description", "Interactive asset")
        snippets.append(
            textwrap.dedent(
                f"""
                <figure class=\"interactive-widget\">
                    <iframe class=\"widget\" loading=\"lazy\" src=\"{src}\" title=\"{title}\"></iframe>
                    <figcaption>{caption}</figcaption>
                </figure>
                """
            ).strip()
        )
    manifest_entries = []
    for record in load_widget_manifest():
        widget_html = record.get("widget_html")
        if not widget_html:
            continue
        widget_path = ROOT / widget_html
        if not widget_path.exists():
            continue
        label = record.get("file_stub", "widget").replace("_", " ")
        manifest_entries.append(
            f'<li><a href="{widget_html}" target="_blank" rel="noopener">{label}</a> '
            f"({record.get('source', 'graph')})</li>"
        )
    if manifest_entries:
        snippets.append(
            '<div class="widget-list"><h3>Widget Library</h3><ul>'
            + "\n".join(manifest_entries)
            + "</ul></div>"
        )
    if not snippets:
        return ""
    return (
        '<section id="interactive-assets">\n'
        "  <h2>Interactive Assets</h2>\n" + "\n".join(snippets) + "\n</section>"
    )


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "section"


def build_slug_map(note_entries: List[Tuple[str, str]]) -> Dict[str, str]:
    slug_map: Dict[str, str] = {}
    used: set[str] = set()
    for filename, _content in note_entries:
        base = slugify(Path(filename).stem)
        candidate = base
        counter = 2
        while candidate in used:
            candidate = f"{base}-{counter}"
            counter += 1
        slug_map[filename] = candidate
        used.add(candidate)
    return slug_map


def replace_wiki_links(
    md_text: str, slug_map: Dict[str, str], base_href: str = ""
) -> str:
    def _replace(match: re.Match[str]) -> str:
        target = match.group(1).strip()
        label = (match.group(2) or target).strip()
        normalized = normalize_candidate(target)
        resolved = fuzzy_match_note(normalized)
        filename = resolved if resolved.endswith(".md") else f"{resolved}.md"
        slug = slug_map.get(filename)
        if not slug:
            return label
        href = f"{base_href}previews/notes/{slug}.html"
        return f"[{label}]({href})"

    return WIKI_LINK_PATTERN.sub(_replace, md_text)


def derive_display_title(content: str, filename: str) -> str:
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip()
    fallback = Path(filename).stem.replace("_", " ").replace("-", " ").strip()
    return fallback if fallback else "Section"


def extract_summary(content: str, max_length: int = 200) -> str:
    for line in content.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("> Tags"):
            continue
        summary = re.sub(r"`([^`]+)`", r"\1", stripped)
        summary = re.sub(r"\[\[(.*?)\]\]", r"\1", summary)
        if len(summary) > max_length:
            summary = summary[: max_length - 3].rstrip() + "..."
        return summary
    return ""


def render_markdown_html(md_text: str) -> str:
    if markdown is None:  # pragma: no cover
        raise RuntimeError("Markdown library is unavailable; cannot render HTML.")
    html_body = markdown.markdown(  # type: ignore[attr-defined]
        md_text,
        extensions=["toc", "tables", "fenced_code", "attr_list"],
        extension_configs={"toc": {"permalink": "#"}},
    )
    return convert_mermaid_blocks(html_body)


def render_page_html(
    *,
    page_title: str,
    body_html: str,
    widgets_block: str = "",
    home_href: str = "",
    download_href: str = "white_paper.md",
) -> str:
    home_link = (
        f'<a class="home-link" href="{home_href}">&larr; Back to Outline</a>'
        if home_href
        else ""
    )
    return HTML_TEMPLATE.format(
        title=page_title,
        widgets=widgets_block,
        body=body_html,
        home_link=home_link,
        download_href=download_href,
    )


def run_helper(description: str, command: list[str]) -> None:
    print(f"[task] {description}: {' '.join(command)}")
    subprocess.run(command, check=True)


def refresh_connected_graphs(allow_test_token: bool, skip: bool) -> None:
    if skip:
        print("Skipping ConnectedPapers refresh (flagged).")
        return
    env_token = os.getenv("CONNECTEDPAPERS_TOKEN") or os.getenv(
        "CONNECTED_PAPERS_API_KEY"
    )
    if not env_token and not allow_test_token:
        print(
            "ConnectedPapers token missing. Skipping API refresh. Set CONNECTEDPAPERS_TOKEN"
            " or use --allow-test-token to fetch demo graphs."
        )
        return
    script_path = ROOT / "script" / "connected_papers.py"
    cmd = [sys.executable, str(script_path)]
    if allow_test_token and not env_token:
        cmd.append("--allow-test")
    run_helper("ConnectedPapers graph refresh", cmd)


def refresh_widget_assets(skip: bool, force: bool) -> None:
    if skip:
        print("Skipping Semantic Scholar widget build (flagged).")
        return
    script_path = ROOT / "script" / "build_semantic_widgets.py"
    cmd = [sys.executable, str(script_path)]
    if force:
        cmd.append("--force")
    run_helper("Semantic Scholar + widget manifest rebuild", cmd)


def write_html(note_entries: List[Tuple[str, str]]) -> None:
    if markdown is None:
        stub = textwrap.dedent(
            """
            <html><body>
            <p><strong>Markdown to HTML conversion requires the 'markdown' package.</strong></p>
            </body></html>
            """
        )
        WHITE_PAPER_HTML.write_text(stub, encoding="utf-8")
        return
    NOTE_HTML_DIR.mkdir(parents=True, exist_ok=True)
    for stale in NOTE_HTML_DIR.glob("*.html"):
        stale.unlink()
    slug_map = build_slug_map(note_entries)
    note_cards = []
    for filename, content in note_entries:
        slug = slug_map[filename]
        processed_md = replace_wiki_links(content, slug_map, base_href="../../")
        html_body = render_markdown_html(processed_md)
        title = derive_display_title(content, filename)
        summary = extract_summary(content)
        note_body = f'<section class="note-content">{html_body}</section>'
        page_html = render_page_html(
            page_title=title,
            body_html=note_body,
            widgets_block="",
            home_href="../../white_paper.html",
            download_href="../../white_paper.md",
        )
        (NOTE_HTML_DIR / f"{slug}.html").write_text(page_html, encoding="utf-8")
        note_cards.append({"title": title, "slug": slug, "summary": summary})
    outline_content = next(
        (content for name, content in note_entries if Path(name).stem == "outline"),
        OUTLINE.read_text(encoding="utf-8") if OUTLINE.exists() else "",
    )
    outline_html = render_markdown_html(replace_wiki_links(outline_content, slug_map))
    intro_html = render_markdown_html(INDEX_INTRO)
    contact_html = render_markdown_html(CONTACT_BLOCK.strip())
    note_list_items = "\n".join(
        (
            f'<li><a href="previews/notes/{card["slug"]}.html">{card["title"]}</a>'
            + (f" — {card['summary']}" if card["summary"] else "")
            + "</li>"
        )
        for card in note_cards
    )
    body_html = textwrap.dedent(
        f"""
        <section class=\"page-intro\">
            {intro_html}
        </section>
        <section class=\"outline-section\">
            <h2>Master Outline</h2>
            {outline_html}
        </section>
        <section class=\"note-library\">
            <h2>Per-Note HTML Library</h2>
            <ul>
                {note_list_items}
            </ul>
        </section>
        <section class=\"contact\">
            {contact_html}
        </section>
        """
    )
    WHITE_PAPER_HTML.write_text(
        render_page_html(
            page_title="TS-LLM Knowledge Base",
            body_html=body_html,
            widgets_block=build_widget_block(),
            home_href="",
            download_href="white_paper.md",
        ),
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build the TS-LLM white paper outputs."
    )
    parser.add_argument(
        "--skip-html", action="store_true", help="Only emit white_paper.md"
    )
    parser.add_argument(
        "--skip-widget-refresh",
        action="store_true",
        help="Do not rebuild Semantic Scholar/ConnectedPapers widget manifests.",
    )
    parser.add_argument(
        "--force-widget-refresh",
        action="store_true",
        help="Regenerate widget payloads even if cached files exist.",
    )
    parser.add_argument(
        "--skip-connected-refresh",
        action="store_true",
        help="Do not call script/connected_papers.py automatically.",
    )
    parser.add_argument(
        "--allow-test-token",
        action="store_true",
        help="Pass --allow-test to the ConnectedPapers refresh when an API key is absent.",
    )
    args = parser.parse_args()
    refresh_connected_graphs(
        allow_test_token=args.allow_test_token,
        skip=args.skip_connected_refresh,
    )
    refresh_widget_assets(
        skip=args.skip_widget_refresh,
        force=args.force_widget_refresh,
    )
    _markdown_text, note_entries = write_markdown()
    if not args.skip_html:
        write_html(note_entries)
    print(
        "white_paper.md created."
        + (" HTML skipped." if args.skip_html else " HTML site rendered.")
    )


if __name__ == "__main__":
    main()
