````markdown
# user-prompt.md
---
title: "User Prompt — Project: Extended_Foundational_Models_of_LLM_paper"
tags: [LLM, TranslatorStudies, Obsidian, ProjectPlan]
author: "Generated prompt template for AI"
audience: "Translator Studies academics (novice in computational methods)"
date-created: 2025-12-02
---

> ## Purpose (one sentence)
> Provide a reusable, Obsidian-ready instruction file that the AI will follow to create the full set of MD deliverables required for an extended literature review and methodology guide on LLMs for Translator Studies.

> ## Recipient Profile (short)
> Translator Studies academics familiar with translation theory and qualitative methods but *not* with statistical linguistics, NLP, ML, stylometry, or neural network training. The material must fill epistemic gaps with step-by-step, causal explanations, and always be accessible.

---

## Master Constraints (must be obeyed by the AI)
1. **One MD file per assistant response.**  
2. **Each assistant response must begin with a short “Technical Implementation Plan” (2–5 bullet points) and end with either `// continue` _or_ a request for user confirmation** (the first file must request confirmation to proceed).  
3. **Never implement multiple files in the same response.** Only one file = one message.  
4. **Obsidian flavor:** use nested code blocks for the paper content. Use triple-backtick code fences with `markdown` language tag to present file contents (this makes the file copy/pasteable into Obsidian). Example pattern below.  
5. **Stop tokens:** Keep user-directed explanatory sentences ≤3. Prioritize content tokens for the paper. No placeholders/TODO. No truncation.  
6. **Citations:** APA style for References.md. Every section that makes an internet-verifyable factual claim must include a DOI or, if no DOI, a canonical citation (publisher + year). Include “API citation” lines in summaries as required (format guidance below).  
7. **Images & Infographics:** include an Obsidian-friendly embed link example `![[images/figure1.png]]` plus an external web embed example `<iframe src="https://example.com" ...></iframe>` when web embeds are relevant. Provide both an internal asset suggestion and an external URL fallback.  
8. **Tables & Schemas:** include Markdown tables (and a downloadable CSV link pattern `sandbox:/mnt/data/<file>.csv` if a file is created).  
9. **Response sequencing:** After each MD file I will place the literal line `// continue` (if awaiting your "Continue") or I will request confirmation (for the technical plan). You must say **Continue** or **Proceed** for me to send the next file.

---

## File list & purpose (order of generation — one file per response)
1. `technical_implementation_plan.md` — exact technical plan (short) and execution checklist.  
2. `Outline.md` — hierarchical outline for the whole paper set.  
3. `Combined_Primary_and_Secondary_Source_review_table.md` — a Markdown table merging all primary & secondary sources and mapping them to LLM-Stage & methods.  
4. `Combined_Primary_and_Secondary_Source_review.md` — full literature review (primary + secondary), causal chains, 2-paragraph summary per paper with API citation and page numbers, DOI.  
5. `Tertiary_Sources_review_table.md` — table of tertiary sources for the three special topics (Prompt engineering & Skopos, Empiric Critique, Context Engineering).  
6. `Prompt requirements in PROMPT-ENGINEERING AND SIMILARITY OF SKOPOS Theorie and Prompting practice.md` — focused review, prompts templates, Skopos mapping.  
7. `Beyond_prompt_engineering: What is Context and Context Engineering.md` — conceptual & operational definition of context + engineering patterns.  
8. `Criticize_Empiric_TranslationStudies_and_current_use_of_LLMs_in_Translation_Studies_Literature.md` — critical review and recommendations.  
9. `Tertiary_Sources_review.md` — detailed tertiary literature and annotated bibliography.  
10. `Discussions.md` — citational dialogue, comparisons, methodological implications.  
11. `Conclusion.md` — conclusions and in-text referenced synthesis.  
12. `Future_studies.md` — concrete future research questions, experimental designs, suggested metrics.  
13. `References.md` — APA style references (all DOIs included where available).  
14. `General_Terminology.md` — glossary of terms targeted to the recipient with simple examples and minimal math.  

> **Note:** This `user-prompt.md` is the master instruction; the AI will replicate these constraints inside each generated MD file as frontmatter and a short "file constraints" section.

---

