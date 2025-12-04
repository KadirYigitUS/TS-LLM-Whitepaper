---
title: Extended Literature Review — From Probability to Agency
---

# Build Pipeline — Extended Literature Review

::::{tab-set}
:::{tab-item} English
Full English consolidation is shown here.
:::
:::{tab-item} Türkçe
:doc:`Türkçe özetini aç <tr/build_pipeline>`
:::
::::

This page consolidates the `Combined_Primary_and_Secondary_Source_review.md` and `Tertiary_Sources_review.md` notes so the entire TS-to-LLM argument can be read linearly.

## 1. Pre-History: Statistical Meaning
### 1.1 From Rules to Statistics (Jurafsky & Martin, 2024)
- Markov chains (n-grams) approximate next-word probabilities.
- In TS terms, early SMT behaved like a phrasebook—frequency over meaning.

### 1.2 Word Embeddings (Mikolov et al., 2013)
- Vectors capture relationships ("King" − "Man" + "Woman" = "Queen").
- Translation becomes navigation inside a semantic map, not table lookup.

## 2. The Nine Seminal Papers (Primary Sources)
1. **Attention Is All You Need** — Self-attention removes recurrence; long-distance dependencies stay intact.
2. **BERT** — Masked Language Modeling learns bidirectional context.
3. **GPT-3** — Scale alone creates few-shot translators.
4. **Scaling Laws** — Power laws make capability a function of compute, data, and parameters.
5. **LLaMA** — Smaller, open weights trained longer → democratized research.
6. **Chain-of-Thought Prompting** — Forcing reasoning steps mirrors Think-Aloud Protocols (TAPs).
7. **InstructGPT** — RLHF aligns probability mass with intent (Skopos alignment at training time).
8. **Flan Collection** — Instruction tuning with 1,800 tasks generalizes to unseen briefs.
9. **Toolformer** — Self-supervised API use; translators as orchestration designers.

## 3. Functionalist & Contextual Tertiary Sources
### 3.1 Skopos Theory (Reiss & Vermeer, 2013; Nord, 1997)
- Commission = System Prompt.
- Skopos = Goal statement in the instruction block.
- Loyalty = Safety/alignment overrides in prompts.

### 3.2 Hallidayan Context (Halliday, 1978)
- Field, Tenor, Mode become explicit prompt slots.
- Retrieval-Augmented Generation (RAG) injects the missing situational context into the token window. See `obsidian_workflow.md` for tactics.

### 3.3 Critical Empiricism (Kenny, 2022; Bowker, 2023; House, 2015)
- Machine Translation literacy is table stakes.
- Cultural erasure and data voids require human-in-the-loop auditing.
- Overt vs. Covert translation mirrors literal vs. stylistic prompts.

## 4. Synthesis Tables
```{list-table}
:header-rows: 1
* - Engineering Stage
  - TS Analogy
  - Evidence
* - Attention / Transformers
  - Handling separable verbs and long clauses
  - Vaswani et al. (2017)
* - Scaling Laws
  - Predictable fidelity once budget is known
  - Kaplan et al. (2020)
* - Instruction Tuning
  - Commission briefs encoded directly into training tasks
  - Longpre et al. (2023)
* - Toolformer
  - Translator uses external termbases, not memory
  - Schick et al. (2023)
```

## 5. Research Implications for TS Scholars
- Treat prompts + RAG packets as research artifacts that must be archived and cited.
- Replace BLEU with purpose-aware metrics (Skopos Adherence Score, Cultural Erasure Score).
- Study translator+AI workflows ("cyborg" ethnographies) instead of isolated outputs.

## 6. Quick Cross-References
- [General Terminology](general_terminology.md)
- [Discussions](discussions.md)
- [Future Studies](future_studies.md)
- [References](references.md)
