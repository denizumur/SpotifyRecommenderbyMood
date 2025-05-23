#  Ruh Haline Göre Spotify Şarkı Önerici

Bu proje, kullanıcının mikrofonla söylediği Türkçe ifadeyi:
1. İngilizce'ye çevirir (Whisper modeli ile),
2. Duyguyu tespit eder (Naive Bayes sınıflandırıcı ile),
3. Tespit edilen duyguya göre Spotify API üzerinden şarkılar önerir.

##  ÖRNEK 
![Uygulama Ekran Görüntüsü](https://i.imgur.com/MpPZ4KG.png)


##  Özellikler

-  Mikrofonla ses kaydı
-  Whisper ile İngilizce'ye çeviri
-  Naive Bayes duygu sınıflandırması (`dair-ai/emotion`)
-  Spotify API'den dinamik şarkı önerisi.
