print(""""******************************
Atm Makinesi Hoşgeldiniz

1. Bakiye Sorgulama
2. Para Yatırma
3. Para Çekme
Programdan çıkmak için 'q' ya basın.
"******************************
 """)



bakiye = 1000

while True:
    islem = input("İşlemi Seçiniz:")

    if(islem == "q"):
        print("Yine bekleriz.")
        break
    elif(islem == "1"):
        print("Bakiyeniz {} tl dir. ".format(bakiye))
    elif(islem == "2"):
        miktar = int(input("Yatırmak istediğiniz miktarı giriniz."))
        bakiye +=miktar
        print("Şuanki bakiyeniz {} tl dir.".format(bakiye))
    elif(islem == "3"):
        miktar = int(input("Çekmek istediğiniz miktarı giriniz."))
        if(bakiye - miktar < 0 ):
            print("Böyle bir miktar çekemezsiniz.")
            continue
        bakiye -= miktar
        print("Şuanki bakiyeniz {} tl dir.".format(bakiye))
    else:
        print("Geçersiz İşlem..")

