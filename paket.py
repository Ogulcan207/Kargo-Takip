from enum import Enum
from datetime import datetime

class PaketTipi(Enum):
    EVRAK = "evrak"
    KOLI = "koli"
    KIRILABILIR = "kırılabilir ürün"
    BOZUK = "bozuk"
    OZEL = "özel"

class Paket:
    def __init__(self, paket_id, takip_no, paket_agirligi, paket_tipi, paket_durumu, paket_adresi):
        self.paket_id = paket_id
        self.takip_no = takip_no
        self.paket_agirligi = paket_agirligi
        self.paket_tipi = paket_tipi
        self.paket_durumu = paket_durumu
        self.paket_adresi = paket_adresi
        self.olusturma_tarihi = None
        self.teslim_tarihi = None

    def __str__(self):
        return f"Paket ID: {self.paket_id}, Takip No: {self.takip_no}, Paket Agirligi: {self.paket_agirligi}, Paket Tipi: {self.paket_tipi}, Paket Durumu: {self.paket_durumu}, Paket Adresi: {self.paket_adresi}"

    def durum_guncelle(self, yeni_durum):
        self.paket_durumu = yeni_durum
        if yeni_durum == "teslim edildi":
            self.teslim_tarihi = datetime.now()

    def paket_bilgileri_getir(self):
        return {
            'paket_id': self.paket_id,
            'takip_no': self.takip_no,
            'agirlik': self.paket_agirligi,
            'tip': self.paket_tipi,
            'durum': self.paket_durumu,
            'adres': self.paket_adresi,
            'teslim_tarihi': self.teslim_tarihi
        }
