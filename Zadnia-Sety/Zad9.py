# -*- coding: latin-1 -*-
# Utw�rz drugi s�ownik z dodatkowymi informacjami o osobie, np. {"hobby": "cycling", "language": "English"} i u�yj metody, aby doda� te informacje do s�ownika person.

person = {"name": "Bartek", "age": 35, "city": "��d�"}
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