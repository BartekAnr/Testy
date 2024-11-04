# -*- coding: latin-1 -*-
# Stwórz dwa zbiory i sprawdŸ, czy jeden z nich jest podzbiorem drugiego.

x = {"Anna", "Bartek", "Cecylia"}
y = {"Anna", "Bartek", "Cecylia", "Daniel"}

# Sprawdzenie, czy x jest podzbiorem y
if x.issubset(y):
    print("Zbiór x jest podzbiorem zbioru y.")
else:
    print("Zbiór x nie jest podzbiorem zbioru y.")

# Sprawdzenie, czy y jest podzbiorem x
if y.issubset(x):
    print("Zbiór y jest podzbiorem zbioru x.")
else:
    print("Zbiór y nie jest podzbiorem zbioru x.")