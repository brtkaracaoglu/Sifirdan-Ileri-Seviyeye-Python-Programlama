import random
import time

print("""**********************************

Sayı Tahmin Oyunu

1 ile 40 arasında sayıyı tahmin edin.

**********************************""")

rastgeleSayi = random.randint(1,40)
tahminHakki = 7
while True:

     tahmin = int(input("Tahmininiz:"))

     if (tahmin < rastgeleSayi):
         print("Bilgiler Sorgulanıyor...")
         time.sleep(1)
         print("Daha yüksek bir sayı söyleyin...")
         tahminHakki -= 1

     elif (tahmin > rastgeleSayi):
         print("Bilgiler Sorgulanıyor...")
         time.sleep(1)
         print("Daha düşük bir sayı söyleyin...")
         tahminHakki -= 1
     else:
         print("Bilgiler Sorgulanıyor...")
         time.sleep(1)
         print("Tebrikler! Sayımız",rastgeleSayi)
         break

     if (tahminHakki == 0):
         print("Tahmin Hakkınız Bitti...")
         print("Sayımız:",rastgeleSayi)
         break
