# -*- coding: latin-1 -*-
# Usu� z s�ownika person klucz age za pomoc� metody pop(). Sprawd�, co si� stanie, gdy spr�bujesz usun�� klucz, kt�ry nie istnieje.

person = {"name": "Bartek", "age": 35, "city": "��d�"}
print(person)


person["job"] = "programmer"
person["city"] = "Warszawa"
print(person)


person.pop("age")

if "elements" in person:
    person.pop("elements")
else:
    print("Klucz 'elements' nie istnieje.")

print(person)