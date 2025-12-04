> Tags: #LiteratureReview #Bibliography #Skopos #Context #Critique

# Extended Tertiary Sources Review: The Theoretical Backbone

## 1. Functionalism and Skopos Theory
*The theoretical basis for Prompt Engineering and Instruction Tuning.*

### 1.1 Reiss, K., & Vermeer, H. J. (2013). *Towards a General Theory of Translational Action: Skopos Theory Explained* (C. Nord, Trans.).
*   **The Core Argument**: Translation is an intentional interaction. The "Skopos" (Purpose) of the target text is the dominant factor in all translation decisions, superseding the linguistic structure of the source text.
*   **Relevance to LLMs**: This is the fundamental theory of **Prompt Engineering**. An LLM has no inherent intent; it requires an external "Commission" (the Prompt) to define the function. Without a defined Skopos, the LLM falls back on the statistical average of its training data (which is rarely the desired function).
*   **Key Concept for AI**: The **Commission** (Brief). In AI terms, this is the "System Instruction" that conditions the probability distribution.

### 1.2 Nord, C. (1997). *Translating as a Purposeful Activity: Functionalist Approaches Explained*.
*   **The Core Argument**: Introduces the concept of **Loyalty** (distinct from fidelity). Loyalty is a moral responsibility to the partners in the transaction (Author, Client, Receiver). It prevents the "radical functionalism" where a translator might change a text so much it becomes deceptive.
*   **Relevance to LLMs**: Mirrors the **Alignment Problem** (Helpfulness vs. Truthfulness/Harmlessness). An AI that is purely "Helpful" (High Skopos) might lie to please the user. "Loyalty" is the ethical guardrail (like RLHF Safety training) that prevents the model from hallucinating or generating toxic content just to fulfill a request.

---

## 2. Linguistics and Context Engineering
*The theoretical basis for RAG (Retrieval Augmented Generation) and Context Windows.*

### 2.1 Halliday, M. A. K. (1978). *Language as Social Semiotic: The Social Interpretation of Language and Meaning*.
*   **The Core Argument**: Language does not exist in a vacuum. Meaning is determined by the **Context of Situation**, defined by three variables:
    *   **Field**: What is happening (Topic/Activity).
    *   **Tenor**: Who is participating (Role relationships/Power).
    *   **Mode**: Role of language (Channel/Medium).
*   **Relevance to LLMs**: Provides the architecture for **Context Engineering**. An LLM "Context Window" is empty until filled. The translator must explicitly "inject" Field, Tenor, and Mode into the prompt to constrain the vector space. If you don't define the Tenor, the AI guesses the average Tenor (usually bland/neutral).

### 2.2 House, J. (2015). *Translation Quality Assessment: Past and Present*.
*   **The Core Argument**: Distinguishes between **Overt Translation** (where the reader knows it is a translation) and **Covert Translation** (where the text functions as a second original).
*   **Relevance to LLMs**: Defines the **Style Transfer** task.
    *   *Overt*: "Translate accurately" (Literal/Gloss).
    *   *Covert*: "Rewrite this as if written by a native speaker" (Natural Language Generation).
    *   Scholars use this distinction to evaluate whether an LLM has successfully adapted to the target culture or merely transcoded words.

---

## 3. Critical Empiricism and Methodology
*The theoretical basis for critiquing AI evaluation metrics and bias.*

### 3.1 Kenny, D. (2022). *Machine Translation for Everyone: Empowering Users in the Age of Artificial Intelligence*.
*   **The Core Argument**: Advocates for **Machine Translation Literacy**. Users (and scholars) must understand the basic architecture (Neural Networks) to critique the output effectively. We cannot treat the engine as a "Magic Box."
*   **Relevance to LLMs**: Demands **Process-Oriented Research**. Instead of just counting errors in the final text, researchers must analyze the interaction: How did the prompt change the result? Did the user edit the output? The "Human-in-the-Loop" is the unit of analysis, not the machine alone.

### 3.2 Bowker, L. (2023). *De-mystifying Translation: Introducing Translation to Non-translators*.
*   **The Core Argument**: Highlight the **Data Void**. Technology is not neutral; it reflects the data it was fed. Low-resource languages and non-hegemonic cultures are underrepresented, leading to bias and erasure.
*   **Relevance to LLMs**: Critiques the **Universalist Claim** of models like GPT-4. Just because a model *can* output Swahili does not mean it understands Swahili cultural concepts; it often maps English concepts onto Swahili words (Anglo-centric bias).

### 3.3 Koehn, P. (2010/2020). *Statistical Machine Translation*.
*   **The Core Argument**: (Foundational Engineering Text). Explains the mathematics of **Loss Functions** and **BLEU Scores**.
*   **Relevance to LLMs**: Provides the "Enemy" for qualitative TS scholars. It explains *why* models prefer high-frequency phrases (to minimize mathematical loss) and *why* automatic metrics fail to capture the "Skopos." Understanding Koehn allows a TS scholar to argue against "Score-based" evaluation with mathematical authority.

---

## 4. Summary of Tertiary Implications
The bridge between TS and AI is built on these texts:
1.  **Reiss & Vermeer** teach us how to **Prompt** (Purpose).
2.  **Halliday** teaches us how to **Contextualize** (Situation).
3.  **Kenny & Bowker** teach us how to **Critique** (Literacy & Bias).

These theories transform the LLM from a threat into a controllable instrument within the translator's toolkit.


---
## Cross-References
- [[outline]]
- [[References]]
- [[General_Terminology]]
- [[Visual_Assets]]
