# -*- coding: latin-1 -*-
# Maj�c list� s��w, stw�rz zbi�r, kt�ry b�dzie zawiera� tylko s�owa unikalne, a nast�pnie zlicz, ile jest takich s��w.
from collections import Counter

words = ["Bartek", "Natalia", "Heniek", "Heniek", "J�zio", "J�zio", "Bodzio", "Bodzio"]
print(f"List words elements: {words}")
unics = [word for word, times in Counter(words).items() if times<=1]
unics_words = set(unics)
print(unics_words)

how_many = len(unics_words)
print(f"List words have {how_many} unics elements")