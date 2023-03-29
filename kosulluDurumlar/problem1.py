"""
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve
şu kurallara göre ekrana şu yazıları yazdırın.

 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez
"""

boy = float(input("Boyunuzu kaç yazınız :"))
kilo = int(input("Kilonuz kaç yazınız :"))

bedenKitleİndexsi = (kilo / (boy ** 2))
print("Beden Kitle İndeksi {}".format(bedenKitleİndexsi))

if (bedenKitleİndexsi < 18.5):
    print("Zayıf")
elif (bedenKitleİndexsi >= 18.5 and bedenKitleİndexsi < 25):
    print("Normal")
elif (bedenKitleİndexsi >= 25 and bedenKitleİndexsi <= 30):
    print("Fazla Kilolu")
else:
    print("Obez")