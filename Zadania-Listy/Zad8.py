# -*- coding: latin-1 -*-
# �wiczenie 8: Napisz funkcj�, kt�ra przyjmuje list� wyraz�w i zwraca s�ownik, w kt�rym kluczami b�d� wyrazy, a warto�ciami liczba ich wyst�pie� w li�cie.

def get_dictionary():
    y = []
    x = {}
    while True:
        s = input("Podaj wyrazy, kt�re chcesz umie�ci� w skrzyni (napisz stop, aby zako�czy�): ")
        if s.lower() == "stop":  # lower zeby wpisanie stop bez wzgledu na wielkosc liter dzialalo
            break
        elif not s.isalpha():   # isalpha sprawdza czy wpisane sa tylko litery, stringi
            print("Mog� by� tylko wyraz! Spr�buj ponownie!")
        else:
            y.append(s)

    for i in y:
        x[i] = y.count(i)

    return x

print(get_dictionary())
