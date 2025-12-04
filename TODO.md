# TODO — Technical Implementation Plan

## Hosting & Delivery Requirements
- [x] Record that GitHub Pages must embed interactive widgets and keep every asset below the platform's file-size limits.

## Reference Pipeline
- [x] Parse `References.md` plus `tables/*.csv` to confirm DOI coverage and bibliographic consistency.
- [x] Download every cited primary, secondary, and tertiary source via DOI or fallback web search; rename files in APA alphabetical order with numeric prefixes.
- [x] Store citation metadata (author, year, DOI, file path, category) for downstream scripts.

## Obsidian Vault Preparation
- [x] Write a `/script/obsidian_cleanup.py` utility to strip YAML front matter, remove "Technical Implementation Plan" sections, delete `// continue` markers, normalize tables, and append Obsidian tags/cross-links.
- [x] Run the cleaner over `Obsidian_Project/` and verify mermaid diagram embeds from `Visual_Assets.md` render correctly.
- [x] Add contextual cross-references between related notes (inline links + endnote references to `References.md`).

## White Paper Assembly
- [ ] Implement `/script/white_paper_builder.py` to merge the cleaned notes following `outline.md`, emitting `white_paper.md` (LaTeX-ready) and `white_paper.html` with internal anchors and download CTA.
- [ ] Inject contact block (Kadir Yiğit US — kyigitus@gmail.com; authored with GPT-5.1-Codex (Preview), Gemini 3.0 Pro, GitHub Copilot in VS Code).
- [ ] Ensure HTML supports interactive embeds (widgets, diagrams) without exceeding GitHub limits.

- [ ] Create `/script/connected_papers.py` to call `connectedpapers-py` for each citation category (primary, secondary, tertiary, overall) and save graph data/PNGs/JSON. *(seed files ready; API call pending token)*
- [ ] Develop `/script/network_widgets.R` to turn the graph data into R-based interactive widgets (node size = citations, color = category) for embedding.
- [ ] Link the resulting assets from `white_paper.html` and host standalone versions in the GitHub Pages bundle.

## Repository Scaffolding & Metadata
- [ ] Create `.gitignore`, `.vscode/`, `.copilot/`, and `system_instruct` configs reflecting the project workflow; ensure `docs_AI/` (meta-dialogue records) is ignored.
- [ ] Populate `README.md` with build instructions, download link for the white paper, and summary of interactive content.
- [ ] Move any AI-user dialogue or coordination notes into `docs_AI/` before final commit.
