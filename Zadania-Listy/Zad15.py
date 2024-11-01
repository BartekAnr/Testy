# -*- coding: latin-1 -*-
# Æwiczenie 15: Napisz funkcjê, która przyjmuje listê s³ów i zwraca now¹ listê zawieraj¹c¹ d³ugoœci tych s³ów, u¿ywaj¹c list comprehension.

def get_sum_list():
    x = []
    
    while True:
        s = input("Podaj slowa, ktore chcesz umiescic w zbiorze (lub wpisz 'stop', aby zakonczyc): ")
        if s.lower() == 'stop':
            break
        elif not s.isalpha():
            print("Podaj tylko wyrazy!")
        else:
            x.append(s)
    print(f"Lista twoich elementow: {x}")

    y = [len(i) for i in x]
    
    return y

lenghts = get_sum_list()
print(f"Ilosc liter w poszczegolnych elementach: {lenghts}")
