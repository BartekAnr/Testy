# -*- coding: latin-1 -*-
# Napisz funkcj�, kt�ra sprawdzi, czy wszystkie warto�ci w li�cie s� unikalne, u�ywaj�c zbior�w.

numbers = [1,2,3,4,5,6,1,2,3,4,7,6,9,0]

def check_numbers(x):
    cheking = set([item for item in x if x.count(item) <= 1])
    return cheking

print(check_numbers(numbers))

####

from collections import Counter

numbers = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 7, 6, 9, 0]

def check_numbers(x):
    # Zliczamy wyst�pienia wszystkich element�w
    count_dict = Counter(x)
    # Wybieramy tylko te elementy, kt�re wyst�puj� jeden raz
    unique_numbers = {item for item, count in count_dict.items() if count == 1}
    return unique_numbers

print(check_numbers(numbers))
