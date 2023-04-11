
##kitap = Kitap()  __init__ metodu
##print(kitap)  __str__ metodu
##len(kitap) ## __len__ metodu
##del kitap  __del__ metodu



class Kitap():
    """init metodu"""
    def __init__(self,isim,yazar,sayfaSayisi,tur):
        print("İnit Fonksiyonu")
        self.isim = isim
        self.yazar = yazar
        self.sayfaSayisi = sayfaSayisi
        self.tur = tur

    """str metodu"""
    def __str__(self):
        return "İsim: {}\nYazar: {}\nSayfa Sayısı: {}\nTürü: {}".format(self.isim, self.yazar, self.sayfaSayisi,
                                                                        self.tur)
    """len metodu"""
    def __len__(self):
        return self.sayfaSayisi

    """del metodu"""
    def __del__(self):
        print("Kitap objesi siliniyor.......")

kitap = Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye")
print(kitap)
print(len(kitap))
del kitap






