while 1:
    calisma = 1
    while calisma ==1:
        print("Bu program girdiğiniz sayıyı 2 nin kuvveti şeklinde alır.\n")
        veri = input("Lütfen bir tam sayı giriniz:")
        try:
            sayi = int(veri)
            calisma = 0
        except ValueError:
            print("lütfen bir tam sayı giriniz!!!")
        helper = 2
        def işlem(at,helper):
            if(at == 0):
                helper = 1
                return helper
            elif(at ==1):
                return helper
            else:
                helper = helper*2
                at=at-1
                return işlem(at,helper)
        print("Sonuç:",işlem(sayi,helper))