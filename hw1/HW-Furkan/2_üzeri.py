sayı=1
print("-1 İLE PROGRAMDAN ÇIKABİLİRSİNİZ.\n")
while sayı!='-1':
    sayı=input("LÜTFEN 2 ÜZERİ ALMAK İSTEDİĞİNİZ SAYIYI GİRİNİZ.\n")
    if sayı=='-1':
        break
    elif sayı.isdecimal()!=1 :
        print("LÜTFEN BİR İNTEGER SAYI GİRİNİZ!!!\n")
        continue

    sayı=int(sayı)
    us=1
    def hesapla(sayı,us):

        if sayı== 0:
            return us
        else :
            us =us*2
            return hesapla(sayı-1,us)

    print(hesapla(sayı,us))
print("PROGRAM KAPANDI.\n")