import random
import time

class Kumanda():

    def __init__(self,tvDurum = "Kapalı",tvSes = 0,kanalListesi = ["Trt"],kanal = "Trt"):

        self.tvDurum =tvDurum
        self.tvSes = tvSes
        self.kanalListesi = kanalListesi
        self.kanal = kanal

    def tvAc(self):

        if (self.tvDurum == "Açık"):
            print("Televizyon Zaten Açık...")
        else:
            print("Televizyon Açılıyor...")
            self.tvDurum = "Açık"

    def tvKapat(self):

        if (self.tvDurum == "Kapalı"):
            print("Televizyon Zaten Kapalı...")
        else:
            print("Televizyon Kapatılıyor...")
            self.tvDurum = "Kapalı"

    def sesAyarlari(self):

        while True:
            cevap = input("Sesi Azalt: '<'\nSesi Artır: '>'\nÇıkış: Çıkış\n")

            if (cevap == '<'):
                if (self.tvSes != 0):

                    self.tvSes -= 1
                    print("Ses:",self.tvSes)
            elif (cevap == '>'):
                if (self.tvSes != 31):

                    self.tvSes += 1
                    print("Ses:",self.tvSes)
            else:
                print("Ses Ayarları Güncellendi...",self.tvSes)
                break

    def kanalEkle(self,kanalİsmi):

        print("Kanal Ekleniyor...")
        time.sleep(1)
        self.kanalListesi.append(kanalİsmi)
        print("Kanal Eklendi...")

    def rastgeleKanal(self):

        rastgele = random.randint(0,len(self.kanalListesi)-1)
        self.kanal = self.kanalListesi[rastgele]
        print("Şu anki Kanal:",self.kanal)

    def __len__(self):

        return len(self.kanalListesi)

    def __str__(self):

        return "Tv Durumu: {}\nTv Ses: {}\nKanal Listesi: {}\nŞu anki Kanal: {}\n".format(self.tvDurum,self.tvSes,self.kanalListesi,self.kanal)

kumanda = Kumanda()

print("""

Televizyon Uygulaması

1. Tv Aç 
2. Tv Kapat
3. Ses Ayarları
4. Kanal Ekle
5. Kanal Sayısını Öğrenme
6. Rastgele Kanala Geçme
7. Televizyon Bilgileri

Çıkmak için 'q' ya basın.

""")

while True:

    islem = input("İşlemi Seçiniz:")

    if (islem == "q"):
        print("Program Sonlandırılıyor...")
        break

    elif (islem == "1"):
        kumanda.tvAc()

    elif (islem == "2"):
        kumanda.tvKapat()

    elif (islem == "3"):
        kumanda.sesAyarlari()

    elif (islem == "4"):
        kanalİsimleri = input("Kanal İsimlerini ',' ile Ayırarak Giriniz:")

        kanalListesi = kanalİsimleri.split(",")

        for eklenecekler in kanalListesi:
            kumanda.kanalEkle(eklenecekler)

    elif (islem == "5"):
        print("Kanal Sayısı:",len(kumanda))

    elif (islem == "6"):
        kumanda.rastgeleKanal()

    elif (islem == "7"):
        print(kumanda)

    else:
        print("Geçersiz İşlem...")