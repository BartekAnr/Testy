# -*- coding: latin-1 -*-
# Maj¹c listê s³ów, stwórz zbiór, który bêdzie zawiera³ tylko s³owa unikalne, a nastêpnie zlicz, ile jest takich s³ów.
from collections import Counter

words = ["Bartek", "Natalia", "Heniek", "Heniek", "Józio", "Józio", "Bodzio", "Bodzio"]
print(f"List words elements: {words}")
unics = [word for word, times in Counter(words).items() if times<=1]
unics_words = set(unics)
print(unics_words)

how_many = len(unics_words)
print(f"List words have {how_many} unics elements")