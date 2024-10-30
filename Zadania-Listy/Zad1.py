# Æwiczenie 1: Stwórz listê ulubionych owoców, dodaj kilka nowych elementów, usuñ wybrany owoc i zamieñ jeden z owoców na inny.


best_fruits = ["Truskawka", "Arbuz", "Pozeczka", "Malina"]

best_fruits.append("Jablko")
best_fruits.append("Banan")
print(best_fruits)
best_fruits.remove("Banan")
print(best_fruits)
best_fruits[3] = "Poziomka"
print(best_fruits)