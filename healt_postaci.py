class Postac:
    def __init__(self, nazwa, zdrowie, pancerz):
        self.nazwa = nazwa
        self.zdrowie = zdrowie
        self.pancerz = pancerz

    def atak(self, obrazenia):
        if obrazenia > self.pancerz:
            obrazenia -= self.pancerz
        else:
            obrazenia = 0
        
        self.zdrowie -= obrazenia
        print(f"Postac {self.nazwa} otrzymala {obrazenia} obrazen. Pozostalo jej {self.zdrowie} zdrowia.")

    def czy_zyje(self):
        return self.zdrowie > 0

    def lecz(self, punkty_leczenia):
        self.zdrowie += punkty_leczenia
        if self.zdrowie > 100:  # Przyjmujemy, ze maksymalne zdrowie wynosi 100
            self.zdrowie = 100
        print(f"Postac {self.nazwa} zostala wyleczona. Aktualne zdrowie: {self.zdrowie}.")

def wykonaj_atak(atakujacy, obronca, obrazenia):
    print(f"{atakujacy.nazwa} atakuje {obronca.nazwa}!")
    obronca.atak(obrazenia)
    
    if not obronca.czy_zyje():
        print(f"Postac {obronca.nazwa} zostala pokonana!")

# Przyklady uzycia
postac1 = Postac("Wojownik", 100, 20)
postac2 = Postac("Czarodziej", 80, 5)

wykonaj_atak(postac1, postac2, 30)
wykonaj_atak(postac2, postac1, 50)
postac1.lecz(20)