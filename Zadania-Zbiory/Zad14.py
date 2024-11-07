from itertools import chain
from collections import Counter

sentences = ["pierwsze zdanie jest zdaniem pierwszym", "drugie zdanie
jest zdaniem drugim", "trzecie zdanie natomiast jest zdaniem oczywiście
trzecim"]
a = set(sentences[0].split())
b = set(sentences[1].split())
c = set(sentences[2].split())

print(a, b, c)

unics = [k for k,v in Counter(chain(a,b,c)).items() if v==1]
same = [k for k,v in Counter(chain(a,b,c)).items() if v>=2]

print(set(unics))
print(set(same))

# czytelniejsze podejscie

from itertools import chain
from collections import Counter

# Zdania do analizy
sentences = [
    "pierwsze zdanie jest zdaniem pierwszym", 
    "drugie zdanie jest zdaniem drugim", 
    "trzecie zdanie natomiast jest zdaniem oczywiście trzecim"
]

# Podział zdań na zbiory słów
a = set(sentences[0].split())
b = set(sentences[1].split())
c = set(sentences[2].split())

# Wyświetlenie podzielonych zbiorów
print("Zbiory słów:", a, b, c)

# Zliczenie wystąpień słów w łańcuchu zbiorów
word_counts = Counter(chain(a, b, c))

# Wydzielenie unikalnych i wspólnych słów
unics = {k for k, v in word_counts.items() if v == 1}
same = {k for k, v in word_counts.items() if v >= 2}

# Wyświetlenie wyników
print("Unikalne słowa:", unics)
print("Wspólne słowa (co najmniej dwa wystąpienia):", same)