---
baslik: Sorun Giderme
---

# Sorun Giderme

## 1. Metinler sıradanlaşıyor
- **Sebep**: Model ortalamaya çekiliyor.
- **Çözüm**: Skopos’u ayrıntılandır, örnekler ekle, sıcaklığı ihtiyaca göre ayarla.

## 2. Hassas metinler reddediliyor
- **Sebep**: RLHF güvenlik filtreleri.
- **Çözüm**: Yerel/açık modeller kullan veya hukuki amacı promptta açıkla.

## 3. Uzun metinde bağlam kaybı
- **Sebep**: Token penceresi sınırı.
- **Çözüm**: Böl, özetle, Field/Tenor/Mode paketlerini her parçaya enjekte et.

## 4. Mermaid/iframe çalışmıyor
- **Sebep**: CDN veya CSP engeli.
- **Çözüm**: `_static/js/mermaid-init.js` dosyasını kontrol et; büyük widgetları GitHub Pages’tan çağır.

## 5. API dokümantasyonu derlenmiyor
- **Sebep**: Eksik bağımlılıklar.
- **Çözüm**: `autodoc_mock_imports` listesine yeni paket ekle, `make api` çalıştır.
