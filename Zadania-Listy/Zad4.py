# �wiczenie 4: Napisz funkcj�, kt�ra zwr�ci wszystkie liczby parzyste z listy liczb podanej jako argument.

def try_even(x):
    y = []
    for i in x:
        if i % 2 == 0:
            y.append(i)
    return y

print(try_even([2, 4, 5, 6, 7, 8, 9]))