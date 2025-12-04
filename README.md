# TS-LLM Knowledge Stack

Obsidian-first research corpus that synthesizes Translation Studies theory with Large Language Models (LLMs). The repo keeps the vault clean, automates ConnectedPapers + Semantic Scholar graphs, and emits both `white_paper.md` (LaTeX-ready) and `white_paper.html` (embed-ready for GitHub Pages).

## Prerequisites
- Conda environment with Python 3.10+ and R (visNetwork + htmlwidgets). The shared stack uses the `BA_Gensim` env: `/home/ben/miniconda3/envs/BA_Gensim`.
- `connectedpapers-py` API token exported as `CONNECTEDPAPERS_TOKEN` (or pass `--allow-test-token` for demo data).
- System dependencies for Mermaid-ready HTML already handled via CDN.

## Build Pipeline (run from repo root)
```bash
# 1. Refresh ConnectedPapers graphs (skips if token missing)
conda run -n BA_Gensim python script/white_paper_builder.py --skip-html

# 2. Full publish (widgets + markdown + HTML)
conda run -n BA_Gensim python script/white_paper_builder.py
```
The builder automatically:
1. Invokes `script/connected_papers.py` when a token is available (or when `--allow-test-token` is supplied).
2. Invokes `script/build_semantic_widgets.py` to regenerate all Semantic Scholar widgets and the combined manifest.
3. Converts the ordered Obsidian notes (driven by `Obsidian_Project/outline.md`) into `white_paper.md` and `white_paper.html`, injects the contact block, transforms Mermaid code fences into live diagrams, and lists every generated widget for download.

### Useful flags
| Flag | Purpose |
| --- | --- |
| `--skip-connected-refresh` | Use cached ConnectedPapers payloads. |
| `--allow-test-token` | Falls back to ConnectedPapers demo graphs when no API key is present. |
| `--skip-widget-refresh` | Keep the existing Semantic Scholar widgets. |
| `--force-widget-refresh` | Rebuild widgets even if cached JSON/HTML exist. |
| `--skip-html` | Only emit `white_paper.md` (for LaTeX workflows). |

## Interactive Assets
- Primary embed: `data/network_manifests/combined_network_widget.html` (auto-lazy-loaded in `white_paper.html`).
- Widget index: automatically pulled from `data/network_manifests/graph_manifest_combined.json` and shown in the HTML under **Widget Library**.
- Source scripts live in `/script/` (see `build_semantic_widgets.py`, `connected_papers.py`, `network_widgets.R`).

## Repository Structure
- `Obsidian_Project/` – cleaned notes ready for Obsidian + Mermaid.
- `script/` – automation helpers (always document new utilities here).
- `data/` – reference metadata, raw Semantic Scholar graphs, widget outputs, and ConnectedPapers payloads.
- `system_instruct/` – high-level mandates & publishing rules.
- `docs_AI/` – reserved for coordination transcripts (git-ignored).

## Performance & Troubleshooting
- **Mermaid not visible**: `white_paper_builder.py` now rewrites ` ```mermaid` blocks into `<div class="mermaid">` and pulls the Mermaid CDN automatically. Re-run the builder if diagrams still show as code blocks.
- **Slow HTML load**: The heaviest asset is the combined knowledge-graph iframe. It lazily loads, but you can temporarily hide the embed by replacing `loading="lazy"` with `loading="lazy" data-disabled` in `Obsidian_Project/Visual_Assets.md` during drafting.
- **ConnectedPapers throttling**: If the API token is absent, the builder skips the refresh and logs a warning. Export the token (or pass `--allow-test-token`) before publishing.

## Credits
- Lead Agent: Digital Humanities Systems Architect (kyigitus@gmail.com)
- Toolchain: GPT-5.1-Codex (Preview), Gemini 3.0 Pro, GitHub Copilot (VS Code)
