# Tworzymy pusty slownik, w ktorym beda zapisane imiona uczniow i ich oceny
uczniowie = {}

# Funkcja do dodawania ocen dla danego ucznia
def dodaj_oceny(imie):
    oceny = []
    while True:
        ocena = input(f"Podaj ocene dla {imie} (od 1 do 5, wpisz 'stop', aby zakonczyc oceny): ")
        if ocena == 'stop':
            break
        if ocena.isdigit() and 1 <= int(ocena) <= 5:
            oceny.append(int(ocena))
        else:
            print("Niepoprawna ocena. Wpisz liczbe od 1 do 5.")
    return oceny

# Wprowadzenie uczniow i ich ocen
while True:
    imie = input("Podaj imie ucznia (lub wpisz 'koniec' aby zakonczyc): ")
    if imie == 'koniec':
        break
    oceny = dodaj_oceny(imie)
    uczniowie[imie] = oceny

# Obliczanie srednich ocen dla kazdego ucznia
srednie_oceny = {imie: sum(oceny) / len(oceny) for imie, oceny in uczniowie.items()}

# Wyswietlenie listy uczniow i ich srednich ocen
print("\nSrednie oceny:")
for imie, srednia in srednie_oceny.items():
    print(f"{imie}: {srednia:.2f}")

# Znalezienie najwyzszej sredniej oceny
najwyzsza_srednia = max(srednie_oceny.values())

# Wyswietlenie ucznia/uczniow z najwyzsza srednia ocena
najlepsi_uczniowie = [imie for imie, srednia in srednie_oceny.items() if srednia == najwyzsza_srednia]
print("\nNajlepszy uczen/uczniowie:", ', '.join(najlepsi_uczniowie))