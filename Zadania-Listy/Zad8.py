# -*- coding: latin-1 -*-
# Æwiczenie 8: Napisz funkcjê, która przyjmuje listê wyrazów i zwraca s³ownik, w którym kluczami bêd¹ wyrazy, a wartoœciami liczba ich wyst¹pieñ w liœcie.

def get_dictionary():
    y = []
    x = {}
    while True:
        s = input("Podaj wyrazy, które chcesz umieœciæ w skrzyni (napisz stop, aby zakoñczyæ): ")
        if s.lower() == "stop":  # lower zeby wpisanie stop bez wzgledu na wielkosc liter dzialalo
            break
        elif not s.isalpha():   # isalpha sprawdza czy wpisane sa tylko litery, stringi
            print("Mog¹ byæ tylko wyraz! Spróbuj ponownie!")
        else:
            y.append(s)

    for i in y:
        x[i] = y.count(i)

    return x

print(get_dictionary())
