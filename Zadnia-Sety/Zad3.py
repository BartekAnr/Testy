# -*- coding: latin-1 -*-
# Usuñ z s³ownika person klucz age za pomoc¹ metody pop(). SprawdŸ, co siê stanie, gdy spróbujesz usun¹æ klucz, który nie istnieje.

person = {"name": "Bartek", "age": 35, "city": "£ódŸ"}
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