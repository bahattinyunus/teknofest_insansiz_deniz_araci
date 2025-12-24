# 🗺 Navigasyon ve Yol Planlama (Navigation & Path Planning)

## 🛠 Yol Planlama Algoritmaları
İDA'nın rotası, dinamik bir ortamda hem güvenliği hem de hızı optimize etmek üzere tasarlanmıştır.

### A* (A-Star) Algoritması
Küresel yol planlama için özelleştirilmiş bir A* algoritması kullanılmaktadır. Algoritmanın maliyet fonksiyonu şu şekildedir:

$$f(n) = g(n) + h(n) + w(n)$$

- $g(n)$: Başlangıç noktasından mevcut hücreye olan gerçek maliyet.
- $h(n)$: Mevcut hücreden hedefe olan tahmini (Heuristic) maliyet (Öklid mesafesi).
- $w(n)$: **Engel Ağırlığı.** Engellere yakınlık arttıkça bu değer yükselir, böylece araç güvenli bir marj bırakır.

## 📉 Costmap Kavramı
ROS2 `nav2` altyapısı kullanılarak iki katmanlı bir maliyet haritası (Costmap) oluşturulur:
1. **Static Map:** Yarışma alanı sınırları ve bilinen sabit yapılar.
2. **Dynamic Layer:** Lidar ve Kamera'dan gelen anlık engel verileriyle güncellenen katman.

## 🔄 Dinamik Yeniden Planlama
Eğer yol üzerinde yeni bir engel tespit edilirse, yerel planlayıcı (Local Planner) milisaniyeler içinde ana rotayı terk etmeden "Engelden Sakınma Manevrası" üretir.
