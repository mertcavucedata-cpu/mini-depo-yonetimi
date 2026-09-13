class Urun:
    def __init__(self,urun_kod,ad,fiyat,stok):
        self.urun_kod = urun_kod
        self.ad = ad 
        self.fiyat = fiyat
        self.stok = stok 
    
    def bilgi_goster(self):
        return f"KOD: {self.urun_kod}, Ürün: {self.ad}, Fiyat: {self.fiyat}, Stok: {self.stok}"


class Depo:
    def __init__(self):
        self.urunler = []

    def urun_ekle(self,urun):
        self.urunler.append(urun)
        print(f"{urun.ad} depoya eklendi")

    def urunleri_listele(self):
        if not self.urunler:
            print("Depoda ürün bulunmuyor.")
            return
        print("\n--- DEPO STOK LİSTESİ ---")
        for u in self.urunler:
            print(u.bilgi_goster())

    def satis_yap(self,urun_kod,adet):
        for u in self.urunler:
            if u.urun_kod == urun_kod:
                if u.stok >= adet:
                    u.stok -= adet
                    toplam = u.fiyat * adet
                    print(f"Satış başarılı! Toplam Tutar: {toplam} TL. Kalan stok: {u.stok}")
                    return
            else:
                print(f"Yetersiz stok! Mevcut stok: {u.stok}")
                return
        print("Ürün bulunumadı.") 


depo = Depo()

while True:
    print("\n--- MİNİ DEPO YÖNETİM SİSTEMİ ---")
    print("1. Ürün Ekle")
    print("2. Ürünleri Listele")
    print("3. Satış Yap")
    print("4. Çıkış")

    secim = input("İşlem seçiniz (1-4): ")

    if secim == "1":
        u_kod = input("Ürün Kodu: ")
        ad = input("Ürün Adı: ") 
        fiyat = float(input("Fiyatı: "))
        stok = int(input("Stok miktarı: "))
        yeni_urun = Urun(u_kod,ad,fiyat,stok)
        Depo.urun_ekle(yeni_urun)
    
    elif secim == "2":
        Depo.urunleri_listele()

    elif secim == "3":
        u_kod = input("Satılacak Ürün Kod: ")
        adet = int(input("Kaç adet satılacak: "))
        Depo.satis_yap(u_kod,adet)

    elif secim == "4":
        print("Sistemden çıkılıyor...")
        break
    else:
        print("Geçersiz seçim, tekrar deneyin.")