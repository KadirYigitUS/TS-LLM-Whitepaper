---
title: TS-LLM Knowledge Stack
---

# TS-LLM Knowledge Stack

This documentation hub transforms the Obsidian-first manuscript corpus into a Read the Docs site that translators, computational humanists, and tooling engineers can browse together. Every page keeps the translator-centered terminology mandate from `AGENTS.md`, cites sources in APA order, and documents automation hooks from `/script/`.

```{admonition} Publishing context
:class: tip
The GitHub repository `KadirYigitUS/TS-LLM-Whitepaper` powers https://ts-llm-whitepaper.readthedocs.io/.
Pushes to `main` trigger Read the Docs builds that install `docs/requirements.txt`. GitHub Pages continues to host large interactive widgets referenced from `_static/` if they exceed RTD limits.
```

## English
```{toctree}
:maxdepth: 2
:hidden:

en/index
en/getting_started
en/build_pipeline
en/knowledge_graphs
en/obsidian_workflow
en/repository_structure
en/troubleshooting
en/general_terminology
en/discussions
en/future_studies
en/conclusion
en/criticisms
en/references
```
Visit the English tree when you need the full TS-to-LLM argument, complete vault exports, and end-to-end build notes.

## Türkçe
```{toctree}
:maxdepth: 2
:hidden:

tr/index
tr/getting_started
tr/build_pipeline
tr/knowledge_graphs
tr/obsidian_workflow
tr/repository_structure
tr/troubleshooting
tr/general_terminology
tr/references
```
Türkçe bölümü, araştırma argümanının özetlenmiş fakat işlevsel sürümünü ve saha ekipleri için pratik yönergeleri sunar.

```{toctree}
:caption: Developer Resources
:maxdepth: 1

mermaid_demo
api_reference/index
```

## Read the Docs localization checklist
1. In the Read the Docs dashboard, create a project for Turkish (e.g., `ts-llm-whitepaper-tr`) that tracks the same repository and sets `Language = Turkish`.
2. Under **Admin → Translations** of the English project, add the Turkish project so RTD renders `/tr/latest/` alongside `/en/latest/`.
3. Keep both versions on the `main` branch—the language switcher automatically appears once RTD detects the linked projects.
4. Use the `api` Makefile target when scripts change, commit the regenerated `docs/source/api_reference/*.md`, and redeploy.
