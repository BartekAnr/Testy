# -*- coding: latin-1 -*-
# Stw�rz pusty zbi�r, dodaj do niego kilka element�w, a nast�pnie usu� kilka z nich. Sprawd�, jak reaguje na pr�b� usuni�cia elementu, kt�ry nie istnieje.

inne = "Jablko", "Arbuz", "Borowka"
owoce = set([])
owoce.add("Gruszka")
owoce.update(inne)
print(owoce)
owoce.pop()
owoce.remove("Borowka")
owoce.discard("Truskawka") # metoda ta usuwa element, ale przy braku go w zbiorze nie wyrzuca bledu i nie przerywa kodu
print(owoce)