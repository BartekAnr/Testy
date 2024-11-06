# -*- coding: latin-1 -*-
# Stwórz dwie listy, a nastêpnie u¿yj zbiorów, aby znaleŸæ elementy, które wystêpuj¹ w obu listach.

first_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
second_list = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

first_set = set(first_list)
second_set = set(second_list)

print(first_set)
print(second_set)

twins = first_set.intersection(second_set)
print(twins)