# -*- coding: latin-1 -*-
# Utw�rz s�ownik students przechowuj�cy informacje o trzech studentach. Ka�dy student powinien mie� przypisane imi�, wiek i list� przedmiot�w, kt�re ucz�szcza. Wypisz przedmioty, kt�re ma trzeci student.

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

# Wy�wietlenie przedmiot�w trzeciego studenta (Mark)
print(students["Mark"]["lessons"])
