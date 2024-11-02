# -*- coding: latin-1 -*-
# Utwórz s³ownik fruits z piêcioma owocami jako kluczami i ich kolorami jako wartoœciami (np. {"apple": "red"}). Nastêpnie utwórz nowy s³ownik colors z kolorami jako kluczami i owocami jako wartoœciami.

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
            swapped_dict[value].append(key)  # Dodajemy klucz do listy, jeœli wartoœæ ju¿ istnieje
        else:
            swapped_dict[value] = [key]      # Tworzymy now¹ listê z kluczem, jeœli wartoœæ jeszcze nie istnieje
    return swapped_dict

fruits = {
    "apple": "green", 
    "banana": "yellow", 
    "orange": "orange", 
    "berry": "purple", 
    "strawberry": "red", 
    "grape": "purple"  # Przyk³ad powtórzenia koloru
}

colors = swap_keys_values(fruits)
print(colors)