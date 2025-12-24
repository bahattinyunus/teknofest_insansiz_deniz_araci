# 🧠 Algılama Sistemi (Perception System)

## 👁 Görsel Algı (Visual Perception)
Sistemimiz, **ZED 2i Stereo Kamera** vasıtasıyla çift gözlü görme yeteneğine sahiptir. Bu yetenek, sadece renkleri değil, derinliği de (depth maps) gerçek zamanlı olarak işlemesine olanak tanır.

### YOLOv10 & TensorRT Optimizasyonu
Nesne tespiti katmanında, en yeni nesil **YOLOv10 (Small)** modeli kullanılmaktadır. Model, NVIDIA Jetson Orin Nano üzerinde maksimum verimlilikle çalışabilmesi için **TensorRT** motoru ile optimize edilmiştir.

- **Giriş Çözünürlüğü:** 640x640 px
- **FP16 Hassasiyeti:** Jetson üzerinde 40+ FPS performans.
- **Sınıflandırma:** Şamandıralar (Kırmızı/Yeşil), İskeleler, Diğer Deniz Araçları.

## 📡 Lidar Füzyonu
RPLidar A3'ten gelen 360 derecelik 2B lazer verisi, kamera verisiyle **Extended Kalman Filter (EKF)** kullanılarak birleştirilir. Bu, sisli veya düşük ışıklı ortamlarda bile yüksek hassasiyetli engel sakınma sağlar.

### Gürültü Filtreleme
Lidar verilerindeki su serpintisi ve dalga kaynaklı gürültüleri temizlemek için **Statistical Outlier Removal (SOR)** filtresi uygulanmaktadır.
