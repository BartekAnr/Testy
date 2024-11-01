# -*- coding: latin-1 -*-
# Æwiczenie 13: Wygeneruj listê kwadratów liczb od 1 do 10 przy u¿yciu zrozumienia listy.

numbers = list(range(1,11))
print(numbers)
numbers = [number ** 2 for number in numbers ]
print(numbers)