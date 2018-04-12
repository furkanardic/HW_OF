veri = input("Merhaba faktöryelini almak istediğiniz sayıyı giriniz:")
sayi = int(veri)
sonuc=1
def fonksiyon(at,sonuc):
    if (at-1)==0:
        return sonuc
    else:
        sonuc=sonuc*at
        return fonksiyon(at-1,sonuc)

print("Cevap",fonksiyon(sayi,sonuc))