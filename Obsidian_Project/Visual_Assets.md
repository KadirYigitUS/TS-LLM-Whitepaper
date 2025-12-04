---
title: "Visual_Assets.md"
tags: [Visuals, Diagrams, Mermaid, Obsidian]
author: "AI Assistant"
date: 2025-12-02
file_constraints: "Obsidian-native Mermaid.js definitions for project concepts"
---

# Visual Assets (Mermaid Diagrams)

## 1. The Evolutionary Arc of LLMs
*A timeline visualization of the 9 Seminal Papers reviewed in Phase II.*

```mermaid
%%{init: {"theme": "base", "themeVariables": {"primaryColor": "#ffcc00", "edgeLabelBackground": "#ffffff", "tertiaryColor": "#fff"}}}%%
timeline
    title The 9 Seminal Papers: From Architecture to Agency
    2017 : Attention Is All You Need (Vaswani)
         : The Transformer Architecture
    2018 : BERT (Devlin)
         : Bidirectional Context
    2020 : GPT-3 (Brown) & Scaling Laws (Kaplan)
         : Emergence & Predictability
    2022 : Chain-of-Thought (Wei) & InstructGPT (Ouyang) & Flan (Longpre)
         : Reasoning & Alignment
    2023 : LLaMA (Touvron) & Toolformer (Schick)
         : Democratization & Tool Use
```

---

## 2. The Skopos Prompting Triangle
*Visualizing the relationship between the User (Client), the Prompt (Brief), and the Model (Translator), based on Nord/Vermeer.*

```mermaid
graph TD
    User((User / Client)) -->|Defines Purpose| Prompt[Prompt / Commission]
    Prompt -->|Constraints| Model{LLM / Translator}
    
    subgraph "The Alignment Loop"
    Model -->|Generates| Draft[Draft Output]
    Draft -->|Evaluated against| Prompt
    end
    
    Draft -->|Delivered as| Translatum(Final Translatum)
    Translatum -->|Serves| Audience((Target Audience))
    
    style Prompt fill:#f9f,stroke:#333,stroke-width:2px
    style Model fill:#bbf,stroke:#333,stroke-width:2px
```

---

## 3. Context Engineering: The Hallidayan Injection
*How to force "World Context" into the "Context Window" using RAG (Retrieval Augmented Generation).*

```mermaid
flowchart LR
    Source["Source Text"]

    subgraph Hallidayan_Context
        Field["Field: Terminology"]
        Tenor["Tenor: Tone / Role"]
        Mode["Mode: Format"]
    end

    subgraph Context_Engineering
        RAG["Retrieval System"]
        PromptEng["Prompt Architect"]
    end

    Source --> RAG
    Field --> RAG

    RAG -->|Injects Terms| PromptEng
    Tenor -->|Injects Persona| PromptEng
    Mode -->|Injects Constraints| PromptEng

    PromptEng -->|Compiled Prompt| Window["Context Window (4k-128k Tokens)"]
    Window --> Model["LLM Inference"]
    Model --> Output["Contextualized Translation"]

    style Window fill:#ff9,stroke:#333,stroke-width:4px

```

---

## 4. The LLM Processing Pipeline (Simplified)
*A pedagogical view of how text becomes numbers and back to text.*

```mermaid
sequenceDiagram
    participant Human
    participant Tokenizer
    participant Transformer
    participant Probabilities
    
    Human->>Tokenizer: "Translate 'Cat'"
    Tokenizer->>Transformer: [15496, 2033, 9822] (Tokens)
    Transformer->>Probabilities: Process Vectors...
    Probabilities->>Probabilities: Apply Temperature (Creativity)
    Probabilities->>Tokenizer: Select ID [8441] ("Chat")
    Tokenizer->>Human: "Chat"
```

## 5. Semantic Scholar + ConnectedPapers Network (Live)
<iframe class="widget" src="data/network_manifests/combined_network_widget.html" title="TS-LLM knowledge graph"></iframe>

> **Build note**: Run `python script/build_semantic_widgets.py` after refreshing Semantic Scholar or ConnectedPapers data. The script regenerates the per-paper widgets, merges them with any ConnectedPapers payloads, and emits `data/network_manifests/combined_network_widget.html` for embedding here and in `white_paper.html`.

---
## Cross-References
- [[outline]]
- [[References]]
- [[General_Terminology]]
