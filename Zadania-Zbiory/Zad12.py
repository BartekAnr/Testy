# -*- coding: latin-1 -*-
# Napisz funkcjê, która przyjmuje dwie listy i zwraca True, jeœli zawieraj¹ te same unikalne elementy, bez wzglêdu na kolejnoœæ i liczbê wyst¹pieñ.

def check_list():
    a = [1, 2, 2, 3, 4, 4, 5, 5]
    b = [1, 6, 6, 3, 4, 7, 7, 2]
    set_a = set(a)
    set_b = set(b)
    c = set_a & set_b
    if c:
        print(c)
        return True
    else:
        return False

same = check_list()
print(same)
