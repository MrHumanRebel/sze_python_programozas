#Az edges lista kitalált személyekből képezett párokat tartalmaz.
#Egy pár azt jelenti, hogy az adott személyek ismeri egymást.
#Készíts függvényt, amely egy adott, ilyen felépítésű listára meghatározza azt a 2 személyt,
# akiknek a legtöbb közös ismerősük van! Ha több ilyen személypár is lenne,
# akkor az egyik ilyen pár legyen az eredmény! Hívd meg a függvényt az edges listára
# és írd ki a kapott eredményeket!

edges = [
    ("Adél", "Dezső"), ("Géza", "Mihály"), ("Károly", "Adél"), ("Antal", "Mihály"), ("Károly", "Sára"),
    ("Mihály", "Vilma"), ("Dezső", "Vilma"), ("Vilma", "Antal"), ("Károly", "Mihály"), ("Elvira", "Adél"),
    ("Izabella", "Adél"), ("Mihály", "Izabella"), ("Géza", "Vilma"), ("Károly", "Elvira"), ("Elvira", "Mihály"),
    ("Géza", "Dezső"), ("Sára", "Adél"), ("Géza", "Adél"), ("Géza", "Izabella"), ("Izabella", "Dezső")
]

from collections import defaultdict
from itertools import combinations

#Ismerősök halmaza személyenként.
ismerosok = defaultdict(set)
for x,y in edges:
    ismerosok[x].add(y)
    ismerosok[y].add(x)

#Közös ismerősök száma minden párra.
kozosismerosok = [(len(ismerosok[x] & ismerosok[y]), x,y) for x,y in combinations(ismerosok, 2)]
print(max(kozosismerosok))
