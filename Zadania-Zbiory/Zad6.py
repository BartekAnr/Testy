# -*- coding: latin-1 -*-
# Stw�rz dwa zbiory i sprawd�, czy jeden z nich jest podzbiorem drugiego.

x = {"Anna", "Bartek", "Cecylia"}
y = {"Anna", "Bartek", "Cecylia", "Daniel"}

# Sprawdzenie, czy x jest podzbiorem y
if x.issubset(y):
    print("Zbi�r x jest podzbiorem zbioru y.")
else:
    print("Zbi�r x nie jest podzbiorem zbioru y.")

# Sprawdzenie, czy y jest podzbiorem x
if y.issubset(x):
    print("Zbi�r y jest podzbiorem zbioru x.")
else:
    print("Zbi�r y nie jest podzbiorem zbioru x.")