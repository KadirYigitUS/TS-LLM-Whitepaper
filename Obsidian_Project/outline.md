> Tags: #Outline #LLM #TranslatorStudies #ResearchDesign

# Outline — Extended Foundational Models of LLMs for Translator Studies

## 0. Frontmatter and Usage Notes
- **Intended Audience**: Translation Studies (TS) scholars with expertise in qualitative theory but novice status in Computational Linguistics/NLP.
- **Skopos of this Document**: To serve as a rigorous, citation-backed bridge between the engineering history of Large Language Models (LLMs) and the theoretical frameworks of Translation Studies.
- **File Structure**: This outline corresponds to a series of modular Markdown files designed for Obsidian knowledge management.

## 1. Introduction
### 1.1 Motivation
- The rapid integration of Generative AI into translation workflows.
- The "Black Box" problem: Translators use tools they do not conceptually understand.
- The necessity of demystification: Moving from "AI as Magic" to "AI as Probability and Statistics."

### 1.2 Epistemic Gap Analysis (The Recipient Perspective)
- **The Gap**: Lack of familiarity with Statistical Linguistics, Vector Space Models, and Neural Network topology.
- **The Bridge**: Explaining these concepts using TS analogies (e.g., "Vector Space" as "Semantic Equivalence Fields").

## 2. Theoretical Foundations (Secondary Sources)
*Building the vocabulary required to understand the 9 Seminal Papers.*
### 2.1 From Rules to Statistics
- **Statistical Linguistics**: Markov Chains and n-grams (predicting the next word based on frequency).
- **Corpus Studies**: The shift from prescriptive grammar to descriptive usage (parallels in TS Descriptive Translation Studies).

### 2.2 Neural Foundations
- **Perceptrons & Neural Networks**: The biological metaphor vs. the mathematical reality (matrix multiplication).
- **Backpropagation**: How models "learn" (minimizing error/loss functions).
- **Embeddings**: Representing words as numbers (Word2Vec, GloVe) — *Concept*: "Meaning is position in space."

## 3. The Evolutionary Arc of LLMs (The 9 Seminal Papers)
*Primary Source Review: Detailed analysis of the breakthrough papers.*

### 3.1 Stage 1: The Architecture of Attention
- **Paper 1**: *Attention Is All You Need* (Vaswani et al., 2017).
    - **Core Concept**: Self-Attention mechanism.
    - **Significance**: Removing recurrence; parallel processing; the birth of the Transformer.

### 3.2 Stage 2: Understanding Context
- **Paper 2**: *BERT: Pre-training of Deep Bidirectional Transformers* (Devlin et al., 2018).
    - **Core Concept**: Bidirectionality & Masked Language Modeling.
    - **Significance**: Deep contextual understanding vs. simple prediction.

### 3.3 Stage 3: The Scaling Era
- **Paper 3**: *Language Models are Few-Shot Learners* (GPT-3) (Brown et al., 2020).
    - **Core Concept**: In-context learning & Emergence.
    - **Significance**: Scale alone creates capability; the end of task-specific fine-tuning?
- **Paper 4**: *Scaling Laws for Neural Language Models* (Kaplan et al., 2020).
    - **Core Concept**: Power laws of compute, data, and size.
    - **Significance**: The scientific predictability of AI performance.

### 3.4 Stage 4: Efficiency and Democratization
- **Paper 5**: *LLaMA: Open and Efficient Foundation Language Models* (Touvron et al., 2023).
    - **Core Concept**: Data-optimal training (Chinchilla laws applied).
    - **Significance**: High performance on consumer hardware; open research.

### 3.5 Stage 5: Reasoning and Logic
- **Paper 6**: *Chain-of-Thought Prompting Elicits Reasoning* (Wei et al., 2022).
    - **Core Concept**: Intermediate reasoning steps.
    - **Significance**: Unlocking latent logic; prompting as a cognitive scaffolding.

