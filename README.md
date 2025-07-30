# 🚚 Kargo Takip Sistemi

Bu proje, bir kargo şirketinin müşterilerinin gönderilerini ve gönderilerin durumunu takip edebileceği bir Python yazılım sistemidir.

## 📋 Proje Tanımı

Kargo Takip Sistemi, hem gönderici hem de alıcı bilgilerinin yönetildiği, paketlerin durumu ve hareket geçmişinin izlendiği kapsamlı bir uygulamadır.

## ✨ Özellikler

### 📦 Paket Yönetimi
- **Benzersiz Takip Numarası**: Her paket için otomatik oluşturulan takip numarası
- **Paket Tipleri**: Evrak, koli, kırılabilir ürün, bozuk, özel
- **Durum Takibi**: hazırlanıyor → yolda → teslim edildi
- **Ağırlık ve Adres Bilgileri**: Detaylı paket bilgileri

### 👥 Müşteri Yönetimi
- **Bireysel Müşteriler**: TC kimlik numarası ile kayıt
- **Kurumsal Müşteriler**: Şirket adı ve vergi numarası ile kayıt
- **Müşteri Bilgileri**: Ad, soyad, telefon, adres

### 🔍 Takip ve Sorgulama
- **Gerçek Zamanlı Takip**: Paket durumlarının anlık güncellenmesi
- **Hareket Geçmişi**: Tarih ve saat damgalı durum değişiklikleri
- **Detaylı Sorgulama**: Takip numarasına göre paket bilgileri
- **Müşteri Bazlı Listeleme**: Müşteriye ait tüm paketler

## 🗂️ Dosya Yapısı

```
kargo_sistemi/
├── paket.py         # Paket sınıfı ve paket tipleri
├── musteri.py       # Müşteri sınıfı ve alt sınıflar
├── takip.py         # Paket durumu ve hareket yönetimi
├── kargo.py         # Kargo yönetim sistemi
├── main.py          # Ana uygulama ve kullanıcı arayüzü
└── README.md        # Proje dokümantasyonu
```

## 🚀 Kurulum ve Çalıştırma

### Gereksinimler
- Python 3.6 veya üzeri
- Standart Python kütüphaneleri (uuid, datetime, enum)

### Çalıştırma
```bash
python main.py
```

## 📱 Kullanım Kılavuzu

### Ana Menü Seçenekleri

1. **Müşteri Ekle**: Yeni müşteri kaydı oluşturma
2. **Paket Oluştur**: Yeni paket oluşturma
3. **Paket Durumu Değiştir**: Paket durumunu güncelleme
4. **Paket Sorgula**: Takip numarasına göre paket bilgileri
5. **Tüm Paketleri Listele**: Sistemdeki tüm paketleri görüntüleme
6. **Müşteri Paketlerini Listele**: Belirli müşterinin paketlerini görüntüleme
7. **Demo Verileri Yükle**: Örnek verilerle sistemi test etme
8. **Çıkış**: Programdan çıkış

### Demo Verileri

Sistem, test amaçlı demo verileri içerir:
- 3 farklı müşteri (2 bireysel, 1 kurumsal)
- 3 farklı paket tipi
- Farklı durumlarda paketler

## 🏗️ Sistem Mimarisi

### Sınıf Yapısı

#### Paket Sınıfı (`paket.py`)
```python
class Paket:
    - paket_id: Benzersiz paket kimliği
    - takip_no: Takip numarası
    - paket_agirligi: Ağırlık bilgisi
    - paket_tipi: Paket tipi (enum)
    - paket_durumu: Mevcut durum
    - paket_adresi: Teslimat adresi
```

#### Müşteri Sınıfları (`musteri.py`)
```python
class Müsteri:  # Ana müşteri sınıfı
class BireyselMüsteri(Müsteri):  # TC kimlik no ile
class KurumsalMüsteri(Müsteri):  # Şirket bilgileri ile
```

#### Takip Sistemi (`takip.py`)
```python
class TakipSistemi:
    - Paket hareket geçmişi
    - Durum değişiklik kayıtları
    - Tarih damgalı işlemler
```

#### Kargo Sistemi (`kargo.py`)
```python
class KargoSistemi:
    - Merkezi yönetim sistemi
    - Müşteri ve paket yönetimi
    - Sorgulama ve raporlama
```

## 🔧 Teknik Özellikler

- **Nesne Yönelimli Programlama**: Sınıf tabanlı mimari
- **Enum Kullanımı**: Paket tiplerinin standartlaştırılması
- **UUID**: Benzersiz takip numaraları
- **Tarih/Saat İşlemleri**: Hareket geçmişi kayıtları
- **Hata Yönetimi**: Kullanıcı dostu hata mesajları

## 📊 Veri Yapıları

### Paket Durumları
- `hazırlanıyor`: Paket hazırlanma aşamasında
- `yolda`: Paket taşıma sürecinde
- `teslim edildi`: Paket başarıyla teslim edildi
- `iade edildi`: Paket iade edildi

### Paket Tipleri
- `evrak`: Doküman ve evraklar
- `koli`: Standart koli paketleri
- `kırılabilir ürün`: Hassas ürünler
- `bozuk`: Bozulabilir ürünler
- `özel`: Özel paketler


## 👨‍💻 Geliştirici

Bu proje, veri bilimi kursu kapsamında geliştirilmiştir.

## 📄 Lisans

Bu proje eğitim amaçlı geliştirilmiştir.

---