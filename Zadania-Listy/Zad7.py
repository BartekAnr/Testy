# Cwiczenie 7: Posortuj liste liczb w porzadku rosnacym i malejacym. Nastepnie posortuj liste tekstow w porzadku alfabetycznym.

import random

numbers = [random.randint(1, 200) for i in range(10)]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

texts = ["Bukareszt", "Napalm", "Historia", "Renji", "Taekwondo", "Zenobia", "Yeti", "Huligan", "Motloch", "Analfabeta", "Gruszka", "Cyborg", "Pejzaz", "Lista"]
texts.sort()
print(texts)


"""

W numerach mozna zrobic tak:

numbers = [random.randint(1, 200) for _ in range(10)]
numbers.sort(reverse=True)  -   posortuje od razu od tylu
print(numbers)

"""