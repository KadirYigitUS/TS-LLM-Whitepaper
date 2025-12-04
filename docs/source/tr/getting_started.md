---
baslik: Skopos ve Prompt Tasarımı
---

# Skopos Yaklaşımıyla Prompt Tasarımı

## Neden?
LLM’ler amaç belirtilmediğinde internet ortalamasını üretir. Skopos kuramındaki “iş siparişi” (commission), burada sistem promptu olarak yeniden yazılır.

## Eşleştirme Tablosu
| Skopos terimi | LLM karşılığı | İşlev |
| --- | --- | --- |
| Sipariş/Brief | Sistem veya rol promptu | Tonu, rolü ve çıktıyı tanımlar |
| Skopos | Amaç cümlesi | Metnin neden üretildiğini açıklar |
| Kaynak metin | Kullanıcı girdisi | Dönüştürülecek malzeme |
| Translatum | Çıktı | Model cevabı |

## İyi Prompt Örneği
```
Uzman edebiyat çevirmenisin. Amerikan roman okuru için işlevsel eşdeğerlik üret.
Kaynak: "Il pleut des cordes."
Kısıt: Dipnot yok, mümkünse deyim kullan.
```
Çıktı: “It’s raining cats and dogs.”

## Bağlılık (Loyalty) ve Hizalama
- Nord’un sadakat kavramı, RLHF güvenlik filtreleriyle çatışabilir.
- Duruma göre açık ağırlıklı modeller veya ayrıntılı hukuki amaç açıklamaları gerekir.

## Kontrol Listesi
1. Rol/persona tanımla.
2. Amaç ve hedef kitleyi yaz.
3. Biçim/tasarım kısıtlarını ekle (satır uzunluğu, tablo düzeni vb.).
4. Sadakati güvenceye al (belirsizlik etiketi, terminoloji sözlüğü, vs.).
