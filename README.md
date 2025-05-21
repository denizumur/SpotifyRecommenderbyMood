#  Ruh Haline Göre Spotify Şarkı Önerici

Bu proje, kullanıcının mikrofonla söylediği Türkçe ifadeyi:
1. İngilizce'ye çevirir (Whisper modeli ile),
2. Duyguyu tespit eder (Naive Bayes sınıflandırıcı ile),
3. Tespit edilen duyguya göre Spotify API üzerinden şarkılar önerir.

##  Özellikler

-  Mikrofonla ses kaydı
-  Whisper ile İngilizce'ye çeviri
-  Naive Bayes duygu sınıflandırması (`dair-ai/emotion`)
-  Spotify API'den dinamik şarkı önerisi
-  Streamlit arayüzü, karanlık mod, emoji destekli

## Kurulum

```bash
git clone https://github.com/kendi-repo-url.git
cd spoti_project
pip install -r requirements.txt
