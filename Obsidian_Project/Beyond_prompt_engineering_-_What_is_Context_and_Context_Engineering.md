> Tags: #Context #Halliday #RegisterTheory #RAG #Methodology

This note translates Hallidayan context theory into concrete context-window engineering tactics so prompt designers can preserve TS nuance in LLM workflows.

![[Visual_Assets#3. Context Engineering: The Hallidayan Injection]]

# Beyond Prompt Engineering: What is Context and Context Engineering?

## 1. Why this matters to Translation Studies
In Translation Studies (TS), "Context" is everything. A word implies a culture, a history, and a situation.
In AI, "Context" is strictly **mathematical quantity**: The number of tokens (words) the model can "see" at one time before it forgets the beginning.
**Context Engineering** is the art of squeezing the infinite social complexity of a translation situation (Hallidayan Context) into the finite "Context Window" of the model.

## 2. The Two Definitions of Context

### 2.1 The Translator’s Context (Hallidayan)
**Source**: Halliday, M.A.K. (1978). *Language as Social Semiotic*.
For a human, context is the **Context of Situation**:
*   **Field**: What is happening? (e.g., A legal deposition).
*   **Tenor**: Who is taking part? (e.g., Judge to Witness - High Power Distance).
*   **Mode**: What is the channel? (e.g., Spoken, transcribed to text).

### 2.2 The Model’s Context (The Token Window)
For an LLM (like GPT-4 or LLaMA), context is the **Sliding Window of Attention**.
*   **Definition**: The specific sequence of input tokens ($x_1, x_2, ... x_n$) available for the Self-Attention mechanism to calculate weights.
*   **Limitation**: If the "Context Window" is 4,000 tokens (approx. 10 pages), and you feed it Page 11, it mathematically "forgets" Page 1. It has no "World Knowledge" outside its pre-training weights, only "Window Knowledge."

---

## 3. Context Engineering: The Translator’s New Role
Since the model has no social senses, the translator must **explicitly encode** the Hallidayan variables into the Prompt (The Window). We call this "Context Engineering."

### 3.1 Encoding Field (Domain)
*   **TS Goal**: Ensure correct terminology (e.g., "Operation" = Surgery, not Military).
*   **AI Technique**: **RAG (Retrieval Augmented Generation)**.
    *   *Concept*: Before the model translates, we search a glossary/database for relevant terms and "inject" them into the context window.
    *   *Prompt Pattern*:
        > "Context: You are translating a **Medical** text (Field).
        > Here is a glossary of terms found in the source text:
        > - 'Operation' -> 'Chirurgie'
        > - 'Discharge' -> 'Sortie de l'hôpital'"

### 3.2 Encoding Tenor (Relationship)
*   **TS Goal**: Capture the correct register (Politeness, Formality).
*   **AI Technique**: **Persona Adoption**.
    *   *Concept*: Setting the "System Message" to bias the probability distribution toward specific stylistic choices.
    *   *Prompt Pattern*:
        > "Context: The **Tenor** is Formal. The speaker is a subordinate addressing a superior.
        > Use 'Vouvoiement' (Vous) in French. Avoid contractions."

### 3.3 Encoding Mode (Channel)
*   **TS Goal**: Adapt to the medium (Subtitles require brevity; Literature requires flow).
*   **AI Technique**: **Format Constraints**.
    *   *Prompt Pattern*:
        > "Context: The **Mode** is Subtitling.
        > Constraint: No line shall exceed 42 characters.
        > Constraint: Use standard subtitle segmentation."

---

## 4. Operational Example: Resolving Polysemy

**The Problem Word**: "Ball" (Dance vs. Sphere).

**Scenario A: Zero Context (The Ambiguity)**
> **Prompt**: "Translate 'She went to the ball.'"
> **AI Output**: "Elle est allée à la balle." (Incorrect: Refers to a tennis ball).
> *Why?*: Without context, "ball" (sphere) is statistically more probable in the training data than "ball" (dance).

**Scenario B: Engineered Context (Hallidayan Injection)**
> **Prompt**:
> "Context (Field): 19th Century Romance Novel.
> Context (Tenor): Aristocratic High Society.
> Source: 'She went to the ball.'"
>
> **AI Output**: "Elle est allée au bal." (Correct).
> *Why?*: The tokens "Romance" and "Aristocratic" shifted the attention weights. The vector for "ball" moved closer to "dance" in the semantic space.

---

## 5. Advanced Context Engineering: In-Context Learning (Few-Shot)
**Source**: Brown et al. (2020) (Paper #3 in Review).

We can "simulate" cultural context by providing examples. This is the most powerful form of Context Engineering.

*   **The "Context" is the Examples**:
    > "Translate the following slang naturally (Tenor: Casual).
    > Examples:
    > 1. 'What's up?' -> 'Quoi de neuf ?'
    > 2. 'I'm beat.' -> 'Je suis crevé.'
    > 3. 'It's a piece of cake.' -> 'C'est du gâteau.'
    >
    > Source: 'Don't chicken out.'"

*   **Result**: The model sees the pattern (Idiomatic Equivalence) and generates:
    > "Target: 'Ne te dégonfle pas.'"

## 6. Summary: The Formula
Context Engineering is the process of:
$$ \text{Translation Output} = \text{Model}(\text{Source Text} + \text{Field} + \text{Tenor} + \text{Mode}) $$

If you leave out the variables, you get the "Average" of the internet. If you engineer the variables, you get a specialized translation.

## References
*   **Brown, T., et al.** (2020). Language Models are Few-Shot Learners. *NeurIPS*.
*   **Halliday, M. A. K.** (1978). *Language as Social Semiotic: The Social Interpretation of Language and Meaning*. Edward Arnold.
*   **House, J.** (2015). *Translation Quality Assessment: Past and Present*. Routledge.


---
## Cross-References
- [[outline]]
- [[References]]
- [[General_Terminology]]
- [[Visual_Assets]]
