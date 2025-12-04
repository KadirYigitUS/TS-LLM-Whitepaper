---
baslik: Görsel Varlıklar ve Ağlar
---

# Görsel Varlıklar

::::{tab-set}
:::{tab-item} Türkçe
Bu sayfa Türkçe özetleri içerir.
:::
:::{tab-item} English
:doc:`Access the English visuals <en/knowledge_graphs>`
:::
::::

## Zaman Çizelgesi
```{raw} html
<div class="mermaid">
timeline
    title 9 Temel Makale
    2017 : Transformer — Attention Is All You Need
    2018 : BERT — Çift yönlü bağlam
    2020 : GPT-3 & Scaling Laws — Ölçek ve öngörülebilirlik
    2022 : CoT & InstructGPT & Flan — Akıl yürütme ve hizalama
    2023 : LLaMA & Toolformer — Demokratikleşme ve araç kullanımı
</div>
```

## Skopos Üçgeni
```{raw} html
<div class="mermaid">
graph TD
    U((Kullanıcı)) -->|Amaç| P[Prompt/Brief]
    P -->|Kısıt| M{LLM}
    M --> C[Taslak]
    C -->|Değerlendirme| P
    C -->|Teslim| A((Hedef Kitle))
</div>
```

## Bağlam Enjeksiyonu
```{raw} html
<div class="mermaid">
flowchart LR
    Field --> RAG
    Tenor --> RAG
    Mode --> RAG
    RAG --> Prompt
    Prompt --> Window
    Window --> Model
</div>
```

## Ağ Bileşimi
<iframe src="../data/network_manifests/combined_network_widget.html" title="Ağ" loading="lazy"></iframe>
