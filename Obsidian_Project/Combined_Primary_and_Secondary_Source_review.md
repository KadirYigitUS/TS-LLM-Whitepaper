> Tags: #LiteratureReview #Methodology #LLM #History


![[Visual_Assets#1. The Evolutionary Arc of LLMs]]

# Extended Literature Review: From Probability to Agency

## 1. The Pre-History: Foundations of Statistical Meaning (Secondary Sources)
*Before understanding Transformers, we must understand how computers "read" text. They do not see words; they see numbers (vectors) and probabilities.*

### 1.1 From Rules to Statistics: The N-Gram
**Source**: Jurafsky, D., & Martin, J. H. (2024). *Speech and Language Processing* (3rd ed. draft).
*   **Concept**: **The Markov Assumption**. The probability of the next word depends only on the previous $n$ words.
*   **TS Analogy**: Ideally, translation is about meaning. But purely statistical machine translation (SMT) was like a translator using a phrasebook: "If I see 'Pomme', the next word is likely 'Rouge' 30% of the time." It didn't "know" what an apple was; it just counted frequencies.
*   **Why it matters**: This established that language could be modeled mathematically as a sequence of probabilities, paving the way for neural models.

### 1.2 Meaning as Geometry: Word Embeddings
**Source**: Mikolov, T., et al. (2013). *Distributed Representations of Words and Phrases and their Compositionality*.
*   **Concept**: **Vector Space Models**. Words are mapped to vectors (lists of numbers) in a high-dimensional space.
*   **The Breakthrough**: "King - Man + Woman = Queen." The model learned that the geometric distance between "King" and "Queen" was the same as between "Man" and "Woman."
*   **TS Analogy**: Imagine a "Meaning Map." Synonyms are neighbors. Antonyms are far apart. The computer translates by finding the coordinates of a word in English and finding the word at the closest coordinates in French.
*   **API citation**: Mikolov et al., "Distributed Representations..." — pages 1–9.
*   **DOI**: 10.48550/arXiv.1310.4546

---

## 2. The Seminal 9: The Arc of LLM Evolution

### Paper 1: Attention Is All You Need (2017)
**Authors**: Vaswani, A., et al. (Google Brain)

*   **LLM Stage**: The Architecture of Attention.
*   **Breakthrough**: The **Transformer** architecture.
*   **Core Concept**: **Self-Attention**. Replacing Recurrent Neural Networks (RNNs) with a mechanism that processes all words in parallel.

**The Translation Studies Context**:
In previous Neural Machine Translation (NMT), models read a sentence like a human reads a ticker-tape: one word at a time, left-to-right (RNNs). By the time the model reached the end of a long sentence, it often "forgot" the beginning. This is the **Vanishing Gradient Problem**.
Vaswani et al. proposed: Don't read sequentially. Look at the whole sentence at once.

**Detailed Causal Review**:
The authors introduced "Self-Attention," a mathematical way for every word in a sentence to "vote" on how relevant every other word is to it.
*   *Example*: In "The **animal** didn't cross the **street** because **it** was too tired," the word "**it**" has a strong attention weight connecting it to "**animal**."
*   *Mechanism*: Using Query, Key, and Value matrices (Q, K, V), the model calculates a weighted sum of the input vectors. This allows the model to handle long-distance dependencies (e.g., German separable verbs at the end of a sentence) instantly.

**Summary**:
The paper "Attention Is All You Need" revolutionized Natural Language Processing by discarding recurrence and convolution in favor of an attention-based mechanism. The Transformer architecture allows for significantly more parallelization, reducing training time while improving performance on translation tasks (WMT 2014 English-to-German).
By enabling the model to attend to different parts of the input sequence simultaneously, the Transformer captures complex linguistic relationships regardless of their distance in the text. This architecture became the foundation for all subsequent LLMs (BERT, GPT, etc.).

**API citation**: Vaswani et al., "Attention Is All You Need" — pages 1–11.
**DOI**: 10.48550/arXiv.1706.03762

---

### Paper 2: BERT: Pre-training of Deep Bidirectional Transformers (2018)
**Authors**: Devlin, J., et al. (Google AI)

*   **LLM Stage**: Contextual Understanding.
*   **Breakthrough**: **Bidirectional** training.
*   **Core Concept**: **Masked Language Modeling (MLM)**.

**The Translation Studies Context**:
Standard models read left-to-right. But to translate "bank" in "The bank of the river," you need to see "river" (which appears *after* "bank"). BERT (Bidirectional Encoder Representations from Transformers) reads the text in both directions simultaneously.

**Detailed Causal Review**:
*   *Method*: Instead of predicting the next word, BERT hides 15% of the words in a sentence (replacing them with `[MASK]`) and tries to guess them based on the surrounding context.
*   *Impact*: This forced the model to learn deep contextual relations rather than just shallow surface patterns. It created "Contextual Embeddings"—the vector for "bank" changes depending on whether it's near "money" or "river."

**Summary**:
Devlin et al. introduced BERT, a model designed to pre-train deep bidirectional representations from unlabeled text. Unlike previous models that were unidirectional (left-to-right), BERT uses a Masked Language Model (MLM) objective to fuse context from both left and right contexts in all layers.
This approach achieved state-of-the-art results on eleven NLP tasks, including Question Answering and Inference. It marked a shift in the field toward "Pre-training + Fine-tuning," where a single massive model could be adapted for specific tasks with minimal additional training.

**API citation**: Devlin et al., "BERT: Pre-training..." — pages 4171–4186.
**DOI**: 10.48550/arXiv.1810.04805

---

### Paper 3: Language Models are Few-Shot Learners (GPT-3) (2020)
**Authors**: Brown, T., et al. (OpenAI)

*   **LLM Stage**: The Era of Scale.
*   **Breakthrough**: **Emergent Capabilities** via scaling.
*   **Core Concept**: **In-Context Learning** (Few-Shot).

**The Translation Studies Context**:
Before GPT-3, if you wanted a translation machine, you trained it specifically on translation data (Fine-tuning). GPT-3 showed that if you make the model big enough (175 Billion parameters) and train it on "The Internet," it learns to translate *incidentally*, without specific training. You just ask it.

**Detailed Causal Review**:
*   *Mechanism*: The model is an Autoregressive (predict next word) Transformer. It is not bidirectional like BERT.
*   *Discovery*: At scale, the model develops "In-Context Learning." If you prompt it with: "English: Hello, French: Bonjour. English: Cat, French: Chat. English: Dog, French:__", it completes the pattern. It "learns" the task from the prompt itself.

**Summary**:
Brown et al. presented GPT-3, a 175-billion parameter language model, demonstrating that scaling up model size results in strong performance on many NLP tasks without any gradient updates (fine-tuning). The model utilizes "few-shot learning," where it is given a natural language description of the task and a few examples in the prompt.
The paper provided evidence that massive autoregressive language models develop broad, generalized capabilities—such as translation, question answering, and arithmetic—simply by learning to predict the next word in a massive corpus. This challenged the paradigm that specialized training data is required for specialized tasks.

**API citation**: Brown et al., "Language Models are Few-Shot Learners" — pages 1–75.
**DOI**: 10.48550/arXiv.2005.14165

---

### Paper 4: Scaling Laws for Neural Language Models (2020)
**Authors**: Kaplan, J., et al. (OpenAI)

*   **LLM Stage**: The Era of Scale (The Science).
*   **Breakthrough**: **Predictability** of performance.
*   **Core Concept**: **Power Laws**.

**The Translation Studies Context**:
Is building a better translator art or science? Kaplan showed it is Physics. There is a precise mathematical relationship between how much compute (money/electricity) you burn and how smart the model gets.

**Detailed Causal Review**:
*   *The Law*: $L(N) \approx (N_c/N)^\alpha$. Loss ($L$) decreases as a power law of Model Size ($N$), Dataset Size ($D$), and Compute ($C$).
*   *Implication*: Bigger is strictly better. The model does not "plateau"; it keeps improving. This justified the multi-million dollar investments in GPU clusters that followed.

**Summary**:
Kaplan et al. systematically investigated the empirical scaling laws for language model performance. They found that cross-entropy loss scales as a power law with respect to model size, dataset size, and the amount of compute used for training, spanning over seven orders of magnitude.
The authors concluded that larger models are significantly more sample-efficient, meaning it is more optimal to train very large models on fewer tokens than to train smaller models to convergence. This insight directly guided the development of massive models like GPT-3 and PaLM.

**API citation**: Kaplan et al., "Scaling Laws..." — pages 1–18.
**DOI**: 10.48550/arXiv.2001.08361

---

### Paper 5: LLaMA: Open and Efficient Foundation Language Models (2023)
**Authors**: Touvron, H., et al. (Meta AI)

*   **LLM Stage**: Efficiency & Democratization.
*   **Breakthrough**: **High-performance Open Models**.
*   **Core Concept**: **Chinchilla Optimality** (Data-centric scaling).

**The Translation Studies Context**:
GPT-3 was closed-source. LLaMA (Large Language Model Meta AI) proved you don't need 175B parameters. A smaller model (13B or 65B parameters) trained on *more words* (Trillions of tokens) can outperform the giant GPT-3.
*Analogy*: A compact, highly-read encyclopedia is better than a massive library filled with blank pages.

**Detailed Causal Review**:
*   *Correction to Scaling*: Building on DeepMind's "Chinchilla" paper, LLaMA showed that most models were under-trained.
*   *Impact*: By releasing the weights, Meta allowed academic researchers (including TS scholars) to run powerful models on their own universities' computers, breaking the dependency on paid APIs.

**Summary**:
Touvron et al. introduced LLaMA, a collection of foundation language models ranging from 7B to 65B parameters. By training on trillions of tokens of publicly available data, they demonstrated that smaller models trained longer (on more data) can outperform significantly larger models like GPT-3 (175B).
The release of LLaMA democratized access to LLM research, allowing the academic community to study these models' behaviors, biases, and fine-tuning capabilities on consumer-grade hardware, sparking a wave of open-source innovation.

**API citation**: Touvron et al., "LLaMA: Open and Efficient..." — pages 1–26.
**DOI**: 10.48550/arXiv.2302.13971

---

### Paper 6: Chain-of-Thought Prompting Elicits Reasoning (2022)
**Authors**: Wei, J., et al. (Google Research)

*   **LLM Stage**: Reasoning & Logic.
*   **Breakthrough**: **Multi-step Reasoning**.
*   **Core Concept**: **Chain-of-Thought (CoT)**.

**The Translation Studies Context**:
Translators often use "Think-Aloud Protocols" (TAPs) to verify their work ("I am translating this as X because the context implies Y..."). Standard LLMs just guess the answer. Wei et al. showed that if you force the LLM to write out its TAP, it becomes much smarter.

**Detailed Causal Review**:
*   *Technique*: Instead of prompting `Q: 2+2? A:`, you prompt `Q: 2+2? A: I have 2. I add 2 more. The total is 4. Answer: 4.`
*   *Result*: This "intermediate compute" allows the model to handle logic, math, and complex translation nuances that require multiple inferential steps.

**Summary**:
Wei et al. explored how generating a chain of thought—a series of intermediate reasoning steps—significantly improves the ability of large language models to perform complex reasoning. They showed that this ability emerges naturally in sufficiently large models (typically 100B+ parameters).
On benchmarks like the GSM8K (math word problems), Chain-of-Thought prompting enabled models to outperform fine-tuned state-of-the-art systems without any modification to the model weights. It demonstrated that "prompt engineering" could unlock latent cognitive capabilities.

**API citation**: Wei et al., "Chain-of-Thought Prompting..." — pages 1–35.
**DOI**: 10.48550/arXiv.2201.11903

---

### Paper 7: Training Language Models to Follow Instructions (InstructGPT) (2022)
**Authors**: Ouyang, L., et al. (OpenAI)

*   **LLM Stage**: Alignment.
*   **Breakthrough**: **RLHF** (Reinforcement Learning from Human Feedback).
*   **Core Concept**: **Alignment** with Human Intent.

**The Translation Studies Context**:
A raw LLM is like a wildly creative but undisciplined surrealist poet. It might continue a translation request by writing a fictional story about a translator. To make it a *tool*, we must align its "Skopos" (Purpose) with the user's intent.
*Analogy*: The "Translation Brief." We are giving the model a permanent brief: "Be helpful, harmless, and honest."

**Detailed Causal Review**:
*   *Step 1*: Humans write good answers (Supervised Fine-Tuning).
*   *Step 2*: Humans rank model outputs (Reward Model).
*   *Step 3*: Reinforcement Learning (PPO) optimizes the model to get high rankings.
*   *Result*: A 1.3B parameter InstructGPT model was preferred by humans over the 175B GPT-3. Alignment > Size.

**Summary**:
Ouyang et al. introduced InstructGPT, a model fine-tuned using Reinforcement Learning from Human Feedback (RLHF) to align with user intent. While large language models are capable, they often produce untruthful, toxic, or unhelpful outputs.
The authors showed that by collecting a dataset of human comparisons between model outputs and training a reward model, they could fine-tune GPT-3 to minimize toxicity and "hallucination" while maximizing helpfulness. This paper laid the technical groundwork for ChatGPT.

**API citation**: Ouyang et al., "Training Language Models..." — pages 1–68.
**DOI**: 10.48550/arXiv.2203.02155

---

### Paper 8: The Flan Collection (2022)
**Authors**: Longpre, S., et al. (Google Research)

*   **LLM Stage**: Alignment & Generalization.
*   **Breakthrough**: **Massive Multi-task Instruction Tuning**.
*   **Core Concept**: **Task Generalization**.

**The Translation Studies Context**:
How do you train a "Universal Translator"? By exposing the student to every possible type of text (legal, medical, poetic, code). Flan (Fine-tuned LAnguage Net) showed that if you fine-tune on 1,800 different tasks, the model generalizes to *new* tasks it has never seen.

**Detailed Causal Review**:
*   *Method*: Converting standard NLP datasets (classification, translation, logic) into "Instruction Format" (`"Please translate this..."`).
*   *Finding*: Instruction tuning improves performance on held-out tasks. It teaches the model the *concept* of following instructions.

**Summary**:
Longpre et al. released the Flan Collection, a massive compilation of datasets and methods for instruction tuning. By fine-tuning language models on over 1,800 diverse tasks phrased as instructions, they achieved significant improvements in zero-shot and few-shot performance across unseen tasks.
The paper demonstrated that the diversity of the training tasks is crucial for generalization. Models fine-tuned on this collection (like Flan-T5 and Flan-PaLM) outperformed their non-instruction-tuned counterparts, proving that "how you teach" is as important as "what you teach."

**API citation**: Longpre et al., "The Flan Collection..." — pages 1–18.
**DOI**: 10.48550/arXiv.2301.13688

---

### Paper 9: Toolformer: Language Models Can Teach Themselves to Use Tools (2023)
**Authors**: Schick, T., et al. (Meta AI)

*   **LLM Stage**: Agency.
*   **Breakthrough**: **Self-Supervised Tool Use**.
*   **Core Concept**: **API Integration**.

**The Translation Studies Context**:
Translators don't memorize dictionaries; they *use* them. LLMs hallucinate facts because they rely on internal memory. Toolformer taught LLMs to recognize their own ignorance and call an external API (Calculator, Wikipedia, Translator).

**Detailed Causal Review**:
*   *Method*: The model teaches itself where to insert API calls (e.g., `[Wiki(Query)]`) by trying them and seeing if the API result lowers the perplexity (error) of the next word prediction.
*   *Significance*: This transforms the LLM from a static text generator into a central controller for external software.

**Summary**:
Schick et al. introduced Toolformer, a model trained to decide which external tools to use, when to use them, and how to incorporate their results. Using a self-supervised process, the model learns to generate API calls for a calculator, a QA system, a search engine, and a translation system.
This approach significantly improved zero-shot performance on tasks requiring factual knowledge or arithmetic, which are traditional weaknesses of LLMs. It represents a paradigm shift toward "Augmented Language Models" that can interact with the world.

**API citation**: Schick et al., "Toolformer..." — pages 1–14.
**DOI**: 10.48550/arXiv.2302.04761

---

## 3. References for Further Reading (Short List)

1.  **Vaswani, A., et al.** (2017). Attention Is All You Need. *Advances in Neural Information Processing Systems*. DOI: 10.48550/arXiv.1706.03762
2.  **Devlin, J., et al.** (2018). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. *NAACL*. DOI: 10.48550/arXiv.1810.04805
3.  **Brown, T., et al.** (2020). Language Models are Few-Shot Learners. *NeurIPS*. DOI: 10.48550/arXiv.2005.14165
4.  **Kaplan, J., et al.** (2020). Scaling Laws for Neural Language Models. *arXiv*. DOI: 10.48550/arXiv.2001.08361
5.  **Wei, J., et al.** (2022). Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. *NeurIPS*. DOI: 10.48550/arXiv.2201.11903
6.  **Ouyang, L., et al.** (2022). Training Language Models to Follow Instructions with Human Feedback. *NeurIPS*. DOI: 10.48550/arXiv.2203.02155
7.  **Longpre, S., et al.** (2022). The Flan Collection: Designing Data and Methods for Effective Instruction Tuning. *arXiv*. DOI: 10.48550/arXiv.2301.13688
8.  **Touvron, H., et al.** (2023). LLaMA: Open and Efficient Foundation Language Models. *arXiv*. DOI: 10.48550/arXiv.2302.13971
9.  **Schick, T., et al.** (2023). Toolformer: Language Models Can Teach Themselves to Use Tools. *arXiv*. DOI: 10.48550/arXiv.2302.04761


---
## Cross-References
- [[outline]]
- [[References]]
- [[General_Terminology]]
- [[Visual_Assets]]
