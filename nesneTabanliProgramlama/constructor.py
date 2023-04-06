class Araba():

    def __init__(self, model, renk, beygirGucu, silindir):
        print("init fonksiyon çağrıldı")
        self.model = model
        self.renk = renk
        self.beygirGucu = beygirGucu
        self.silindir = silindir

araba1 = Araba("Renault Megane","Gümüş",110,4)

araba2 = Araba("Peugeot","Beyaz",90,4)


print(araba1.renk)
print(araba2.renk)


"""objenin özellikleri oluşturuldu
ardından bilgileri gösteren bir metod oluşturuldu. oluşturulam metodun
ilk parametresi self olmak zorunda çümkü bu metodu obje üzerinde uygulanacak
herhangi bir özelliğe erişmek için uygulanması laızm"""
class Yazilimci():

    def __init__(self,isim,soyisim,numara,maas,diller):
        self.isim = isim
        self.soyisim= soyisim
        self.numara = numara
        self.maas = maas
        self.diller = diller
    def bilgileriGöster(self ):
        print("""
        Yazılımcı objesinin özellikleri
        İsim : {}
        Soyisim : {}
        Numara : {}
        Maaş : {}
        Bildiği Diller : {}
        """.format(self.isim,self.soyisim,self.numara,self.maas,self.diller))
    def zamYap(self,zamMiktar):
            print("Zam Yapılıyor..")

            self.maas += zamMiktar
    def dilEkle(self,yeniDil):
            print("Dil ekleniyor..")

            self.diller.append(yeniDil)
yazilimci = Yazilimci("Berat","Karacaoğlu",12345,5000,["Python,C#"])

print(yazilimci.bilgileriGöster())
yazilimci.dilEkle("Java")
print(yazilimci.bilgileriGöster())
yazilimci.zamYap(5000)
print(yazilimci.bilgileriGöster())