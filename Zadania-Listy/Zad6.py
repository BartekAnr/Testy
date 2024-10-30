# Æwiczenie 6: Utwórz listê imion, a nastêpnie przefiltruj tylko te, które zaczynaj¹ siê na literê „A”.

import re

imiona = ["Bartek", "Andrzej", "Zenek", "Adrian", "Henryk", "Gucio", "Adam", "Blazej", "Adelajda"]
print(imiona)

imiona_a = [imie for imie in imiona if re.match("^A", imie)]
print(imiona_a)



"""
ZAMIAST MODULU "RE"
imiona_a = [imie for imie in imiona if imie.startswith("A")]

"""