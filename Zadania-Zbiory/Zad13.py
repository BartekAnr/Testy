# -*- coding: latin-1 -*-
# Stwórz s³ownik, w którym kluczami bêd¹ litery alfabetu, a wartoœciami bêd¹ zbiory zawieraj¹ce s³owa zaczynaj¹ce siê na dan¹ literê (np. dla litery 'A' zbiór s³ów zaczynaj¹cych siê na 'A').
import string

alphabet = [i for i in string.ascii_uppercase]
print(alphabet)

each_word = dict()

for letter in alphabet:
    each_word[letter] = set(["S³owa na literê, która jest klucz"])

print(each_word)

######  Funkcja, która automatycznie przypisuje s³owa (jako wartoœæ) do klucza w s³owniku, zaczyn¹jce siê na literê, któr¹ jest klucz:

# Litery alfabetu jako klucze
alphabet2 = [i for i in string.ascii_uppercase]
print(alphabet2)

# S³ownik z domyœln¹ wartoœci¹ zbioru dla ka¿dego klucza
each_word = {letter: set() for letter in alphabet2}

# Przyk³adowe s³owa do przypisania (dla demonstracji)
words = ["Ananas", "Banana", "Cukier", "D¹b", "Ekran"]

# Wype³nianie s³ownika s³owami zgodnymi z liter¹ klucza
for word in words:
    first_letter = word[0].upper()
    if first_letter in each_word:
        each_word[first_letter].add(word)

print(each_word)
