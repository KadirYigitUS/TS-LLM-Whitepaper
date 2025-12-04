---
title: Mermaid Regression Test
---

# Mermaid Regression Test

Use this page to ensure CDN-delivered Mermaid renders on Read the Docs.

```{raw} html
<div class="mermaid">
graph LR
    A[Obsidian Notes] --> B(MyST Pages)
    B --> C(Sphinx Build)
    C --> D{Read the Docs}
    D -->|English| E(https://ts-llm-whitepaper.readthedocs.io/en/latest/)
    D -->|Türkçe| F(https://ts-llm-whitepaper.readthedocs.io/tr/latest/)
</div>
```

```{raw} html
<div class="mermaid">
sequenceDiagram
    participant Script
    participant RTD
    participant Reader
    Script->>RTD: push main + make api
    RTD-->>Reader: localized HTML
    Reader->>Script: open issue if broken
</div>
```
