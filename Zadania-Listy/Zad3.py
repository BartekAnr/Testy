# Æwiczenie 3: Napisz funkcjê, która przyjmuje listê liczb oraz dodaje do niej liczbê tylko, jeœli nie znajduje siê ju¿ na liœcie.

import random 

def take_numbers():

    rand_list = []

    for i in range(0,5):
        n = random.randint(0,200)
        rand_list.append(n)

    m = random.randint(0, 200)
    if m not in rand_list:
        rand_list.append(m)

    return rand_list

print(take_numbers())