# �wiczenie 3: Napisz funkcj�, kt�ra przyjmuje list� liczb oraz dodaje do niej liczb� tylko, je�li nie znajduje si� ju� na li�cie.

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