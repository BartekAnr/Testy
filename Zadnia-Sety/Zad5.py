# -*- coding: latin-1 -*-
# Sprawd�, czy w s�owniku person istnieje klucz name, a nast�pnie sprawd�, czy istnieje klucz address. Je�li klucza nie ma, dodaj go ze stosown� warto�ci�.

person = {"name": "Bartek", "age": 35, "city": "��d�"}
print(person)


person["job"] = "programmer"
person["city"] = "Warszawa"
print(person)

if "name" in person:
    print("Element 'name' istnieje w slowniku")
    if "address" not in person:
        s = input("Nie ma elementu 'address' w slowniku. Dodaj element: ")
        person["address"] = s
    else:
        print("nic nie wpisales!")
else:
    print("Element name nie istnieje w slowniku!")

print(person)