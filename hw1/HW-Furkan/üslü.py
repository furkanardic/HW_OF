sayı=1
taban=1
print("-1 İLE PROGRAMDAN ÇIKABİLİRSİNİZ.\n")
while taban!='0':
    taban = input("LÜTFEN TABAN SAYIYI GİRİNİZ.\n")
    sayı=input("LÜTFEN ÜS ALMAK İSTEDİĞİNİZ SAYIYI GİRİNİZ.\n")
    sayı = int(sayı)
    if taban=='0':
        break
    elif str(abs(sayı)).isdecimal()!=1 :
        print("LÜTFEN BİR DECİMAL SAYI GİRİNİZ!!!\n")
        continue
    neg=sayı
    sayı=int(sayı)
    taban=int(taban)
    sonuc=1
    def hesapla(sayı,taban,sonuc,neg):

        if sayı== 0:
            if sayı == 0 and neg < 0:
                print(sayı,taban, sonuc)
                return (1 / sonuc)
            else :
                return sonuc
        else :
            sonuc =sonuc*taban
            if sayı>=0:
                return hesapla(sayı-1,taban,sonuc,neg)
            elif sayı<0:
                return hesapla(sayı+1,taban,sonuc,neg)
    print(hesapla(sayı,taban,sonuc,neg))
print("PROGRAM KAPANDI.\n")


