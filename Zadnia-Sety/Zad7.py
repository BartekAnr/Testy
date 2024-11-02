# -*- coding: latin-1 -*-
# Utw�rz s�ownik fruits z pi�cioma owocami jako kluczami i ich kolorami jako warto�ciami (np. {"apple": "red"}). Nast�pnie utw�rz nowy s�ownik colors z kolorami jako kluczami i owocami jako warto�ciami.

fruits = {"apple": "green", "banana": "yellow", "orange": "orange", "berry": "purple", "strawberry": "red"}
print(fruits)

def swap_keys_values(dictionary):
    swapped_dict = {value: key for key, value in dictionary.items()}
    return swapped_dict

colors = swap_keys_values(fruits)
print(colors)



# Rozwiazanie w przypadku powtarzajacych sie wartosciw w pierwszym slowniku, np. koloru owocu


def swap_keys_values(dictionary):
    swapped_dict = {}
    for key, value in dictionary.items():
        if value in swapped_dict:
            swapped_dict[value].append(key)  # Dodajemy klucz do listy, je�li warto�� ju� istnieje
        else:
            swapped_dict[value] = [key]      # Tworzymy now� list� z kluczem, je�li warto�� jeszcze nie istnieje
    return swapped_dict

fruits = {
    "apple": "green", 
    "banana": "yellow", 
    "orange": "orange", 
    "berry": "purple", 
    "strawberry": "red", 
    "grape": "purple"  # Przyk�ad powt�rzenia koloru
}

colors = swap_keys_values(fruits)
print(colors)