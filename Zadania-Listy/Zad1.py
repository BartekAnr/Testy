# �wiczenie 1: Stw�rz list� ulubionych owoc�w, dodaj kilka nowych element�w, usu� wybrany owoc i zamie� jeden z owoc�w na inny.


best_fruits = ["Truskawka", "Arbuz", "Pozeczka", "Malina"]

best_fruits.append("Jablko")
best_fruits.append("Banan")
print(best_fruits)
best_fruits.remove("Banan")
print(best_fruits)
best_fruits[3] = "Poziomka"
print(best_fruits)