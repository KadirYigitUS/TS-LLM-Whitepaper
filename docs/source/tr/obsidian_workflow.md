---
baslik: Obsidian İş Akışı
---

# Obsidian İş Akışı

::::{tab-set}
:::{tab-item} Türkçe
Türkçe kısa sürümü görüyorsunuz.
:::
:::{tab-item} English
:doc:`Read the full English workflow <en/obsidian_workflow>`
:::
::::

## Bağlamın Çift Anlamı
- **Halliday bağlamı**: Field/Tenor/Mode.
- **Model bağlamı**: Token penceresi.

## Bağlam Mühendisliği Adımları
1. Alan sözlüğünü (Field) prompt öncesine ekle.
2. Tenor için persona, hitap ve güç mesafesini tanımla.
3. Mode gerekliliklerini (satır uzunluğu, biçim) belirt.
4. Örneklerle (few-shot) kültürel bağlamı simüle et.

## Ampirik TS Eleştirisi
- Varsayılan promptlarla yapılan testler bilimsel değil.
- BLEU Skopos’u ölçmez; amaç uyumu puanları tutulmalı.
- Veri boşlukları kültürel silinmeye yol açar; prompt günlükleri şart.

## Vault’tan RTD’ye
- `script/obsidian_cleanup.py` dosyaları temizleyip `docs/source/en` altına kopyalar.
- Türkçe özetler `docs/source/tr` altında tutulur.
- Dil sekmeleri `index.md` içinde `sphinx-design` tab set ile gösterilir.
