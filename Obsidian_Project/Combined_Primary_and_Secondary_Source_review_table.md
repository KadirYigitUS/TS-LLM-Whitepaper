> Tags: #LiteratureReview #LLM #History #Methodology #Tables


![[Visual_Assets#1. The Evolutionary Arc of LLMs]]

# Combined Primary and Secondary Source Review: The LLM Evolutionary Arc

## 1. Usage Notes
This table serves as a "Cheat Sheet" for the subsequent detailed literature review. It maps the engineering milestones (Primary Sources) and the necessary background theories (Secondary Sources) to concepts familiar in Translation Studies (TS).

**Legend:**
- **Primary Source**: The 9 seminal papers explicitly requested.
- **Secondary Source**: Foundational texts (textbooks, earlier papers) required to understand the gap before the breakthrough.
- **TS Analogy**: A metaphor connecting the computational mechanism to human translation processes.

## 2. The Master Table

| Evolutionary Stage | Source Type | Citation (Author, Year) | Technical Concept / Breakthrough | Translation Studies (TS) Analogy | Why it is Fundamental |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **0. Pre-Neural / Foundations** | *Secondary* | Jurafsky & Martin (2024) *Speech and Language Processing* | **N-grams & Statistical Logic**:<br>Predicting the next word based on fixed frequency history (Markov Chains). | **The "Phrasebook" Approach**:<br>Translating based on how often words appear together, without understanding grammar or meaning. | Establishes language as a probabilistic system (Stochastic process), not just a rule-based system. |
| **0. Pre-Neural / Foundations** | *Secondary* | Mikolov et al. (2013) *Word2Vec* | **Vector Embeddings**:<br>Representing words as coordinates in a multi-dimensional numeric space. | **The "Semantic Map"**:<br>Words with similar meanings ("King", "Queen") are mathematically close to each other, like synonyms in a thesaurus cloud. | Proved that computers can capture "meaning" through geometric proximity. |
| **1. The Architecture of Attention** | **Primary #1** | Vaswani et al. (2017) | **The Transformer (Self-Attention)**:<br>Processing the entire sequence at once; weighting relevance of every word to every other word. | **Cognitive Focus**:<br>A translator keeping their eye on the subject ("The cat") while determining the gender of the adjective ("black") at the end of the sentence. | Eliminated the need for sequential processing (RNNs), allowing massive parallelization and speed. |
| **2. Contextual Understanding** | **Primary #2** | Devlin et al. (2018) *(BERT)* | **Bidirectionality & Masking**:<br>Learning context from both left and right of a word simultaneously (Cloze test). | **Reading Ahead**:<br>A translator reading the *entire* source sentence to understand context before translating the first word. | Moved beyond simple "next word prediction" to deep contextual understanding. |
| **3. The Era of Scale** | **Primary #3** | Brown et al. (2020) *(GPT-3)* | **Few-Shot Learning / In-Context Learning**:<br>Model adapts to tasks without weight updates, given just a few examples in the prompt. | **The Polymath Student**:<br>A student who doesn't know the subject but can solve the test just by looking at 3 example questions. | Demonstrated that "intelligence" and versatility emerge strictly from model size and data volume. |
| **3. The Era of Scale** | **Primary #4** | Kaplan et al. (2020) | **Scaling Laws**:<br>Performance improves via a precise power-law relationship with Compute, Data, and Parameters. | **Industrial Forecasting**:<br>Knowing exactly how much "better" a translation engine will get if you double the budget and corpus size. | Turned AI progress from alchemy/guesswork into a predictable science. |
| **4. Efficiency & Open Science** | **Primary #5** | Touvron et al. (2023) *(LLaMA)* | **Compute-Optimal Training**:<br>Training smaller models on *more* data yields better results than just making giant models. | **The Specialized Glossary**:<br>A smaller, highly trained brain (or corpus) is more efficient than a giant, confused generalist. | Democratized LLMs; proved open models could rival proprietary giants (OpenAI/Google). |
| **5. Reasoning & Logic** | **Primary #6** | Wei et al. (2022) | **Chain-of-Thought (CoT)**:<br>Prompting the model to generate intermediate reasoning steps before the answer. | **Think-Aloud Protocol (TAPs)**:<br>Asking a translator to verbalize their decision-making process ("I chose X because Y...") to ensure accuracy. | Unlocked complex reasoning (Math/Logic) that simple pattern matching couldn't handle. |
| **6. Alignment & Instruction** | **Primary #7** | Ouyang et al. (2022) *(InstructGPT)* | **RLHF (Reinforcement Learning from Human Feedback)**:<br>Fine-tuning the model based on human preference rankings. | **The Translation Brief (Skopos)**:<br>Aligning the translator's output not just with grammar, but with what the *client* actually wants/prefers. | Solved the "alignment problem"—making models helpful and safe, not just accurate predictors. |
| **6. Alignment & Instruction** | **Primary #8** | Longpre et al. (2022) *(Flan)* | **Instruction Tuning**:<br>Fine-tuning on thousands of diverse tasks phrasing as instructions. | **Translator Training Curriculum**:<br>Exposing a student to 1,000 different types of translation tasks so they can handle *any* new request. | Enabled models to generalize to unseen tasks (Zero-shot) effectively. |
| **7. Agency & Tools** | **Primary #9** | Schick et al. (2023) *(Toolformer)* | **Tool Use / API Integration**:<br>Self-taught ability to call external calculators, search engines, or wikis. | **The Resourceful Translator**:<br>Recognizing when you don't know a fact, pausing, consulting a dictionary/Google, and pasting the result. | Broke the "hallucination" loop by allowing access to external, verifiable ground truth. |

## 3. Data Download
*Note for implementation: Due to current environment restrictions, a direct CSV file creation is simulated below. Copy the block below to save as `llm_source_review.csv`.*

```csv
Stage,Source,Citation,Concept,Analogy,Significance
Pre-Neural,Secondary,"Jurafsky & Martin (2024)",N-grams,Phrasebook,Probabilistic foundation
Pre-Neural,Secondary,"Mikolov et al. (2013)",Word Embeddings,Semantic Map,Geometric meaning
Architecture,Primary,"Vaswani et al. (2017)",Transformer/Attention,Cognitive Focus,Parallelization
Context,Primary,"Devlin et al. (2018)",BERT/Bidirectional,Reading Ahead,Deep Context
Scale,Primary,"Brown et al. (2020)",GPT-3/Few-Shot,Polymath Student,Emergence
Scale,Primary,"Kaplan et al. (2020)",Scaling Laws,Forecasting,Predictability
Efficiency,Primary,"Touvron et al. (2023)",LLaMA/Optimal Data,Specialized Glossary,Democratization
Reasoning,Primary,"Wei et al. (2022)",Chain-of-Thought,Think-Aloud Protocol,Logic unlocking
Alignment,Primary,"Ouyang et al. (2022)",RLHF/InstructGPT,Skopos/Brief,Human preference
Alignment,Primary,"Longpre et al. (2022)",Flan/Instruction Tuning,Training Curriculum,Generalization
Agency,Primary,"Schick et al. (2023)",Toolformer,Resourceful Translator,External truth
```

## References (Short Form)
*Full citations available in References.md*

- Brown, T. et al. (2020). *Language Models are Few-Shot Learners*.
- Devlin, J. et al. (2018). *BERT: Pre-training of Deep Bidirectional Transformers*.
- Jurafsky, D., & Martin, J. H. (2024). *Speech and Language Processing*.
- Kaplan, J. et al. (2020). *Scaling Laws for Neural Language Models*.
- Longpre, S. et al. (2022). *The Flan Collection*.
- Mikolov, T. et al. (2013). *Distributed Representations of Words and Phrases*.
- Ouyang, L. et al. (2022). *Training Language Models to Follow Instructions*.
- Schick, T. et al. (2023). *Toolformer: Language Models Can Teach Themselves to Use Tools*.
- Touvron, H. et al. (2023). *LLaMA: Open and Efficient Foundation Language Models*.
- Vaswani, A. et al. (2017). *Attention Is All You Need*.
- Wei, J. et al. (2022). *Chain-of-Thought Prompting Elicits Reasoning*.

```
```


---
## Cross-References
- [[outline]]
- [[References]]
- [[General_Terminology]]
- [[Visual_Assets]]
