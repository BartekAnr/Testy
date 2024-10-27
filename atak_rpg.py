

def atak(nazwa_postaci, obrazenia, pancerz_przeciwnika = 0):
    if obrazenia < pancerz_przeciwnika:
        obrazenia = 0
    else:
        obrazenia = obrazenia - pancerz_przeciwnika
    return (f"Postac {nazwa_postaci} zadal {obrazenia} punktow obrazen przeciwnikowi!")

atak("Wojownik", 50, 20)
atak("Lucznik", 20, 40)
