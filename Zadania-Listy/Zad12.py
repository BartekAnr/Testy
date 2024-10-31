# -*- coding: latin-1 -*-
# �wiczenie 12: Utw�rz zagnie�d�on� list� liczb (np. [[1, 2], [3, 4], [5, 6]]), a nast�pnie napisz funkcj�, kt�ra sp�aszczy t� list�, tworz�c pojedyncz� list� wszystkich element�w.

not_sumed = [[1, 2], [3, 4], [5, 6]]

def sumed_list(x):
    y = []
    for i in not_sumed:
        y.extend(i)
    return y

print(sumed_list(not_sumed))



"""

Inne sposoby:


1. itertools.chain:

from itertools import chain

not_sumed = [[1, 2], [3, 4], [5, 6]]

def sumed_list(x):
    return list(chain.from_iterable(x))

print(sumed_list(not_sumed))



2. list comprehension:

not_sumed = [[1, 2], [3, 4], [5, 6]]

def sumed_list(x):
    return [item for sublist in x for item in sublist]

print(sumed_list(not_sumed))

"""