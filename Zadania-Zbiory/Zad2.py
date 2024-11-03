# -*- coding: latin-1 -*-
# Stwórz pusty zbiór, dodaj do niego kilka elementów, a nastêpnie usuñ kilka z nich. SprawdŸ, jak reaguje na próbê usuniêcia elementu, który nie istnieje.

inne = "Jablko", "Arbuz", "Borowka"
owoce = set([])
owoce.add("Gruszka")
owoce.update(inne)
print(owoce)
owoce.pop()
owoce.remove("Borowka")
owoce.discard("Truskawka") # metoda ta usuwa element, ale przy braku go w zbiorze nie wyrzuca bledu i nie przerywa kodu
print(owoce)