"""
Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.
"""

say1 = int(input("Birinci Sayıyı Giriniz :"))
say2 = int(input("İkinci Sayıyı Giriniz :"))
say3 = int(input("Üçüncü Sayıyı Giriniz :"))

enBüyükSay = say3

if(enBüyükSay < say1):
    print("Birinci sayı en büyüktür.")
elif(enBüyükSay < say2):
    print("İkinci sayı en büyüktür.")
else:
    print("Üçüncü sayı en büyüktür.")