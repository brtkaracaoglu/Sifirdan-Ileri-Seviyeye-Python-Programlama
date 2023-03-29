"""
2. dereceden bir bilinmeyenli denklemin köklerini bulma

denklem : ax^2 + bx + c

deltayı hesaplama : b ** 2 - 4 * a * c

birinci kök : (-b - delta ** 0.5) / (2*a)
ikinci kök : (-b + delta ** 0.5) / (2*a)


"""



a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

delta = b ** 2 - 4 * a * c

x1 = (-b - delta ** 0.5) / (2*a)
x2 = (-b + delta ** 0.5) / (2*a)

print("Birinci Kök: {}\nİkinci Kök: {}\n".format(x1,x2))
