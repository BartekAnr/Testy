# Æwiczenie 2: Utwórz listê numerów od 1 do 10, a nastêpnie dodaj do niej kilka liczb, usuñ parzyste liczby, a na koniec pomnó¿ ka¿d¹ liczbê przez 2.

numbers = list(range(1,11))

print(numbers)
numbers.append(14)
numbers.extend([24, 35, 42, 51])
print(numbers)

numbers = [number for number in numbers if number % 2 != 0]

print(numbers)

numbers = [number * 2 for number in numbers]

print(numbers)