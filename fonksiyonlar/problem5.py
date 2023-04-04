"""
1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları
ekrana yazdıran bir fonksiyon yazın.(a <= 100,b <= 100)
"""

def pisagorBulma():

    pisagorListesi = list()
    for i in range(1,101):
        for j in range(1,101):

            c = (i ** 2 + j ** 2) ** 0.5

            if (c == int(c)):
                pisagorListesi.append((i,j,int(c)))

    return pisagorListesi

for i in pisagorBulma():
    print(i)