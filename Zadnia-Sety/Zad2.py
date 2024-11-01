# -*- coding: latin-1 -*-
# Rozszerz s³ownik person, dodaj¹c klucz job z wartoœci¹ „programmer” i zaktualizuj wartoœæ city, aby przechowywa³a inne miasto.

person = {"name": "Bartek", "age": 35, "city": "£ódŸ"}
print(person)
person["job"] = "programmer"
person["city"] = "Warszawa"
print(person)
