# �wiczenie 5: Stw�rz list� liczb losowych, a nast�pnie przefiltruj tylko te, kt�re s� wi�ksze ni� 50.

import random

numbers = []
for i in range(1,11):
    n = random.randint(1,130)
    numbers.append(n)

print(numbers)

new_numbers = []
for number in numbers:
    if number > 50:
        new_numbers.append(number)

print(new_numbers)




""""

import random

numbers = [random.randint(1, 130) for i in range(10)]
print(numbers)

# Filtracja przy u�yciu list comprehension
new_numbers = [number for number in numbers if number > 50]
print(new_numbers)

"""