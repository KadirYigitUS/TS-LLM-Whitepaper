> Tags: #Critique #Methodology #Empiricism #Statistics

# Criticizing Empiric Translation Studies: The Trap of the "Average"

## 1. Why this matters to Translation Studies
Current research in Translation Studies (TS) often asks: *"Is GPT-4 better than a human translator?"*
This is the wrong question. It assumes the LLM has a fixed skill level.
In reality, an LLM's performance is a function of its **Context Engineering**. Comparing a generic GPT-4 prompt against a specialized human is a methodological flaw. Furthermore, statistical models have a hidden danger: they are mathematically designed to be boring.

## 2. The Statistical Trap: Regression to the Mean
**Source**: Koehn, P. (2010/2020). *Statistical Machine Translation*.

### 2.1 The Mathematics of "Blandness"
LLMs are trained to minimize "Perplexity" (Surprise).
*   **The Mechanism**: The model predicts the word that has the highest probability based on the training data.
*   **The Result**: If 80% of texts translate "problème" as "problem" and only 5% translate it as "snag" or "hitch," the model will almost always choose "problem."
*   **The Critique**: Excellent translation is often an **outlier**—a rare, creative choice that fits the specific Skopos perfectly. The LLM naturally suppresses these outliers to play it safe.
    *   *TS Consequence*: We risk a "homogenization" of language where all translations sound like "average" international English.

## 3. The Flaw of Current TS Research Designs
**Source**: Kenny, D. (2022). *Machine Translation for Everyone: Empowering Users in the Age of Artificial Intelligence*.

### 3.1 The "Black Box" Testing Error
Many TS papers use the following methodology:
1.  Take a Source Text.
2.  Feed it to Google Translate/ChatGPT (with a blank or basic prompt).
3.  Count the errors in the Output.
4.  Conclusion: "AI struggles with cultural nuance."

**The Flaw**: This tests the **Zero-Shot capability** of the model, not its maximum capability. It is like testing a human translator by forbidding them from asking clarifying questions or using a dictionary.
*   **New Standard**: Research must report the **Prompt** as a control variable. A study without the exact prompt is irreproducible.

### 3.2 The "Gold Standard" Fallacy (BLEU/COMET)
Engineering papers (e.g., Vaswani et al.) use BLEU scores (Bilingual Evaluation Understudy) to claim "State of the Art."
*   **How BLEU works**: It counts n-gram overlaps between the Machine Output and a Human "Reference" translation.
*   **The Problem**: If the Human Reference is literal, a creative Machine Translation gets a *low* score. If the Human Reference is free, a literal Machine Translation gets a *low* score.
*   **Skopos Critique**: BLEU ignores Purpose. A translation can be perfect for a Manual (Literal) but get a bad score because the Reference was for a Novel (Free).
*   **Recommendation**: TS scholars must reject BLEU in favor of **MQM (Multidimensional Quality Metrics)** or functional human evaluation.

## 4. The "Data Void" and Cultural Erasure
**Source**: Bowker, L. (2023). *De-mystifying Translation: Introducing Translation to Non-translators*.

### 4.1 The High-Resource Bias
LLMs are trained on the internet. The internet is dominated by English (and a few other Western languages).
*   **The Consequence**: Concepts unique to low-resource languages (e.g., Irish, Swahili, Indigenous languages) are statistically drowned out.
*   **Hallucination Risk**: When the model encounters a cultural concept it hasn't seen often (a "Data Void"), it doesn't confess ignorance; it hallucinates a plausible-sounding English concept.
*   **Critique**: Using LLMs for cultural heritage translation without "Human-in-the-Loop" is methodologically unethical because the model pushes the target culture toward the dominant (Anglophone) norm.

## 5. A New Methodology: Process Analysis & Prompt Auditing

We must move from **Product-Oriented Research** (grading the output) to **Process-Oriented Research** (analyzing the interaction).

### 5.1 Experimental Design: The Prompt Audit
Instead of "How many errors?", ask:
*   "Which prompt constraint eliminated the cultural error?"
*   "Does Chain-of-Thought prompting increase the variety of vocabulary?"

### 5.2 The "Cyborg" Protocol
Research should measure the **Total System** (Translator + AI):
*   **Control**: Human translating alone.
*   **Experiment**: Human + AI.
*   **Metric**: Not just speed/quality, but **Cognitive Load** and **Agency**. Does the translator feel like an editor of garbage (low agency) or a director of an orchestra (high agency)?

## 6. Summary: The Empiric Shift
To criticize LLMs effectively, Translation Studies must:
1.  **Acknowledge the Probabilistic Bias**: Models prefer the average. We must prompt them to be exceptional.
2.  **Reject Automated Metrics**: Meaning is not n-gram overlap.
3.  **Control the Variable**: The Prompt is part of the method.
4.  **Focus on Low-Resource Risks**: Where is the data coming from?

## References
*   **Bowker, L.** (2023). *De-mystifying Translation: Introducing Translation to Non-translators*. Routledge.
*   **Kenny, D.** (2022). *Machine Translation for Everyone: Empowering Users in the Age of Artificial Intelligence*. Language Science Press.
*   **Koehn, P.** (2010). *Statistical Machine Translation*. Cambridge University Press.


---
## Cross-References
- [[outline]]
- [[References]]
- [[General_Terminology]]
- [[Visual_Assets]]
