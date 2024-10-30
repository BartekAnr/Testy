# �wiczenie 6: Utw�rz list� imion, a nast�pnie przefiltruj tylko te, kt�re zaczynaj� si� na liter� �A�.

import re

imiona = ["Bartek", "Andrzej", "Zenek", "Adrian", "Henryk", "Gucio", "Adam", "Blazej", "Adelajda"]
print(imiona)

imiona_a = [imie for imie in imiona if re.match("^A", imie)]
print(imiona_a)



"""
ZAMIAST MODULU "RE"
imiona_a = [imie for imie in imiona if imie.startswith("A")]

"""