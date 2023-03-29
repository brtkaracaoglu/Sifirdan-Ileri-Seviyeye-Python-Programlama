"""
Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.
"""
a = int(input("a:"))
b = int(input("b:"))

print("Sayılar değişmeden önce :\na : {} b :{}\n".format(a,b))

a,b = b,a

print("Sayılar değiştikten sonra :\na : {} b :{}\n".format(a,b))

