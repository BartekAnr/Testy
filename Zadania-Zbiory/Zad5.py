# -*- coding: latin-1 -*-
# Napisz funkcjê, która sprawdzi, czy wszystkie wartoœci w liœcie s¹ unikalne, u¿ywaj¹c zbiorów.

numbers = [1,2,3,4,5,6,1,2,3,4,7,6,9,0]

def check_numbers(x):
    cheking = set([item for item in x if x.count(item) <= 1])
    return cheking

print(check_numbers(numbers))

####

from collections import Counter

numbers = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 7, 6, 9, 0]

def check_numbers(x):
    # Zliczamy wyst¹pienia wszystkich elementów
    count_dict = Counter(x)
    # Wybieramy tylko te elementy, które wystêpuj¹ jeden raz
    unique_numbers = {item for item, count in count_dict.items() if count == 1}
    return unique_numbers

print(check_numbers(numbers))
