# -*- coding: latin-1 -*-
# Napisz funkcj�, kt�ra przyjmuje dwie listy i zwraca True, je�li zawieraj� te same unikalne elementy, bez wzgl�du na kolejno�� i liczb� wyst�pie�.

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
