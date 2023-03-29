print("""************************************
Kullanıcı Girişi
************************************""")

sysKullaniciAdi = "Berat"
sysParola = "12345"

kullaniciAdi = input("Kullanıcı Adı :")
parola = input("Parola :")

if (kullaniciAdi == sysKullaniciAdi and sysParola != parola):
    print("Parolanız Hatalı...")
elif (kullaniciAdi != sysKullaniciAdi and sysParola == parola):
    print("Kullanıcı Adınız Hatalı...")
elif (kullaniciAdi != sysKullaniciAdi and sysParola != parola):
    print("Kullanıcı Adınız ve Parolanız Hatalı...")
else:
    print("Sisteme Başarıyla Giriş Yapıldı...")

