# -*- coding: latin-1 -*-
# SprawdŸ, czy w s³owniku person istnieje klucz name, a nastêpnie sprawdŸ, czy istnieje klucz address. Jeœli klucza nie ma, dodaj go ze stosown¹ wartoœci¹.

person = {"name": "Bartek", "age": 35, "city": "£ódŸ"}
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