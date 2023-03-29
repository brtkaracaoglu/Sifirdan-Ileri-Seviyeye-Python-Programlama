"""
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın
ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.


"""
km = int(input("Kaç km yol gittiniz :"))
yakit = float(input("Km'de araç ne kadar yakıyor :"))

sonuc = km * yakit

print("Tutar : {} tl".format(sonuc))