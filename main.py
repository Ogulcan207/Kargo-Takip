from kargo import KargoSistemi
from musteri import BireyselMüsteri, KurumsalMüsteri
from paket import PaketTipi

def menu_goster():
    print("\n" + "="*50)
    print("        KARGO TAKİP SİSTEMİ")
    print("="*50)
    print("1. Müşteri Ekle")
    print("2. Paket Oluştur")
    print("3. Paket Durumu Değiştir")
    print("4. Paket Sorgula")
    print("5. Tüm Paketleri Listele")
    print("6. Müşteri Paketlerini Listele")
    print("7. Demo Verileri Yükle")
    print("8. Çıkış")
    print("="*50)

def musteri_ekle_menu(kargo_sistemi):
    print("\n--- Müşteri Ekleme ---")
    musteri_tipi = input("Müşteri tipi (1: Bireysel, 2: Kurumsal): ")
    
    musteri_id = input("Müşteri ID: ")
    musteri_ad = input("Müşteri Adı: ")
    musteri_soyad = input("Müşteri Soyadı: ")
    musteri_tel = input("Telefon: ")
    musteri_adres = input("Adres: ")
    
    if musteri_tipi == "1":
        tc_no = input("TC Kimlik No: ")
        musteri = BireyselMüsteri(musteri_id, musteri_ad, musteri_soyad, musteri_tel, musteri_adres, tc_no)
    else:
        sirket_adi = input("Şirket Adı: ")
        vergi_no = input("Vergi No: ")
        musteri = KurumsalMüsteri(musteri_id, musteri_ad, musteri_soyad, musteri_tel, musteri_adres, sirket_adi, vergi_no)
    
    kargo_sistemi.musteriler[musteri_id] = musteri
    print(f"Müşteri başarıyla eklendi: {musteri}")

def paket_olustur_menu(kargo_sistemi):
    print("\n--- Paket Oluşturma ---")
    
    gonderici_id = input("Gönderici Müşteri ID: ")
    alici_id = input("Alıcı Müşteri ID: ")
    paket_agirligi = input("Paket Ağırlığı (kg): ")
    paket_adresi = input("Teslimat Adresi: ")
    
    print("\nPaket Tipleri:")
    for i, tip in enumerate(PaketTipi, 1):
        print(f"{i}. {tip.value}")
    
    tip_secim = input("Paket Tipi (1-5): ")
    paket_tipleri = list(PaketTipi)
    paket_tipi = paket_tipleri[int(tip_secim)-1].value
    
    kargo_sistemi.paket_olustur(gonderici_id, alici_id, paket_agirligi, paket_tipi, paket_adresi)

def paket_durum_degistir_menu(kargo_sistemi):
    print("\n--- Paket Durumu Değiştirme ---")
    takip_no = input("Takip Numarası: ")
    
    print("\nDurum Seçenekleri:")
    durumlar = ["hazırlanıyor", "yolda", "teslim edildi", "iade edildi"]
    for i, durum in enumerate(durumlar, 1):
        print(f"{i}. {durum}")
    
    durum_secim = input("Yeni Durum (1-4): ")
    yeni_durum = durumlar[int(durum_secim)-1]
    
    kargo_sistemi.paket_durum_degistir(takip_no, yeni_durum)

def paket_sorgula_menu(kargo_sistemi):
    print("\n--- Paket Sorgulama ---")
    takip_no = input("Takip Numarası: ")
    kargo_sistemi.paket_sorgula(takip_no)

def demo_verileri_yukle(kargo_sistemi):
    print("\n--- Demo Verileri Yükleniyor ---")
    
    # Müşteriler
    kargo_sistemi.musteri_ekle("M001", "Ahmet", "Yılmaz", "0555-111-1111", "İstanbul, Kadıköy", "Bireysel")
    kargo_sistemi.musteri_ekle("M002", "Ayşe", "Demir", "0555-222-2222", "Ankara, Çankaya", "Bireysel")
    kargo_sistemi.musteri_ekle("M003", "ABC Şirketi", "Ltd. Şti.", "0212-333-3333", "İstanbul, Beşiktaş", "Kurumsal")
    
    # Paketler
    kargo_sistemi.paket_olustur("M001", "M002", "2.5", "koli", "Ankara, Çankaya Mah.")
    kargo_sistemi.paket_olustur("M002", "M001", "0.5", "evrak", "İstanbul, Kadıköy Mah.")
    kargo_sistemi.paket_olustur("M003", "M001", "5.0", "kırılabilir ürün", "İstanbul, Kadıköy Mah.")
    
    # Durum değişiklikleri
    paketler = list(kargo_sistemi.paketler.keys())
    if len(paketler) >= 3:
        kargo_sistemi.paket_durum_degistir(paketler[0], "yolda")
        kargo_sistemi.paket_durum_degistir(paketler[1], "teslim edildi")
        kargo_sistemi.paket_durum_degistir(paketler[2], "hazırlanıyor")
    
    print("Demo verileri başarıyla yüklendi!")

def main():
    kargo_sistemi = KargoSistemi()
    
    print("Kargo Takip Sistemine Hoş Geldiniz!")
    
    while True:
        menu_goster()
        secim = input("\nSeçiminiz (1-8): ")
        
        if secim == "1":
            musteri_ekle_menu(kargo_sistemi)
        elif secim == "2":
            paket_olustur_menu(kargo_sistemi)
        elif secim == "3":
            paket_durum_degistir_menu(kargo_sistemi)
        elif secim == "4":
            paket_sorgula_menu(kargo_sistemi)
        elif secim == "5":
            kargo_sistemi.tum_paketleri_listele()
        elif secim == "6":
            musteri_id = input("Müşteri ID: ")
            kargo_sistemi.musteri_paketleri(musteri_id)
        elif secim == "7":
            demo_verileri_yukle(kargo_sistemi)
        elif secim == "8":
            print("\nKargo Takip Sisteminden çıkılıyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")
        
        input("\nDevam etmek için Enter'a basın...")

if __name__ == "__main__":
    main()
