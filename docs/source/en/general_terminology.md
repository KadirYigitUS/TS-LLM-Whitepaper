---
title: General Terminology — A Translator’s Guide to AI
---

# General Terminology — Translator-Facing Glossary

This glossary prioritizes conceptual intuition, echoing the `General_Terminology.md` vault note. Each entry couples maths with translator analogies.

## 1. Usage Notes
- Target reader: Translation Studies scholars.
- Style: Translator-first explanations, then math, then professional stakes.

## 2. Basic Units (The Atoms)
### Token
- **Definition**: Smallest unit an LLM reads (≈0.75 words).
- **Math**: $Input = [t_1, t_2, t_3, ...]$
- **TS Analogy**: "Apple" = 1 token; "Donaudampfschifffahrt" consumes many.
- **Why it matters**: Cost + bias—languages that require more tokens become expensive and error-prone.

### Vector (Embedding)
- **Definition**: Numeric representation of meaning.
- **Example**: `King = [0.2, 0.9, -0.4]`, `Queen = [0.2, 0.9, +0.6]`.
- **TS Analogy**: Semantic map; synonyms sit near each other.

### Context Window
- **Definition**: Max tokens a model considers simultaneously.
- **Analogy**: Translating a novel but forgetting Chapter 1 when you hit Chapter 2.

## 3. Training Concepts (The Education)
### Pre-training
- Reads terabytes of text to learn probabilities.
- Creates a knowledgeable yet unruly base model.

### Fine-tuning
- Specializes the base model on curated data (e.g., legal briefs).

### Alignment (RLHF)
- Reinforcement Learning from Human Feedback to favor helpful/safe behavior.
- TS equivalent: teaching a junior translator ethics and client protocol.

## 4. Operational Concepts (The Usage)
### Prompt Engineering
- Designing inputs that sculpt the probability distribution.
- = Translation Brief / Skopos statement.

### Temperature
- Controls randomness (0 = deterministic legal tone, 0.8 = creative marketing tone).

### Hallucination
- Fluent but false statements; requires human-in-the-loop QA.

### Chain-of-Thought (CoT)
- Step-by-step reasoning, mirroring Think-Aloud Protocols.

## 5. Visual Summary
See [Knowledge Graphs](knowledge_graphs.md#4-llm-processing-pipeline-simplified) for the pipeline diagram referenced in Obsidian.

## 6. Cross-References
- [Outline](index.md)
- [Visual Assets](knowledge_graphs.md)
- [References](references.md)
