---
title: Critiquing Empiric Translation Studies
---

# Critiquing Empiric TS & Current LLM Usage

## 1. Regression to the Mean
- LLMs minimize perplexity → prefer common phrases.
- Excellent translations are often outliers; prompts must force purpose-specific language.

## 2. Flawed Research Designs
- Many TS studies feed default prompts to public APIs, then count errors.
- This only measures zero-shot baselines and hides the prompt variable.
- **Requirement**: Publish exact prompts and decoding parameters for reproducibility.

## 3. Automated Metrics vs. Purpose
- BLEU rewards n-gram overlap, not Skopos adherence.
- MQM or functional human evaluation better represent TS priorities.

## 4. Data Voids & Cultural Erasure
- Internet corpora overweight hegemonic languages; low-resource concepts get hallucinated.
- Always annotate culture-specific items and monitor replacements.

## 5. Process-Oriented Research Agenda
1. **Prompt Audits**: Track which constraint eliminated which error.
2. **Cyborg Protocols**: Compare human-only vs. human+AI with agency + cognitive load metrics.
3. **Transparency**: Archive prompts, retrieved packets, and edits alongside outputs.

## 6. Key Sources
- Koehn (2010/2020) on loss functions + BLEU limitations.
- Kenny (2022) on MT literacy.
- Bowker (2023) on data voids.

```{seealso}
See [obsidian_workflow.md](obsidian_workflow.md) for context-engineering tactics that operationalize these critiques.
```
