class Müsteri:
    def __init__(self, musteri_id, musteri_ad, musteri_soyad, musteri_tel, musteri_adres, musteri_tip):
        self.musteri_id = musteri_id
        self.musteri_ad = musteri_ad
        self.musteri_soyad = musteri_soyad
        self.musteri_tel = musteri_tel
        self.musteri_adres = musteri_adres
        self.musteri_tip = musteri_tip

    def __str__(self):
        return f"Müsteri ID: {self.musteri_id}, Müsteri Ad: {self.musteri_ad}, Müsteri Soyad: {self.musteri_soyad}, Müsteri Tel: {self.musteri_tel}, Müsteri Adres: {self.musteri_adres}, Müsteri Tip: {self.musteri_tip}"

class BireyselMüsteri(Müsteri):
    def __init__(self, musteri_id, musteri_ad, musteri_soyad, musteri_tel, musteri_adres, tc_no):
        super().__init__(musteri_id, musteri_ad, musteri_soyad, musteri_tel, musteri_adres, "Bireysel")
        self.tc_no = tc_no
    
    def __str__(self):
        return f"{super().__str__()}, TC No: {self.tc_no}"

class KurumsalMüsteri(Müsteri):
    def __init__(self, musteri_id, musteri_ad, musteri_soyad, musteri_tel, musteri_adres, sirket_adi, vergi_no):
        super().__init__(musteri_id, musteri_ad, musteri_soyad, musteri_tel, musteri_adres, "Kurumsal")
        self.sirket_adi = sirket_adi
        self.vergi_no = vergi_no
    
    def __str__(self):
        return f"{super().__str__()}, Şirket: {self.sirket_adi}, Vergi No: {self.vergi_no}"