"""
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.

    Toplam Not >=  90 -----> AA
    Toplam Not >=  85 -----> BA
    Toplam Not >=  80 -----> BB
    Toplam Not >=  75 -----> CB
    Toplam Not >=  70 -----> CC
    Toplam Not >=  65 -----> DC
    Toplam Not >=  60 -----> DD
    Toplam Not >=  55 -----> FD
    Toplam Not <  55 -----> FF
"""

vize1 = int(input("Vize1 Notunu Giriniz :"))
vize2 = int(input("Vize2 Notunu Giriniz :"))
final = int(input("Final Notunu Giriniz :"))

toplamNot = vize1 * 3/10 + vize1 * 3/10 + final * 4/10


if(toplamNot >= 90):
    print("AA")
elif(toplamNot >= 85):
    print("BA")
elif(toplamNot >= 80):
    print("BB")
elif(toplamNot >= 75):
    print("CB")
elif(toplamNot >= 70):
    print("CC")
elif(toplamNot >= 65):
    print("DC")
elif(toplamNot >= 60):
    print("DD")
elif(toplamNot >= 55):
    print("FD")
else:
    print("FF")