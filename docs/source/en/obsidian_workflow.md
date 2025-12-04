---
title: Obsidian Workflow — Context Engineering & Methodology
---

# Obsidian Workflow

This page merges two core vault notes—`Beyond_prompt_engineering_-_What_is_Context_and_Context_Engineering.md` and `Criticize_Empiric_TranslationStudies_and_current_use_of_LLMs_in_Translation_Studies_Literature.md`—plus highlights from `Discussions.md`.

## 1. Context Means Two Different Things
### 1.1 Hallidayan Context of Situation
- **Field** (activity), **Tenor** (participants/roles), **Mode** (channel).
- Translators already capture these in briefs; now they must encode them as tokens.

### 1.2 Model Context Windows
- LLMs know only the tokens inside the window ($x_1 \dots x_n$); everything else is latent statistical memory.
- If the source exceeds the window, the model forgets earlier segments—necessitating RAG or summarization.

## 2. Context Engineering Playbook
1. **Encode Field** via retrieved glossaries or style guides pasted ahead of the source text.
2. **Encode Tenor** by defining persona, honorifics, and power distance.
3. **Encode Mode** with strict formatting rules (subtitle lengths, markdown schema, etc.).
4. **Few-shot prompts** become simulated cultural context (Brown et al., 2020).
5. **Formula**: $$Translation = Model(Source + Field + Tenor + Mode)$$

## 3. Critiquing Empiric TS Methodology
- LLMs are regression-to-the-mean engines: they minimize perplexity, not creativity.
- Papers that feed default prompts to ChatGPT and count errors are measuring zero-shot baselines, not instrumented workflows.
- BLEU/COMET ignore purpose; TS scholars must evaluate Skopos adherence, cultural fidelity, and process data (prompts, iterations, edits).

### 3.1 Data Voids & Cultural Erasure
- Internet-scale corpora overrepresent hegemonic languages; low-resource concepts get hallucinated.
- Always log prompts, retrieved packets, and human edits to audit where hallucinations enter.

### 3.2 Prompt Audits
- Capture which constraint removed a cultural error.
- Track prompt sensitivity (how much outputs change when the brief is tweaked).

## 4. Translator Agency in the Cyborg Loop
| Traditional Task | AI-Augmented Task | Supporting Theory |
| --- | --- | --- |
| Drafting | Prompt specification | Skopos (Vermeer, Nord) |
| Dictionary lookup | Retrieval-augmented grounding | Toolformer (Schick) |
| Contextualization | Context injection packets | Halliday |
| Revision | Audit + hallucination triage | Kenny (MT literacy) |
| Ethics | Alignment override | Nord’s loyalty vs. RLHF |

## 5. Implementation Notes for the Obsidian Vault
- `script/obsidian_cleanup.py` already removes YAML front matter, inline wikilinks, and stray `// continue` markers so the Markdown renders cleanly in Sphinx.
- Each vault note now lives under `docs/source/en/` with explicit headings so cross-references are stable.
- Use MyST `{include}` blocks sparingly; duplicating content keeps RTD search indexes accurate.

```{tip}
When exporting new Obsidian notes:
1. Run `python script/obsidian_cleanup.py --src Obsidian_Project --dest docs/source/en`.
2. Curate bilingual summaries under `docs/source/tr` (do not machine-translate blindly).
3. Add the new files to the appropriate toctree tab above.
```