### 3.6 Stage 6: Alignment and Instruction
- **Paper 7**: *Training Language Models to Follow Instructions* (InstructGPT) (Ouyang et al., 2022).
    - **Core Concept**: RLHF (Reinforcement Learning from Human Feedback).
    - **Significance**: Aligning probability with human intent (Skopos alignment).
- **Paper 8**: *The Flan Collection* (Longpre et al., 2022).
    - **Core Concept**: Mass-scale instruction tuning.
    - **Significance**: Generalization across unseen tasks via instruction exposure.

### 3.7 Stage 7: Agency and Tools
- **Paper 9**: *Toolformer* (Schick et al., 2023).
    - **Core Concept**: API integration & self-supervised tool use.
    - **Significance**: Breaking the "frozen weights" limitation; LLMs as agents.

## 4. Critical Intersections: AI & Translation Theory (Tertiary Sources)
### 4.1 Prompt Engineering as Skopos Theory
- **Mapping**: The "System Instruction" as the *Translation Brief*.
- **Concept**: *Skopos* (Purpose) determines the *Translatum* (Output).
- **Deliverable**: `Prompt requirements in PROMPT-ENGINEERING...md`

### 4.2 Context Engineering
- **Problem**: LLMs have no "world," only "context windows."
- **Concept**: Operationalizing "Context" (Co-text, Situational, Cultural) into tokens.
- **Deliverable**: `Beyond_prompt_engineering: What is Context...md`

### 4.3 Empiricism & Critique
- **Critique**: The flaw of "average" translation in statistical models.
- **Methodology**: Moving TS research from "error analysis" to "process analysis" and "prompt auditing."
- **Deliverable**: `Criticize_Empiric_TranslationStudies...md`

## 5. Discussion
- Synthesizing the engineering trajectory with the translator's reality.
- The shift from "Translator as Dictionary User" to "Translator as Probabilistic Auditor."

## 6. Future Directions for TS Research
- **New Metrics**: Beyond BLEU/METEOR; measuring "Prompt Sensitivity" and "Hallucination Rate."
- **Experimental Designs**: Longitudinal studies of Translator+AI interaction.

## 7. Appendices & References
- **Glossary**: `General_Terminology.md`
- **References**: `References.md` (APA Style)


---
## Linked Notes Directory
| Note | Scope |
| --- | --- |
| [[Beyond_prompt_engineering_-_What_is_Context_and_Context_Engineering]] | Defines "context engineering" tactics for TS-aligned prompt design. |
| [[Combined_Primary_and_Secondary_Source_review]] | Narrative synthesis of the primary + secondary corpus. |
| [[Combined_Primary_and_Secondary_Source_review_table]] | Tabular snapshot of the combined source review (filters + status). |
| [[Conclusion]] | Summative arguments tying TS priorities to LLM research arcs. |
| [[Criticize_Empiric_TranslationStudies_and_current_use_of_LLMs_in_Translation_Studies_Literature]] | Critical reflection on empirical TS methods vs current LLM deployments. |
| [[Discussions]] | Extended discussion note used for panel summaries and peer feedback. |
| [[Future_studies]] | Roadmap of experimental designs and funding-ready study ideas. |
| [[General_Terminology]] | Glossary of translator-centered terminology and LLM jargon. |
| [[Prompt_requirements_in_Prompt-Engineering_-_Similarity_of_Skopos_Theorie_and_Prompting_Practice.md]] | Maps Skopos Theory constructs onto prompt-engineering briefs. |
| [[References]] | Master APA reference list aligned with the manuscript citation order. |
| [[Tertiary_Sources_review]] | Annotated tertiary literature review linking industry reports. |
| [[Tertiary_Sources_review_table]] | Tertiary review tracking sheet (status, lens, geography). |
| [[Visual_Assets]] | Instructions + embed inventory for the semantic network widgets. |

---
## Cross-References
- [[References]]
- [[General_Terminology]]
- [[Visual_Assets]]
