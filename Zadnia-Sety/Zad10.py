# -*- coding: latin-1 -*-
# Utw�rz s�ownik u�ywaj�c defaultdict, gdzie ka�dy nowy klucz b�dzie mia� domy�ln� warto�� 0. Wykorzystaj go do zliczenia liter w zadanym tek�cie (np. liczba wyst�pie� ka�dej litery w stringu).

from collections import defaultdict
tekst = "witam w programie ktory pokazuje ile liter wystepuje w tekscie"

letters_numbers = defaultdict(int)


for i in tekst:
    if i != " ":
        letters_numbers[i.lower()] += 1
    
print(letters_numbers)