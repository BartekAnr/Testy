# -*- coding: latin-1 -*-
# Æwiczenie 9: Stwórz listê losowych liczb od 1 do 10 i zlicz, ile razy ka¿da liczba siê powtarza.

import random

numbers = [random.randint(1, 10) for _ in range(10)]
print(numbers)

each_number = {}
for number in numbers:
    each_number[number] = numbers.count(number)

print(each_number)

"""

Wykorzystanie modulu Counter do zliczania liczby wystapien elementu!

import random
from collections import Counter

numbers = [random.randint(1, 10) for _ in range(10)]
print(numbers)

each_number = dict(Counter(numbers))
print(each_number)

"""