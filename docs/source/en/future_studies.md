---
title: Future Studies — Research Agenda for the AI Era
---

# Future Studies — Research Agenda

Based on `Future_studies.md`, this section proposes grant-ready designs.

## 1. Prompt Sensitivity Study (Quantitative)
- **Question**: Does explicit Skopos definition reduce semantic variance?
- **Design**: 50 ambiguous segments × 3 prompt levels (none / weak / strong). Generate 100 samples each at temperature 1.0.
- **Metric**: Embedding variance + proposed **Skopos Adherence Score (SAS)** rated by humans.

## 2. Cyborg Process Study (Qualitative)
- **Question**: How does Chain-of-Thought prompting alter revision strategies?
- **Design**: 10 translators, two conditions (post-edit vanilla MT vs. CoT-enhanced outputs). Capture TAP + screen recordings.
- **Outcome**: Edits, acceptance rate, perceived agency.

## 3. Alignment Ethics Study (Critical)
- **Question**: Do safety-aligned APIs censor necessary translations?
- **Design**: Compare closed vs. open models on high-risk corpora (legal, medical, historical). Record refusals and sanitizations.
- **Metric**: Censorship Index for each model.

## 4. New Metrics Cheat Sheet
| Metric | Definition | Measurement |
| --- | --- | --- |
| Hallucination Rate | Factual errors per 1k words | Human annotation |
| Prompt Sensitivity | Output shift under slight prompt change | Vector similarity |
| Cultural Erasure Score | How often CSIs become target-norm | Annotate culture-specific items |
| Explanation Quality | Validity of CoT reasoning | Boolean checks |

## 5. Summary
We moved from “Is AI as good as humans?” to “How do we wield probabilistic infrastructure with agency, ethics, and rigor?”
