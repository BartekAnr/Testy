# -*- coding: latin-1 -*-
# Stw�rz s�ownik, w kt�rym kluczami b�d� litery alfabetu, a warto�ciami b�d� zbiory zawieraj�ce s�owa zaczynaj�ce si� na dan� liter� (np. dla litery 'A' zbi�r s��w zaczynaj�cych si� na 'A').
import string

alphabet = [i for i in string.ascii_uppercase]
print(alphabet)

each_word = dict()

for letter in alphabet:
    each_word[letter] = set(["S�owa na liter�, kt�ra jest klucz"])

print(each_word)

######  Funkcja, kt�ra automatycznie przypisuje s�owa (jako warto��) do klucza w s�owniku, zaczyn�jce si� na liter�, kt�r� jest klucz:

# Litery alfabetu jako klucze
alphabet2 = [i for i in string.ascii_uppercase]
print(alphabet2)

# S�ownik z domy�ln� warto�ci� zbioru dla ka�dego klucza
each_word = {letter: set() for letter in alphabet2}

# Przyk�adowe s�owa do przypisania (dla demonstracji)
words = ["Ananas", "Banana", "Cukier", "D�b", "Ekran"]

# Wype�nianie s�ownika s�owami zgodnymi z liter� klucza
for word in words:
    first_letter = word[0].upper()
    if first_letter in each_word:
        each_word[first_letter].add(word)

print(each_word)
