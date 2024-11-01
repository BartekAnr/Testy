# -*- coding: latin-1 -*-
# Wypisz wszystkie klucze i wartoœci w s³owniku person w formacie: „Klucz: Wartoœæ”.

person = {"name": "Bartek", "age": 35, "city": "£ódŸ"}
print(person)

person["job"] = "programmer"
person["city"] = "Warszawa"
print(person)

i = 1
for n, m in person.items():
    print(f"{i}. {n}: {m}")
    i+=1
