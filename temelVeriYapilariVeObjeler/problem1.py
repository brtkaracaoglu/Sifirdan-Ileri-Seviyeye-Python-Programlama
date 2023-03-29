"""
Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın.
Ekrana yazdırma işlemini *format* metoduyla yapmaya çalışın.

"""

a = int(input("Birinci sayı:"))
b = int(input("İkinci sayı:"))
c = int(input("Üçüncü sayı:"))

sonuc = a * b * c

print("Sonuc : {}".format(sonuc))