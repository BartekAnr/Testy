# -*- coding: latin-* -*-
# �wiczenie 14: Stw�rz list� wszystkich liczb parzystych od 1 do 20 przy u�yciu list comprehension.

numbers = [number for number in range(1,21) if number % 2 == 0]
print(numbers)