while 1:
    calisma=1
    while calisma==1:
        veri = input("Merhaba faktöryelini almak istediğiniz sayıyı giriniz:")
        try:
            sayi = int(veri)
            calisma=0
        except ValueError:
            print("Lütfen sayı giriniz!!!")
    sonuc=1
    def fonksiyon(at,sonuc):
        if (at-1)==0:
            return sonuc
        else:
            sonuc=sonuc*at
            return fonksiyon(at-1,sonuc)

    print("Cevap",fonksiyon(sayi,sonuc))