## Obsidian formatting & nested code-block template (copy/pasteable)
Everything that will become an MD file must be presented inside a code fence ` ```markdown ` so you can paste it into Obsidian.

**Example:**
```markdown
```markdown
---
title: "Outline.md"
tags: [Outline, LLM, TranslatorStudies]
---

# Outline — Extended Foundational Models of LLMs for Translator Studies

## 0. Frontmatter and Usage Notes
- Intended audience: Translator Studies academics...
- File constraints: one MD file per response, obey token rules...

## 1. Introduction
1.1 Motivation
1.2 Audience knowledge gaps (bulleted)
...

## 2. Literature review (structure pointers)
...

---
````

````
(Above: the outer triple-backticks show the assistant reply container; the inner triple-backticks with `markdown` are the file content you paste into Obsidian.)

---

## Citation & "API citation" formatting rules (strict)
1. **APA bibliography** in `References.md` (author, year, title, journal/proceedings, DOI).  
2. **Inline summary API citation** (in the two-paragraph summaries required in Combined reviews) — include a line at the end of the two-paragraph summary:  
   `API citation: <source name> — pages X–Y.`  
   Example: `API citation: Vaswani et al., "Attention Is All You Need" — pages 1–12.`  
   (When available include DOI on the final References entry.)  
3. **Every "end with API citation, DOI" instruction must be literal**: after each paper summary include `API citation: <title> — pages X–Y; DOI: 10.xxxx/xxxxx`.

---

## Tables, Figures, and Assets
- **Tables**: Use standard Markdown tables. Keep wide tables limited using wrap or multi-line cells. Example cell for methods column can include bullet lists using `<br>` for line breaks.  
- **Figures**: Provide both internal and external references:
  - Internal: `![[images/figure2_attention_viz.png]]`
  - External: HTML embed fallback:
    ```html
    <figure>
      <iframe src="https://example.com/attention_viz" width="100%" height="400"></iframe>
      <figcaption>Attention visualization (external)</figcaption>
    </figure>
    ```
- **Infographics**: For each infographic required, include alt text and a suggested generation prompt (for your own image tool) and a download filename.

---

## Per-file mandatory sections (template)
Every MD file generated must include, in this order:
1. YAML frontmatter with `title`, `tags`, `date`, `author`, `file_constraints`.  
2. A short Technical Implementation Plan (2–4 bullets specific to that file).  
3. The main content (organized with H2/H3 headers).  
4. At least one table or figure (unless the file is purely terminology).  
5. Citations inline and final `References` short list (not complete References.md) with DOIs.  
6. End with the literal line `// continue` (except for the `technical_implementation_plan.md` which ends with a request for confirmation).

---

## Terminology & pedagogy rules
- Always *start* each technical section with a 1–2 sentence "Why this matters to translator studies" statement.  
- For each technical concept, include: (a) short plain-language definition, (b) a minimal mathematical intuition (1–3 equations max) and (c) a worked tiny example in translation context (2–3 sentences).  
- Avoid advanced notation unless necessary; when used, define every symbol.  
- Use friendly, slightly playful tone but remain academically rigorous.

---

## Workflow & quality checks (automated checklist to include in every file)
- [ ] File frontmatter present  
- [ ] Technical plan present  
- [ ] At least one figure/table present or explained why not  
- [ ] All claims have supporting citations with DOI when available  
- [ ] APA references appended or referenced to `References.md`  
- [ ] Ends with `// continue` or confirmation request

---

## Example small prompt templates (for the Prompt file)
Place these inside `Prompt requirements in PROMPT-ENGINEERING ... .md` later, but include here as canonical forms:

1. **Skopos-mapped translation prompt (example)**  
````

You are an assistant helping with a literary translation where the Skopos is "preserve rhythm and voice". Input: <source_text>. Output: <translation> with a 3-line justification of choices and an explanation of trade-offs.

```
2. **Chain-of-Thought prompt (translation diagnostic)**  
```

Q: Translate and explain decisions (step-by-step). A: Let's think step by step: [literal mapping] -> [stylistic mapping] -> final translation.

```

---

## How we will handle long tables / large reference lists
- I will place large tables in `[Combined_Primary_and_Secondary_Source_review_table.md]` as compressed Markdown tables and, if necessary, provide a CSV in `/mnt/data` and a download link in the file. (You will instruct me to create files when you confirm.)

---

## Final: Deliverable behavior & sequencing
- I will now pause. If you **Confirm**, I will send `technical_implementation_plan.md` as the next message (one full MD file) in an Obsidian nested code block.  
- After each delivered MD file you reply **Continue** or **Proceed** and I will deliver the next file.  
- Any deviation or new constraint you add later will be applied to subsequent files only (I will note the change at the top of the next file).

```

// REQUEST FOR USER CONFIRMATION: Reply **Proceed** to start the sequence with `technical_implementation_plan.md`, or reply **Modify** and list any changes you want applied to the plan.
