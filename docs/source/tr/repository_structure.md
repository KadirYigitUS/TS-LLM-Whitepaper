---
baslik: Depo Yapısı
---

# Depo Yapısı

## Klasör Özeti
```text
/docs           → Sphinx + RTD içerikleri
/Obsidian_Project → Ana çalışma notları
/script         → Otomasyon betikleri
/data           → Bağlantılı grafikler ve meta veriler
tables/         → CSV takip tabloları
```

## Sphinx Kaynakları
- `_static/` logo + mermaid init
- `en/` İngilizce notlar
- `tr/` Türkçe özetler
- `api_reference/` script modülleri

## İş Akışı
1. Obsidian’da yaz → temizleyici betik ile `docs/source/en` içine aktar.
2. Türkçe özet hazırla.
3. `make -C docs html` ile yerelde doğrula.
4. `make -C docs api` ile API sayfalarını güncelle.
5. GitHub’a push → Read the Docs otomatik derler.

## RTD Dil Ayarı
- İngilizce proje ana proje olur.
- RTD’de “Translations” sekmesinden Türkçe proje bağlanır.
- İki proje de aynı `main` dalını izler.
