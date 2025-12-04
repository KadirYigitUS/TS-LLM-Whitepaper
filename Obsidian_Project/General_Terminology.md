> Tags: #Glossary #Terminology #Pedagogy #AI_Literacy

This translator-facing glossary explains every recurring AI term using Translation Studies analogies before diving into the granular definitions below.

![[Visual_Assets#4. The LLM Processing Pipeline (Simplified)]]

# General Terminology: A Translator’s Guide to AI

## 1. Usage Notes
This glossary is designed for Translation Studies scholars. It prioritizes **conceptual intuition** over engineering precision. Each term includes a "Why it matters" section to connect the math to the translation profession.

---

## 2. Basic Units (The Atoms)

### **Token**
*   **Definition**: The fundamental unit of text for an LLM. It is roughly 0.75 of a word (e.g., "Translating" might be two tokens: `Trans` + `lating`).
*   **Math Intuition**: $Input = [t_1, t_2, t_3, ...]$
*   **Translation Example**: The English word "Apple" is 1 token. The complex German word "Donaudampfschifffahrt" is many tokens.
*   **Why it matters**: You pay for API usage by the token. Also, LLMs struggle with languages that require many tokens to express simple concepts (Tokenization Bias).

### **Vector (Embedding)**
*   **Definition**: A list of numbers representing the *meaning* of a token.
*   **Math Intuition**: `King` = `[0.2, 0.9, -0.4]`. `Queen` = `[0.2, 0.9, +0.6]`.
*   **Translation Example**: Think of a "Semantic Map." Words with similar meanings are located close to each other on the map.
*   **Why it matters**: This is how the computer "understands" synonyms. It calculates distance on the map.

### **Context Window**
*   **Definition**: The maximum amount of text the model can consider at one time (e.g., 4,000 to 128,000 tokens).
*   **Translation Example**: Imagine translating a novel, but you immediately forget Chapter 1 as soon as you start Chapter 2.
*   **Why it matters**: If your source text exceeds the window, the model loses coherence. You must use RAG or summarization strategies.

---

## 3. Training Concepts (The Education)

### **Pre-training**
*   **Definition**: The initial, massive training phase where the model learns to predict the next word from terabytes of internet text.
*   **Translation Example**: A student reading the entire library to learn grammar and facts, but not learning *how* to take an exam.
*   **Why it matters**: This creates the "Base Model" (knowledgeable but unruly).

### **Fine-tuning**
*   **Definition**: Training the Base Model on a smaller, specific dataset to specialize it.
*   **Translation Example**: Sending that student to a specialized Medical Translation course.
*   **Why it matters**: You cannot teach a base model new facts easily, but you can Fine-tune it to learn a specific *style* or terminology.

### **Alignment (RLHF)**
*   **Definition**: Reinforcement Learning from Human Feedback. Tweaking the model to prefer "helpful" and "safe" answers.
*   **Translation Example**: Teaching a student *ethics* and *client protocol* (e.g., "Don't translate hate speech literally; add a note").
*   **Why it matters**: Commercial models (ChatGPT) are heavily aligned, which can sometimes result in "Censorship" or "Over-sanitization" of sensitive source texts.

---

## 4. Operational Concepts (The Usage)

### **Prompt Engineering**
*   **Definition**: The art of designing the input text to guide the model's probability distribution.
*   **Translation Example**: Writing the **Translation Brief** (Skopos).
*   **Why it matters**: The quality of the output is usually limited by the quality of the prompt, not the intelligence of the model.

### **Temperature**
*   **Definition**: A parameter (0.0 to 1.0) that controls randomness.
    *   *Low Temp (0.1)*: Deterministic. Always picks the most likely word.
    *   *High Temp (0.9)*: Creative. Picks less likely words.
*   **Translation Example**:
    *   *Temp 0.2*: Legal/Technical translation (Precision).
    *   *Temp 0.8*: Poetry/Marketing translation (Inspiration).
*   **Why it matters**: You must adjust this knob depending on your Skopos.

### **Hallucination**
*   **Definition**: When the model generates text that is grammatically fluent but factually incorrect or unfaithful to the source.
*   **Math Intuition**: The model is filling a "Data Void" with probable-sounding noise.
*   **Translation Example**: A translator guessing the meaning of a word they don't know because they are too embarrassed to check the dictionary.
*   **Why it matters**: It is the #1 risk in AI translation. It requires "Human-in-the-Loop" verification.

### **Chain-of-Thought (CoT)**
*   **Definition**: Prompting the model to "think step-by-step" before giving the final answer.
*   **Translation Example**: A "Think-Aloud Protocol" (TAP). "First I see this idiom, I look for an equivalent, I decide on X, so the translation is..."
*   **Why it matters**: It drastically improves accuracy on complex logic or nuanced translation tasks.

---

## 5. Visual Summary

`![[images/llm_glossary_viz.png]]`
*(Alt Text: A diagram showing the flow: Token -> Vector -> Transformer Layers -> Probability Distribution -> Selection (Temperature) -> Output Token.)*

<figure>
<figcaption>External Concept: The LLM Processing Pipeline.</figcaption>
</figure>


---
## Cross-References
- [[outline]]
- [[References]]
- [[Visual_Assets]]
