while 1:
    calisma = 2
    while calisma == 2:
        veri = input("Üssünü almak istediğiniz tam sayıyı giriniz:")
        try:
            sayi = int(veri)
            calisma = calisma - 1
        except ValueError:
            print("lütfen bir tam sayı giriniz!!!")
        veri2 = input("Kaçıncı kuvvetini almak istediğinizi 0 ya da pozitif tam sayı olarak giriniz:")
        try:
            sayi2 = int(veri2)
            calisma = calisma - 1
        except ValueError:
            print("lütfen pozitif bir tam sayı veya 0 giriniz!!!")
        silah = 1
        def fonk(at,avrat,silah):
            if avrat == 0:
                return silah
            elif avrat<0:
                return "Lütfen pozitif bir tam sayı giriniz!!!"
            else:
                silah=silah*at
                avrat=avrat-1
                return fonk(at,avrat,silah)

        print("Sonuc:",fonk(sayi,sayi2,silah))
