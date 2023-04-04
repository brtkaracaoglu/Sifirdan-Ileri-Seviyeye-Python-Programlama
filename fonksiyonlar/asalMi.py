"""
Asal Sayılar : 1'e ve kendisinden başka sayıya bölünmeyen sayılardır.
"""
def asalMi(sayi):
    if(sayi == 1):
        return False
    elif(sayi == 2):
        return True
    else:
        for i in range(2,sayi):
            if(sayi % i == 0):
                return False
        return True

while True:
    sayi = input("Sayi:")

    if(sayi == "q"):
        print("Programdan çıktınız.")
        break
    else:
        sayi = int(sayi)

        if(asalMi(sayi)):
            print(sayi,"asal bir sayidir.")
        else:
            print(sayi,"asal bir sayı değildir.")














