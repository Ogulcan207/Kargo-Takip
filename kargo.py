from paket import Paket
from musteri import Müsteri
from takip import TakipSistemi
import uuid
from datetime import datetime

class KargoSistemi:
    def __init__(self):
        self.paketler = {}
        self.musteriler = {}
        self.takip_sistemi = TakipSistemi()
    
    def musteri_ekle(self, musteri_id, musteri_ad, musteri_soyad, musteri_tel, musteri_adres, musteri_tip="Bireysel"):
        musteri = Müsteri(musteri_id, musteri_ad, musteri_soyad, musteri_tel, musteri_adres, musteri_tip)
        self.musteriler[musteri_id] = musteri
        print(f"Müşteri {musteri_ad} {musteri_soyad} başarıyla eklendi.")
        return musteri
    
    def paket_olustur(self, gonderici_id, alici_id, paket_agirligi, paket_tipi, paket_adresi):
        takip_no = str(uuid.uuid4())[:8].upper()
        paket_id = len(self.paketler) + 1
        
        paket = Paket(paket_id, takip_no, paket_agirligi, paket_tipi, "hazırlanıyor", paket_adresi)
        self.paketler[takip_no] = paket
        
        self.takip_sistemi.paket_ekle(takip_no, paket)
        
        print(f"Paket oluşturuldu. Takip No: {takip_no}")
        return paket
    
    def paket_durum_degistir(self, takip_no, yeni_durum):
        if takip_no in self.paketler:
            paket = self.paketler[takip_no]
            eski_durum = paket.paket_durumu
            paket.paket_durumu = yeni_durum
            
            # Takip sistemine hareket kaydet
            self.takip_sistemi.hareket_ekle(takip_no, eski_durum, yeni_durum)
            
            print(f"Paket {takip_no} durumu '{eski_durum}' → '{yeni_durum}' olarak güncellendi")
        else:
            print(f"Takip numarası {takip_no} bulunamadı!")
    
    def paket_sorgula(self, takip_no):
        if takip_no in self.paketler:
            paket = self.paketler[takip_no]
            print(f"\n=== Paket Bilgileri ===")
            print(paket)
            print(f"\n=== Hareket Geçmişi ===")
            self.takip_sistemi.hareket_gecmisi_goster(takip_no)
        else:
            print(f"Takip numarası {takip_no} bulunamadı!")
    
    def tum_paketleri_listele(self):
        if not self.paketler:
            print("Henüz paket bulunmuyor.")
            return
        
        print("\n=== Tüm Paketler ===")
        for takip_no, paket in self.paketler.items():
            print(f"Takip No: {takip_no} | Durum: {paket.paket_durumu} | Tip: {paket.paket_tipi}")
    
    def musteri_paketleri(self, musteri_id):
        print(f"\n=== Müşteri {musteri_id} Paketleri ===")
        bulunan_paketler = []
        
        for takip_no, paket in self.paketler.items():
            if str(musteri_id) in str(paket.paket_id):
                bulunan_paketler.append(paket)
        
        if bulunan_paketler:
            for paket in bulunan_paketler:
                print(paket)
        else:
            print(f"Müşteri {musteri_id} için paket bulunamadı.")

