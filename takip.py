from datetime import datetime

class TakipSistemi:
    def __init__(self):
        self.paketler = {}
        self.hareket_gecmisi = {}
    
    def paket_ekle(self, takip_no, paket):
        self.paketler[takip_no] = paket
        self.hareket_gecmisi[takip_no] = []
        self.hareket_ekle(takip_no, "Oluşturuldu", "hazırlanıyor")
    
    def hareket_ekle(self, takip_no, eski_durum, yeni_durum):
        if takip_no in self.hareket_gecmisi:
            hareket = {
                'tarih': datetime.now(),
                'eski_durum': eski_durum,
                'yeni_durum': yeni_durum,
                'aciklama': f"{eski_durum} → {yeni_durum}"
            }
            self.hareket_gecmisi[takip_no].append(hareket)
    
    def hareket_gecmisi_goster(self, takip_no):
        if takip_no in self.hareket_gecmisi:
            hareketler = self.hareket_gecmisi[takip_no]
            if hareketler:
                for i, hareket in enumerate(hareketler, 1):
                    tarih = hareket['tarih'].strftime("%d.%m.%Y %H:%M")
                    print(f"{i}. {tarih} - {hareket['aciklama']}")
            else:
                print("Henüz hareket kaydı bulunmuyor.")
        else:
            print("Paket bulunamadı.")
    
    def paket_durumu_getir(self, takip_no):
        if takip_no in self.paketler:
            return self.paketler[takip_no].paket_durumu
        return None
    
    def tum_hareketleri_listele(self):
        print("\n=== Tüm Hareket Geçmişi ===")
        for takip_no, hareketler in self.hareket_gecmisi.items():
            print(f"\nPaket: {takip_no}")
            for hareket in hareketler:
                tarih = hareket['tarih'].strftime("%d.%m.%Y %H:%M")
                print(f"  {tarih} - {hareket['aciklama']}")
