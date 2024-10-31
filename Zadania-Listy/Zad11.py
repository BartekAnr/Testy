# -*- coding: latin-1 -*-
# �wiczenie 11: Utw�rz list� losowych liczb, a nast�pnie przekszta�� j�, pozostawiaj�c tylko liczby niepowtarzaj�ce si�.
import random

# Generowanie listy z losowymi liczbami
numbers = [random.randint(1, 20) for _ in range(20)]
print("Original list:", numbers)

# Zliczanie wyst�pie� ka�dej liczby
count_dict = {}
for number in numbers:
    count_dict[number] = count_dict.get(number, 0) + 1

# Tworzenie nowej listy tylko z liczbami wyst�puj�cymi jeden raz
unique_numbers = [number for number in numbers if count_dict[number] == 1]

print("List without duplicates:", unique_numbers)