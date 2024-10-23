# Stworzenie listy produktow w slowniku
produkty = {"Chleb": 3.50, "Mleko": 4.50, "Maslo": 6.00, "Jajka": 8.00, "Ser": 5.50}

# Wydrukowanie listy dostepnych produktow
print("Dostepne produkty:")
i = 1
for produkt, cena in produkty.items():
    print(f"{i}. {produkt} {cena:.2f} zl")
    i += 1

# Stworzenie koszyka do robienia zakupow
koszyk = []

# Wybieranie produktow do koszyka ze listy produktow
while True:
    zakup = input("Wybierz produk, ktory chcesz kupic (lub wpisz 'koniec', aby zakonczyc robie zakupow): ")
    if zakup == 'koniec':
        break
    elif zakup in produkty.keys():
        koszyk.append(zakup)
    else:
        print("Wybierz tylko dostepne produkty!")

print(f"Produkty w koszyku: {koszyk}")

# Podliczenie calkowitej ceny koszyka oraz najdrozszego i najtanszego produktu
suma = sum(produkty[produkt] for produkt in koszyk)
print(f"Laczny koszt: {suma:.2f} zl")

najdrozszy_produkt = max(koszyk, key = lambda produkt: produkty[produkt])
print(f"Najdrozszy produkt: {najdrozszy_produkt}")

najtanszy_produkt = min(koszyk, key = lambda produkt: produkty[produkt])
print(f"Najtanszy produkt: {najtanszy_produkt}")



"""
UWAGA!
By dodatkowo sprawdzic czy koszyk nie jest pusty:

if koszyk:
    print(f"\nProdukty w koszyku: {koszyk}")

    # Podliczenie ca³kowitej ceny koszyka oraz najdro¿szego i najtañszego produktu
    suma = sum(produkty[produkt] for produkt in koszyk)
    print(f"£¹czny koszt: {suma:.2f} z³")

    najdrozszy_produkt = max(koszyk, key=lambda produkt: produkty[produkt])
    print(f"Najdro¿szy produkt: {najdrozszy_produkt} - {produkty[najdrozszy_produkt]:.2f} z³")

    najtanszy_produkt = min(koszyk, key=lambda produkt: produkty[produkt])
    print(f"Najtañszy produkt: {najtanszy_produkt} - {produkty[najtanszy_produkt]:.2f} z³")
else:
    print("Twój koszyk jest pusty.")
"""