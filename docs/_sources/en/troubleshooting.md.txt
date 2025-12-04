---
title: Troubleshooting — Probability Meets Purpose
---

# Troubleshooting

::::{tab-set}
:::{tab-item} English
English triage guide below.
:::
:::{tab-item} Türkçe
:doc:`Türkçe sorun giderme özeti <tr/troubleshooting>`
:::
::::

This guide distills the pain points captured in `Discussions.md`, `Future_studies.md`, and `Conclusion.md`. Each scenario lists the probabilistic cause plus the translator-centered remedy.

## 1. Outputs Collapse to "Average" English
- **Symptom**: Marketing copy sounds generic, idioms disappear.
- **Why**: Scaling laws optimize for perplexity → regression to the mean (Kaplan et al., 2020).
- **Fix**: Revisit the prompt commission. Specify audience, tone, and desired surprise level. Inject curated examples (few-shot) that represent the target register.

## 2. Model Refuses Sensitive Translations
- **Symptom**: Commercial APIs decline to translate historical testimonies or legal evidence.
- **Why**: RLHF safety (Ouyang et al., 2022) prioritizes "harmlessness" over Nord’s loyalty.
- **Fix**: Switch to an auditable open-weight model (e.g., LLaMA) running locally, or craft prompts that explain the legal/archival Skopos. Record the justification for compliance reviews.

## 3. Context Window Forgetfulness
- **Symptom**: Long chapters drift off-topic or contradict earlier terms.
- **Why**: The context window is finite; once tokens fall out, they are gone.
- **Fix**: Apply Context Engineering — chunk, summarize, and inject Hallidayan Field/Tenor/Mode packets ahead of each segment. Use RAG for terminology.

## 4. Widget or Mermaid Failures on Read the Docs
- **Symptom**: Interactive graphs fail to load or Mermaid syntax renders as code blocks.
- **Why**: Missing CDN initialization or CSP restrictions.
- **Fix**: Confirm `_static/js/mermaid-init.js` ships with the build. For large HTML widgets, deploy to GitHub Pages and iframe them via HTTPS.

## 5. API Docs Break the Build
- **Symptom**: Autodoc raises `ImportError` for optional dependencies.
- **Why**: Read the Docs environment lacks heavy packages (`connectedpapers`, `pandas`, etc.).
- **Fix**: Add missing modules to `autodoc_mock_imports` (already done) and regenerate `api_reference/*.md` through `make api` after editing scripts.

## 6. Research Reproducibility Gaps
- **Symptom**: Reviewers cannot replicate studies because prompts were not archived.
- **Why**: Legacy TS methods logged only final translations.
- **Fix**: Adopt the Prompt Audit protocol outlined in `obsidian_workflow.md` and store prompt/output pairs in version control (with sensitive data removed).

```{tip}
Before opening an issue, capture:
1. Prompt + context packets
2. Model + version (API or local)
3. Temperature / decoding settings
4. Expected vs. actual behavior
5. Links to relevant notes (outline, glossary, etc.)
```
