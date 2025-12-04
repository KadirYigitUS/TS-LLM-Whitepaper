---
title: Visual Assets and Knowledge Graphs
---

# Knowledge Graphs & Visual Assets

````{tab-set}

```{tab-item} English

English diagrams appear below.

```

```{tab-item} Türkçe

:doc:`Türkçe kısa sürümü aç <tr/knowledge_graphs>`

```

````

All diagrams originate from `Visual_Assets.md` and were adapted to MyST + Mermaid for Sphinx. Mermaid runs through the CDN configured in `conf.py`; complex widgets load via `<iframe>` elements that point to assets shipped in `docs/data` or GitHub Pages.

## 1. Evolutionary Arc of LLMs
```{raw} html
<div class="mermaid">
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
</div>
```

## 2. Skopos Prompting Triangle
```{raw} html
<div class="mermaid">
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
</div>
```

## 3. Context Engineering Flow
```{raw} html
<div class="mermaid">
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
</div>
```

## 4. LLM Processing Pipeline (Simplified)
```{raw} html
<div class="mermaid">
sequenceDiagram
    participant Human
    participant Tokenizer
    participant Transformer
    participant Probabilities

    Human->>Tokenizer: "Translate 'Cat'"
    Tokenizer->>Transformer: [15496, 2033, 9822]
    Transformer->>Probabilities: Process vectors
    Probabilities->>Probabilities: Apply temperature
    Probabilities->>Tokenizer: Select token 8441 ("Chat")
    Tokenizer->>Human: "Chat"
</div>
```

## 5. Semantic Scholar + Connected Papers Network
<iframe class="widget" src="https://kadiryigitus.github.io/TS-LLM-Whitepaper/data/network_manifests/combined_network_widget.html" title="TS-LLM knowledge graph" loading="lazy"></iframe>

```{note}
If the iframe fails on Read the Docs because of CSP limits, host the widget via GitHub Pages and update the `src` attribute to `https://kadiryigitus.github.io/TS-LLM-Whitepaper/data/network_manifests/combined_network_widget.html`.
```

```{note}
Last widget refresh: 5 Dec 2025 (Connected Papers + Semantic Scholar). After running `python script/build_semantic_widgets.py`, update this timestamp in both EN and TR pages so readers know which snapshot they are viewing.
```

## 6. Build Notes
1. Run `python script/build_semantic_widgets.py` whenever Semantic Scholar or ConnectedPapers exports change.
2. Commit regenerated HTML/JSON assets under `docs/data/` so Read the Docs can publish them (large files should remain on GitHub Pages if they exceed 10&nbsp;MB).
3. Reference diagrams throughout the docs using standard Markdown links instead of Obsidian wikilinks.
