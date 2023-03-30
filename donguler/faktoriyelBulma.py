print(""""******************************
Faktöriyel Bulma Programı

Çıkmak için q'ya basın.
"******************************
 """)

while True:
    islem = input("Sayı giriniz :")
    if(islem == "q"):
        print("Program Sonlandırılıyor.")
        break
    else:
        islem = int(islem)

        faktoriyel = 1
        for i in range(2,islem+1):
            print("Faktöriyel",faktoriyel,"i",i)
            faktoriyel *=i
        print("Faktoriyel",faktoriyel)

