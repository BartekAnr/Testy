# -*- coding: latin-1 -*-
# Maj¹c listê liczb, stwórz zbiór zawieraj¹cy tylko te liczby, które s¹ wiêksze od 10.

numbers = [12, 222, 4, 56, 3, 67, 10, 11, 43, 1, 0, 65, 203, 148, 5]

unics = set([i for i in numbers if i > 10])
print(unics)