"""
faktöriyel
"""


def faktoriyel(sayi):
     faktoriyel = 1
     if(sayi == 0 or sayi == 1):
         print("Faktoriyel:",faktoriyel)
     else:
         while (sayi >=1):
             faktoriyel *= sayi
             sayi -=1
         print("Faktöriyel:",faktoriyel)

faktoriyel(5)