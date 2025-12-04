---
title: Prompt Engineering as Functional Translation — The Skopos Connection
---

# Prompt Engineering as Functional Translation

Prompt design is simply Skopos Theory encoded for neural networks. This page adapts the Obsidian note `Prompt_requirements_in_Prompt-Engineering_-_Similarity_of_Skopos_Theorie_and_Prompting_Practice.md` into MyST-compatible sections.

## 1. Relevance to Translation Studies
Functionalist scholars (Reiss, Vermeer, Nord) argued that **purpose drives method**. LLMs require the same clarity: without a defined Skopos, the model defaults to the statistical average of the internet.

## 2. Vermeer’s Skopos Rule → AI Conditioning
- **Skopos Rule**: The goal of the target text justifies the translation strategy.
- **LLM Equivalent**: Conditioning narrows the probability space. No context means the model predicts “average” prose.

```{list-table}
:header-rows: 1
* - Skopos terminology
  - LLM terminology
  - Function
* - Commission (Brief)
  - System / Instruction prompt
  - Constrains role, tone, deliverable
* - Skopos (Purpose)
  - Goal statement
  - Explains why the output exists
* - Source Text
  - User content / context
  - Material to transform
* - Translatum
  - Completion
  - Generated response
* - Adequacy
  - Alignment
  - Does it satisfy the client?
```

## 3. Prompt Templates as Translation Briefs
Bad prompt (no Skopos):
> “Translate this into English: *Il pleut des cordes.*” → “It is raining ropes.”

Skopos-driven prompt:
```
You are an expert literary translator. Translate for an American novel audience.
Prioritize functional equivalence and colloquial tone.
Source: "Il pleut des cordes."
Constraints: No footnotes. Prefer idioms.
```
Result: “It’s raining cats and dogs.”

## 4. Nord’s Loyalty ↔ AI Alignment
- **Nord**: Translators owe loyalty to author, client, and reader.
- **AI Alignment**: RLHF optimizes for helpfulness/harmlessness. Conflicts arise when legal or historical work requires unfiltered accuracy.
- **Engineering tactic**: Encode loyalty explicitly (e.g., “Accuracy supersedes euphemism; mark ambiguous terms with `[AMBIG]`." )

## 5. The Skopos Prompting Triangle
Refer to the Mermaid diagram in [Visual Assets](knowledge_graphs.md#knowledge-graphs--visual-assets) to see how user, prompt, and model form an alignment loop.

## 6. Checklist for Translator-Prompt Designers
1. **Define the role** (persona, domain expertise, register authority).
2. **Declare the Skopos** (persuasion, legal accuracy, pedagogy, archival fidelity).
3. **Describe the addressee** (audience, cultural background, reading environment).
4. **Constrain format** (length, subtitling rules, markup).
5. **Encode loyalty** (cite ambiguities, refuse hallucinations, mark safety overrides).

Each translation brief you send to a model should read like a Skopos commission—otherwise you are auditing the machine’s defaults instead of directing them.
