# -*- coding: latin-1 -*-
# Napisz funkcjê, która przyjmuje listê i zwraca zbiór duplikatów w tej liœcie.


# from collections import Counter

  
def get_duplicates():
    elements = []
    duplicates = set([])

    while True:
        x = input("Podaj elementy, ktore chcesz dodac do listy (lub napisz 'stop', aby zakonczyc): ")
        if x.lower() == 'stop':
            break
        elif not x.isalpha():
            print("Podaj tylko wyrazy!")
        else:
            elements.append(x)

    for element in elements:
        if elements.count(element) >= 2:
            duplicates.add(element)

    # elements_count = Counter(elements)
    # duplicates = {item for item, count in element_counts.items() if count > 1}   ---->  wydajniejszy sposob zapisu

    return duplicates

example = get_duplicates()

print(example)