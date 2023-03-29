print(""""******************************
Kullanıcı Girişi Programı
"******************************
 """)

sysKullaniciAdi = "a"
sysParola = "2"
girisHakkı = 3

while True:
    kullaniciAdi = input("Kullanıcı Adı:")
    parola = input("Parola:")
    if(kullaniciAdi != sysKullaniciAdi and parola == sysParola):
        print("Kullanıcı adınız yanlıs...")
        girisHakkı -= 1
    elif(kullaniciAdi == sysKullaniciAdi and parola != sysParola):
        print("Parola yanlış..")
        girisHakkı -= 1
    elif (kullaniciAdi != sysKullaniciAdi and parola != sysParola):
        print("Kullanıcı adınız ve Parola yanlış..")
        girisHakkı -= 1
    else:
        print("Siisteme başarıyla giriş yapıldı")
        break
    if(girisHakkı == 0):
        print("Giriiş hakkınız bitt")
        break




