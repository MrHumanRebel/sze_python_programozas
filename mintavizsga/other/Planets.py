#A planets lista a Naprendszer bolygóinak tömegét és (átlagos) sugarát tartalmazza.
#Készíts programot, amely kiszámítja, hogy a bolygók felszínén érvényes nehézségi gyorsulás
# hányszorosa a földinek!
#A nehézségi gyorsulás képlete: g=G*(M/R^2)
# ahol G = 6,67408*10^-11 Nm^2/kg^2 az univerzális gravitációs állandó
# M bolygó tömege, R pedig a bolygó tömegközéppontjától mért távolság.
#A program ne csak a planets listára működjön, hanem bármely ugyanilyen formátumú, bemenetre is!
#Elvárt futási eredmény:
#Merkúr: 0.38
#Vénusz: 0.90
#Föld: 1.00

import math
planets = [
    # bolygó neve,  tömeg(10^21kg),  sugár(km)
    ('Merkúr',      330.2,           2439.7),
    ('Vénusz',      4868.5,          6051.8),
    ('Föld',        5973.6,          6371.0),
    ('Mars',        641.85,          3389.5),
    ('Jupiter',     1898600,         69911),
    ('Szaturnusz',  568460,          58232),
    ('Uránusz',     86832,           25362),
    ('Neptunusz',   102430,          24622)
]

def planets_g(planets):
    G = 6.67408*10**(-11)
    new_planets = []
    fold_data = 0
    #Föld adatai:
    for i in range(len(planets)):
        if planets[i][0]=="Föld":
            earth_data = G*(planets[i][1]/(planets[i][2]**2))
            fold_data = earth_data
    #Többi bolygó adatainak kiszámítása és összehasonlítása a Földdel.
    for i in range(len(planets)):
        number = (G *(planets[i][1] / (planets[i][2] ** 2))/fold_data)
        new_planets.append((planets[i][0], number))
    #Kiírás
    for planets in new_planets:
        print(f'{planets[0]}: {planets[1]:.2f}')
planets_g(planets)
