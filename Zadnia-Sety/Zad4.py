# -*- coding: latin-1 -*-
# Wypisz wszystkie klucze i warto�ci w s�owniku person w formacie: �Klucz: Warto��.

person = {"name": "Bartek", "age": 35, "city": "��d�"}
print(person)

person["job"] = "programmer"
person["city"] = "Warszawa"
print(person)

i = 1
for n, m in person.items():
    print(f"{i}. {n}: {m}")
    i+=1
