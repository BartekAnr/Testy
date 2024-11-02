# -*- coding: latin-1 -*-
# Utwórz s³ownik students przechowuj¹cy informacje o trzech studentach. Ka¿dy student powinien mieæ przypisane imiê, wiek i listê przedmiotów, które uczêszcza. Wypisz przedmioty, które ma trzeci student.

students = {
    "John": {
        "age": 21,
        "lessons": ["Basic python", "English", "Filozofy", "IT for marketing", "History of science"]
    },
    "Bill": {
        "age": 20,
        "lessons": ["Mathematic", "Filozofy", "Physics", "Deep Learning"]
    },
    "Mark": {
        "age": 22,
        "lessons": ["History of Europe", "Geographic", "Geopolitics", "History"]
    }
}

# Wyœwietlenie przedmiotów trzeciego studenta (Mark)
print(students["Mark"]["lessons"])
