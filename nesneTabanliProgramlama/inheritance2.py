class Kullanici():

    def __init__(self,adi,soyadi,numara):
        print("Kullanıcı sınıfı fonksiyonu")
        self.adi = adi
        self.soyadi = soyadi
        self.numara = numara

    def bilgileriGoster(self):
        print("Kullanıcı sınıfının bilgileri")

        print("Adi: {}\nSoyadi: {}\nNumara: {}".format(self.adi,self.soyadi,self.numara))


class Akedemisyen(Kullanici):
    pass


##Overriding
class Ogrenci(Kullanici):

    def __init__(self,adi,soyadi,numara,dogumTarihi):
        print("Ögrenci sınıfı fonksiyonu")
        self.adi = adi
        self.soyadi = soyadi
        self.numara = numara
        self.dogumTarihi = dogumTarihi
    def bilgileriGoster(self):
        print("Öğrenci sınıfının bilgileri")

        print("Adi: {}\nSoyadi: {}\nNumara: {}\nDoğum Tarihi: {}".format(self.adi,self.soyadi,self.numara,self.dogumTarihi))

##Super() Türkçe karşılığı üst olan bu fonksiyon içinde bulunduğu sınıfın üst bir
# sınıftan miras alındığını ve oradaki özellikleri kullanabilmenizi sağlıyor.
class Personel(Kullanici):

    def __init__(self,adi,soyadi,numara,personelSayisi):
        super().__init__(adi,soyadi,numara)
        print("Personel sınıfı fonksiyonu")

        self.personelSayisi = personelSayisi

    def bilgileriGoster(self):
        print("Personel sınıfının bilgileri")

        print("Adi: {}\nSoyadi: {}\nNumara: {}\nPersonel Sayısı: {}".format(self.adi,self.soyadi,self.numara,self.personelSayisi))








print("Akademisyen Bilgileri")
akademisyen = Akedemisyen("Berat","Karacaoğlu",1234)
print(Akedemisyen.bilgileriGoster(akademisyen))

print("Ögrenci Bilgileri")
ogrenci = Ogrenci("Aslı","Turan",1234,2001)
print(Ogrenci.bilgileriGoster(ogrenci))

print("Personel Bilgileri")
personel = Personel("Emre","Kaya",1234,12)
print(Personel.bilgileriGoster(personel))















