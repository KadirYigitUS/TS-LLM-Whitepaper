# System Instruction Snapshot

- **Lead Contact**: Kadir Yiğit US — kyigitus@gmail.com
- **Co-author Credits**: GPT-5.1-Codex (Preview), Gemini 3.0 Pro, and GitHub Copilot inside VS Code.
- **Mandates**:
  - Keep APA ordering and translator-centric terminology across notes, scripts, and exports.
  - Document every automation helper inside `/script/`.
  - Maintain an Obsidian-first workflow; notes must remain compatible with Mermaid and callouts.
- **Publishing Requirements**:
  - GitHub Pages must host the interactive widgets (Semantic Scholar + ConnectedPapers) without exceeding file-size limits.
  - `white_paper.html` is the primary delivery artifact, backed by `white_paper.md` for LaTeX conversion.
- **Build Chain Overview**:
  1. `python script/connected_papers.py` (requires `CONNECTEDPAPERS_TOKEN` or `--allow-test`).
  2. `python script/build_semantic_widgets.py` (converts Semantic Scholar graphs + merges manifests).
  3. `python script/white_paper_builder.py` (runs the two steps above automatically, assembles Markdown + HTML, injects widget listings, and renders Mermaid diagrams via CDN).
- **Notes Archive**: Long-form coordination or AI-chat transcripts live under `docs_AI/` (ignored from git history per governance policy).
