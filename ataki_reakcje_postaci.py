class Postac:
    def __init__(self, nazwa, zdrowie, pancerz, ulti, bron="podstawowa bron"):
        self.nazwa = nazwa
        self.zdrowie = zdrowie
        self.pancerz = pancerz if pancerz else 0  # Ustaw pancerz na 0, jesli brak wartosci
        self.bron = bron
        self.ulti = ulti

    def atak(self, obrazenia):
        # Dostosowanie obrazen na podstawie broni
        if self.bron == "Topor":
            obrazenia += obrazenia * 0.1
        elif self.bron == "Rozdzka":
            obrazenia += 5

        # Uwzglednienie pancerza
        if obrazenia > self.pancerz:
            obrazenia -= self.pancerz
        else:
            obrazenia = 0

        self.zdrowie -= obrazenia
        print(f"Postac {self.nazwa} otrzymala {obrazenia} obrazen. Pozostalo jej {self.zdrowie} zdrowia.")

    def atak_specjalny(self, obronca):
        if self.ulti == "Przelamanie":
            obronca.pancerz = 0
            print(f"Postac {obronca.nazwa} zostala zaatakowana umiejetnoscia specjalna {self.ulti}. Pancerz zostal calkowicie zdjety!")
        elif self.ulti == "Piorun":
            obronca.zdrowie -= 20
            print(f"Postac {obronca.nazwa} zostala zaatakowana umiejetnoscia specjalna {self.ulti}. Pozbawiono dodatkowych 20 punktow zycia!")
        else:
            print("Brak umiejetnosci specjalnej lub nie uzyto jej.")

    def czy_zyje(self):
        return self.zdrowie > 0

    def lecz(self, punkty_leczenia):
        self.zdrowie += punkty_leczenia
        if self.zdrowie > 100:
            self.zdrowie = 100
        print(f"Postac {self.nazwa} zostala wyleczona. Aktualne zdrowie: {self.zdrowie}.")

def wykonaj_atak(atakujacy, obronca, obrazenia, specjalny=False):
    print(f"{atakujacy.nazwa} atakuje {obronca.nazwa} za pomoca {atakujacy.bron}!")
    obronca.atak(obrazenia)

    # Wywolanie ataku specjalnego tylko, jesli zaznaczono
    if specjalny:
        atakujacy.atak_specjalny(obronca)

    # Sprawdzenie, czy obronca nadal zyje
    if not obronca.czy_zyje():
        print(f"Postac {obronca.nazwa} zostala pokonana!")

# Przyklady uzycia
postac1 = Postac("Wojownik", 100, 20, "Przelamanie", "Topor")
postac2 = Postac("Czarodziej", 80, 5, "Piorun", "Rozdzka")
postac3 = Postac("Lowca", 90, 15, None)

wykonaj_atak(postac1, postac2, 30, specjalny=True)
wykonaj_atak(postac2, postac1, 50)
postac1.lecz(20)
wykonaj_atak(postac3, postac2, 30)
wykonaj_atak(postac2, postac3, 20, specjalny=True)
postac3.lecz(30)
postac1.lecz(20)
wykonaj_atak(postac1, postac3, 50)
wykonaj_atak(postac3, postac1, 40)
