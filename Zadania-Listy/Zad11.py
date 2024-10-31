# -*- coding: latin-1 -*-
# Æwiczenie 11: Utwórz listê losowych liczb, a nastêpnie przekszta³æ j¹, pozostawiaj¹c tylko liczby niepowtarzaj¹ce siê.
import random

# Generowanie listy z losowymi liczbami
numbers = [random.randint(1, 20) for _ in range(20)]
print("Original list:", numbers)

# Zliczanie wyst¹pieñ ka¿dej liczby
count_dict = {}
for number in numbers:
    count_dict[number] = count_dict.get(number, 0) + 1

# Tworzenie nowej listy tylko z liczbami wystêpuj¹cymi jeden raz
unique_numbers = [number for number in numbers if count_dict[number] == 1]

print("List without duplicates:", unique_numbers)