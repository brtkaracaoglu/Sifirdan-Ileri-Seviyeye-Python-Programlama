"""
Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB)
dönen bir tane fonksiyon yazın.
"""


def ebobBulma(sayi1,sayi2):
    i = 1
    ebob = 0
    while(i <= sayi1 and i <= sayi2):

        if(not(sayi1 % i) and not(sayi2 % i)):
            ebob = i
        i += 1
    return ebob
sayi1 = int(input("Sayı 1:"))
sayi2 = int(input("Sayı 2:"))

print("Ebob: ",ebobBulma(sayi1,sayi2))
