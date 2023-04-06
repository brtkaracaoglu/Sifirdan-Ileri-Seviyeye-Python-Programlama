class Calisan():

    def __init__(self,isim,maas,departman):
        print("Çalışan sınıfının init foksiyonu")

        self.isim = isim
        self.maas = maas
        self.departman = departman
    def bilgileriGoster(self):
        print("Çalışan sınıfının bilgileri.....")

        print("İsim : {} \nMaaş : {} \nDepartman: {}\n ".format(self.isim,self.maas,self.departman))

    def departmanDegistir(self,yeniDepartman):
        self.departman = yeniDepartman


class Yonetici(Calisan):
    def zamYap(self,zamMiktari):
        self.maas += zamMiktari

yonetici = Yonetici("Berat Karacaoğlu",5000,"Bilişim")
print(yonetici)
print(yonetici.bilgileriGoster())
print(yonetici.departmanDegistir("İnsan Kaynakları"))
print(yonetici.bilgileriGoster())
yonetici = Yonetici("Arya Karacaoğlu",7000,"Pazarlama")

print(yonetici)
print(yonetici.zamYap(500))
print(yonetici.bilgileriGoster())


"""Overriding"""

class Calisan():

    def __init__(self,isim,maas,departman):
        print("Çalışan sınıfının init foksiyonu")

        self.isim = isim
        self.maas = maas
        self.departman = departman
    def bilgileriGoster(self):
        print("Çalışan sınıfının bilgileri.....")

        print("İsim : {} \nMaaş : {} \nDepartman: {}\n ".format(self.isim,self.maas,self.departman))

    def departmanDegistir(self,yeniDepartman):
        self.departman = yeniDepartman


class Yonetici(Calisan):
    def __init__(self,isim,maas,departman,kisiSayisi):
        print("Yönetici sınıfının init foksiyonu")

        self.isim = isim
        self.maas = maas
        self.departman = departman
        self.kisiSayisi = kisiSayisi

    def bilgileriGoster(self):
            print("Yönetici sınıfının bilgileri.....")

            print("İsim : {} \nMaaş : {} \nDepartman: {} \nKişi Sayısı : {} ".format(self.isim, self.maas, self.departman,self.kisiSayisi ))
    def zamYap(self,zamMiktari):
        self.maas += zamMiktari

yonetici = Yonetici("Oğuz Alp",4500,"Bilişim",10)
print(yonetici)
print(yonetici.bilgileriGoster())


"""Süper anahtar kelimesi"""
class Calisan():

    def __init__(self,isim,maas,departman):
        print("Çalışan sınıfının init foksiyonu")

        self.isim = isim
        self.maas = maas
        self.departman = departman
    def bilgileriGoster(self):
        print("Çalışan sınıfının bilgileri.....")

        print("İsim : {} \nMaaş : {} \nDepartman: {}\n ".format(self.isim,self.maas,self.departman))

    def departmanDegistir(self,yeniDepartman):
        self.departman = yeniDepartman


class Yonetici(Calisan):
    def __init__(self,isim,maas,departman,kisiSayisi):
        super().__init__(isim,maas,departman)
        print("Yönetici sınıfının init foksiyonu")

        self.kisiSayisi = kisiSayisi

    def bilgileriGoster(self):
            print("Yönetici sınıfının bilgileri.....")

            print("İsim : {} \nMaaş : {} \nDepartman: {} \nKişi Sayısı : {} ".format(self.isim, self.maas, self.departman,self.kisiSayisi ))
    def zamYap(self,zamMiktari):
        self.maas += zamMiktari

yonetici = Yonetici("Ahmet Kaya",8500,"Bilişim",5)
print(yonetici)
print(yonetici.bilgileriGoster())

