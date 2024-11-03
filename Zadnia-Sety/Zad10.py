# -*- coding: latin-1 -*-
# Utwórz s³ownik u¿ywaj¹c defaultdict, gdzie ka¿dy nowy klucz bêdzie mia³ domyœln¹ wartoœæ 0. Wykorzystaj go do zliczenia liter w zadanym tekœcie (np. liczba wyst¹pieñ ka¿dej litery w stringu).

from collections import defaultdict
tekst = "witam w programie ktory pokazuje ile liter wystepuje w tekscie"

letters_numbers = defaultdict(int)


for i in tekst:
    if i != " ":
        letters_numbers[i.lower()] += 1
    
print(letters_numbers)