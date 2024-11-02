# -*- coding: latin-1 -*-
# Utwórz drugi s³ownik z dodatkowymi informacjami o osobie, np. {"hobby": "cycling", "language": "English"} i u¿yj metody, aby dodaæ te informacje do s³ownika person.

person = {"name": "Bartek", "age": 35, "city": "£ódŸ"}
print(person)

person["job"] = "programmer"
person["city"] = "Warszawa"
print(person)


description = {"hobby": "cycling", "language": "English"}
person.update(description)

print(person)

i = 1
for n, m in person.items():
    print(f"{i}. {n}: {m}")
    i+=1