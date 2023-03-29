"""
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;
"""

geometrikSekil = input("Üçgen mi? Dörtgen mi? hangisini istiyorsunuz seçiniz :")

if(geometrikSekil == "Dörtgen"):
    print("lütfen kenarları sırası ile giriniz :")
    a = int(input("1 Kenar :"))
    b = int(input("2 Kenar :"))
    c = int(input("3 Kenar :"))
    d = int(input("4 Kenar :"))
    if(a == b and a == c and a == d):
        print("Kare")
    elif(a == c and b == d):
        print("Dikdortgen")
    else:
        print("Dörtgen")
elif(geometrikSekil == "Üçgen"):
    a = int(input("1 Kenar :"))
    b = int(input("2 Kenar :"))
    c = int(input("3 Kenar :"))
    if(abs(a+b) > c and abs(a+c) > b and abs(b+c) > a):
        if (a == b and a == c):
            print("Eşkanar üçgen")
        elif((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("İkizkenar üçgen")
        else:
            print("Çeşitkenar üçgen")
    else:
        print("Üçgen belirtmiyor")
else:
    print("Geçersiz sekil")
