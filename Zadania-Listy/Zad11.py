# -*- coding: latin-1 -*-
# �wiczenie 10: Napisz funkcj�, kt�ra przyjmuje dwie listy liczb, zwraca jedn� list�, kt�ra jest po��czeniem obu bez duplikat�w.

def get_one_list(x, y):
    z = []
    for i in x:
        if i not in y:
            z.append(i) 
    for i in y:
        if i not in x:
            z.append(i) 
    return z

print(get_one_list([1, 2, 3, 4, 5, 6], [3, 4, 5, 6, 8, 9]))

"""

Uzycie operacji na zbiorach: "roznicy symetrycznej", i przypisanie wyniku do listy

def get_one_list(x, y):
    return list(set(x).symmetric_difference(y))

print(get_one_list([1, 2, 3, 4, 5, 6], [3, 4, 5, 6, 8, 9]))

"""