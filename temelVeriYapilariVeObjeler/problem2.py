"""
Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)
"""

boy = float(input("Boyunuzu giriniz :"))
kilo = int(input("Kilonuzu giriniz :"))

sonuc = (kilo) / (boy * boy)

print("Beden Kitle İndeksi : {}".format(sonuc))
