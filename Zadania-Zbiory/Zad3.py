# -*- coding: latin-1 -*-
# Stwórz dwa zbiory, np. zawieraj¹ce imiona. PrzeprowadŸ na nich operacje: suma, przeciêcie, ró¿nica, ró¿nica symetryczna.

imiona1 = set(["Adam", "Bartek", "Pawel", "Heniek", "Jonasz", "Halina"])
imiona2 = set(["Julia", "Natalia", "Cecylia", "Agnieszka", "Halina", "Jonasz", "Adam"])

# Suma zbiorow
imiona_razem = imiona1.union(imiona2)  # mozna tez uzyc operatora |
imiona_razem2 = imiona1 | imiona2

print(imiona_razem)
print(imiona_razem2)

# Przeciecie zbiorow
imiona_wspolne = imiona1 & imiona2
imiona_wspolne2 = imiona1.intersection(imiona2) # to samo ale uzywajac metody a nie operatora &

print(imiona_wspolne)
print(imiona_wspolne2)

# Roznica zbiorow
imiona_inne = imiona1.difference(imiona2)
imiona_inne2 = imiona2.difference(imiona1)

print(imiona_inne)
print(imiona_inne2)

# Roznica symetryczna
imiona_nierazem = imiona1.symmetric_difference(imiona2)
imiona_nierazem2 = imiona2.symmetric_difference(imiona1)

print(imiona_nierazem, imiona_nierazem2)