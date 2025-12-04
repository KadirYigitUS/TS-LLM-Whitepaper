---
title: Outline — Extended Foundational Models of LLMs for Translator Studies
---

# Outline — Extended Foundational Models of LLMs for Translator Studies

````{tab-set}
```{tab-item} English

You are reading the English version of this outline.

```
```{tab-item} Türkçe

:doc:`Türkçe özeti aç <tr/index>`

```
````

> Intended audience: Translation Studies (TS) scholars who are fluent in qualitative theory yet new to NLP/LLM engineering.

## 0. Frontmatter and Usage Notes
- **Skopos**: Bridge the engineering history of LLMs with translator-centered theory.
- **Vault linkage**: Mirrors the Obsidian structure so each section stays modular for future remixing.

## 1. Introduction
### 1.1 Motivation
- Translators confront generative AI every day but still describe it as a black box.
- Demystification replaces "AI as Magic" with "AI as probability, vectors, and statistics".

### 1.2 Epistemic Gap Analysis
- **Gap**: Minimal exposure to statistical linguistics, embeddings, or neural topologies.
- **Bridge**: Reframe those concepts using TS analogies (e.g., "vector spaces" become "semantic equivalence fields").

## 2. Theoretical Foundations (Secondary Sources)
The vocabulary required before the nine seminal papers.

### 2.1 From Rules to Statistics
- **Statistical Linguistics**: Markov chains and n-grams predict the next word.
- **TS Parallel**: Descriptive Translation Studies already values corpora over prescriptive rules.

### 2.2 Neural Foundations
- **Perceptrons & Neural Nets**: Biological metaphors vs. actual matrix multiplication.
- **Backpropagation**: Error minimization built into every translation pass.
- **Embeddings**: Meaning is a vector’s position, not a dictionary entry.

## 3. Evolutionary Arc of LLMs — The 9 Seminal Papers
Each stage is mapped to a TS-friendly analogy.

1. **Attention Is All You Need** (2017) — Birth of the Transformer via self-attention.
   DOI: [10.48550/arXiv.1706.03762](https://doi.org/10.48550/arXiv.1706.03762)
   Semantic Scholar: [Vaswani et al. 2017](https://www.semanticscholar.org/paper/204e3073870fae3d05bcbc2f6a8e263d9b72e776)
2. **BERT** (2018) — Bidirectional context with masked language modeling.
   DOI: [10.18653/v1/N19-1423](https://doi.org/10.18653/v1/N19-1423)
   Semantic Scholar: [Devlin et al. 2019](https://www.semanticscholar.org/paper/df2b0e26d0599ce3e70df8a9da02e51594e0e992)
3. **GPT-3** (2020) — Emergent capabilities through sheer scale.
   DOI: [10.48550/arXiv.2005.14165](https://doi.org/10.48550/arXiv.2005.14165)
   Semantic Scholar: [Brown et al. 2020](https://www.semanticscholar.org/paper/90abbc2cf38462b954ae1b772fac9532e2ccd8b0)
4. **Scaling Laws** (2020) — Power laws make progress predictable.
   DOI: [10.48550/arXiv.2001.08361](https://doi.org/10.48550/arXiv.2001.08361)
   Semantic Scholar: [Kaplan et al. 2020](https://www.semanticscholar.org/paper/e6c561d02500b2596a230b341a8eb8b921ca5bf2)
5. **LLaMA** (2023) — Data-optimal, open models for universities.
   DOI: [10.48550/arXiv.2302.13971](https://doi.org/10.48550/arXiv.2302.13971)
   Semantic Scholar: [Touvron et al. 2023](https://www.semanticscholar.org/paper/57e849d0de13ed5f91d086936296721d4ff75a75)
6. **Chain-of-Thought** (2022) — Prompting as cognitive scaffolding.
   DOI: [10.48550/arXiv.2201.11903](https://doi.org/10.48550/arXiv.2201.11903)
   Semantic Scholar: [Wei et al. 2022](https://www.semanticscholar.org/paper/1b6e810ce0afd0dd093f789d2b2742d047e316d5)
7. **InstructGPT** (2022) — RLHF aligns probability with intent (Skopos alignment).
   DOI: [10.48550/arXiv.2203.02155](https://doi.org/10.48550/arXiv.2203.02155)
   Semantic Scholar: [Ouyang et al. 2022](https://www.semanticscholar.org/paper/d766bffc357127e0dc86dd69561d5aeb520d6f4c)
8. **Flan Collection** (2022) — Massive instruction tuning for generalization.
   DOI: [10.48550/arXiv.2301.13688](https://doi.org/10.48550/arXiv.2301.13688)
   Semantic Scholar: [Longpre et al. 2023](https://www.semanticscholar.org/paper/f2b0017ddd77fa38760a18145e63553105a1a236)
9. **Toolformer** (2023) — LLMs as API-using agents.
   DOI: [10.48550/arXiv.2302.04761](https://doi.org/10.48550/arXiv.2302.04761)
   Semantic Scholar: [Schick et al. 2023](https://www.semanticscholar.org/paper/53d128ea815bcc0526856eb5a9c42cc977cb36a7)

## 4. Critical Intersections: AI & Translation Theory
- **Prompt Engineering as Skopos**: System instructions are translation briefs. See :doc:`Prompt Engineering note <en/getting_started>`.
- **Context Engineering**: Halliday’s Field/Tenor/Mode become explicit prompt slots.
- **Empiricism & Critique**: Shift from error counting to prompt/process auditing.

## 5. Discussion
Translators evolve from dictionary users to probabilistic auditors who can interrogate the model’s choices.

## 6. Future Directions
- **New Metrics**: Prompt sensitivity, hallucination rate, cultural erasure.
- **Study Designs**: Longitudinal translator+AI ethnographies.

## 7. Appendices & References
- **Glossary**: :doc:`General Terminology <en/general_terminology>`
- **Bibliography**: :doc:`References <en/references>`
- **Visual assets**: :doc:`Knowledge Graphs <en/knowledge_graphs>`

```{seealso}
Additional linked notes:
- :doc:`Beyond Prompt Engineering <en/obsidian_workflow>` — operationalizing Halliday.
- :doc:`Combined Source Review <en/build_pipeline>` — detailed reading notes for every seminal paper.
- :doc:`Discussions <en/discussions>` — synthesis for seminars and panels.
- :doc:`Future Studies <en/future_studies>` — grant-ready experimental ideas.
```
