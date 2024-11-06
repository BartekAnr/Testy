# -*- coding: latin-1 -*-
# Stwórz trzy zbiory i znajdŸ elementy wspólne dla wszystkich trzech zbiorów, elementy unikalne w ka¿dym zbiorze i te, które nale¿¹ do przynajmniej jednego z nich.
from itertools import chain
from collections import Counter

one =set([1, 3, 5, 7, 8])
two = set([1, 4, 6, 7, 9])
three = set([1, 2, 6, 7, 8])
print(f"First set: {one}, Second set: {two}, Third set: {three}")

same = one & two & three
print(f"Same elements in each set: {same}")

unics1 = one.difference(two | three)
unics2 = two.difference(one | three)
unics3 = three.difference(one | two)

# allunics = [k for k, v in Counter(chain(one, two, three)).items() if v==1]  - # prostsza metoda znalezienia uniklanych elementow w kazdym zbiorze ale ujetych w jednej liscie (ktora potem mozna przeksztalcic w zbior). Podobnie tê metodê mo¿na zastosowaæ w sumie wszystkich zbiorow by ja splaszczyc to jednej i wyciagnac z niej elementy wspolne

print(f"Unics elements for first set: {unics1},\nUnics elements for second set: {unics2}\nUnics elements for thirs set: {unics3}")

symetric = [k for k, v in Counter(chain(one, two, three)).items() if v>1]
print(f"Symetric difference in each set: {symetric}")