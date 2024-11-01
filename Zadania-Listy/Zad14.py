# -*- coding: latin-* -*-
# Æwiczenie 14: Stwórz listê wszystkich liczb parzystych od 1 do 20 przy u¿yciu list comprehension.

numbers = [number for number in range(1,21) if number % 2 == 0]
print(numbers)