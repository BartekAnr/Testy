# -*- coding: latin-1 -*-
# �wiczenie 15: Napisz funkcj�, kt�ra przyjmuje list� s��w i zwraca now� list� zawieraj�c� d�ugo�ci tych s��w, u�ywaj�c list comprehension.

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
