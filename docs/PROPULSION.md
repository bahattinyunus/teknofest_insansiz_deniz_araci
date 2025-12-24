# ⚙️ İtki Sistemi ve Kontrol (Propulsion & Control)

## 🚤 Mekanizma ve İtki
Aracımız, diferansiyel sürüş prensibine dayalı iki adet **BlueRobotics T200** fırçasız motor kullanmaktadır.

### İtki Karakteristiği
- **Gerilim:** 16V (4S LiPo)
- **Maksimum İtki:** 5.1 kg f (motor başına)
- **Konfigürasyon:** Katamaran arkası çift motor.

## 🎮 PID Kontrolör Mimarisi
İDA'nın rota takibi ve hızı, kapalı döngü (Closed-Loop) PID kontrolörler ile yönetilir.

### Mevcut PID Formülü:
$$u(t) = K_p e(t) + K_i \int_{0}^{t} e(\tau) d\tau + K_d \frac{de(t)}{dt}$$

- **Yaw (Rota) Kontrol:** Aracın belirlenen hedefe dönmesini sağlar. $K_p$ değeri, suyun direncine göre optimize edilmiştir.
- **Thrust (Hız) Kontrol:** Hedef noktasına olan yaklaşıma göre motor gücünü ayarlar.

## ⚡ Güç Yönetimi
Elektronik sistemler (Jetson, Pixhawk) ana bataryadan izole edilmiş regülatörler vasıtasıyla beslenir, bu sayede motorların çektiği ani akımlar sensör verilerini etkilemez.
