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