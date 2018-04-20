sayı=1
while sayı!='0':
    sayı=input("LÜTFEN FAKTÖRİYELİNİ ALMAK İSTEDİĞİNİZ SAYIYI GİRİNİZ.\n")
    if sayı=='0':
        break
    elif sayı.isdecimal()!=1 :
        print("LÜTFEN BİR İNTEGER SAYI GİRİNİZ!!!\n")
        continue

    sayı=int(sayı)
    fakt=1
    def hesapla(sayı,fakt):

        if sayı== 1:
            return fakt
        else :
            fakt =fakt*sayı
            return hesapla(sayı-1,fakt)

    print(hesapla(sayı,fakt))
print("PROGRAM KAPANDI.\n")