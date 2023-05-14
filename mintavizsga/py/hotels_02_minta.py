#!/usr/bin/env python
# coding: utf-8

# ### 1. feladat [6p]
#
# A `planets` lista a Naprendszer bolygóinak tömegét és (átlagos) sugarát tartalmazza. Készíts programot, amely kiszámítja, hogy a bolygók felszínén érvényes nehézségi gyorsulás hányszorosa a földinek! A nehézségi gyorsulás képlete
# $$g = G \frac{M}{R^2},$$
# ahol $G = 6,67408 \cdot 10^{-11} \frac{Nm^2}{kg^2}$ az univerzális gravitációs állandó, $M$ a bolygó tömege, $R$ pedig a bolygó tömegközéppontjától mért távolság. A program ne csak a `planets` listára működjön, hanem bármely ugyanilyen formátumú, bemenetre is! Elvárt futási eredmény:
# ```
#
# Merkúr: 0.38
# Vénusz: 0.90
# Föld: 1.00
# ...
# ```

# In[1]:


import pandas as pd
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


# In[2]:


def planet_speed(planets):
    G = 6.67408 * 10**(-11)
    new_planets = []
    for i in range(len(planets)):
        if planets[i][0] == "Föld":
            fold_data = G*(planets[i][1]/(planets[i][2]**2))
    for i in range(len(planets)):
        new_planets.append(
            (planets[i][0], (G*(planets[i][1]/(planets[i][2]**2))/fold_data)))
    for planets in new_planets:
        print(f'{planets[0]}: {planets[1]:.2f}')


planet_speed(planets)


# ### 2. feladat [8p]
#
# Készíts programot, amely bekéri a felhasználótól $n$ értékét, szimulál $n$ darab kockadobást, majd kiírja, hogy mi volt a leghosszabb 6-os sorozat hossza! Példa futási eredmény:
# ```
#
# n: 50
# 31554643644341364414422455514666664664563666113524
# A leghosszabb 6-os sorozat hossza: 5
# ```

# # Pandas

# In[ ]:


df = pd.read_csv(
    '/home/g14/uni/sze_python_programozas/data/hotels.txt', sep=';')

# Szállodák csoportosítása  a nevük szerint.
gb = df.groupby('Hotel name')

# 1. Hány db értékelés van összesen az egyes szállodákra vonatkozóan?
print(gb['Score'].count())

# 2. A szobák száma (Nr. rooms) alapján melyik az öt legnagyobb szálloda?
print(gb['Nr. rooms'].first().sort_values(ascending=False).head(5))

# 3. Hány ponttal magasabb a medencével (Pool) rendelkezeő szállodák átlagos értéklése
# (Score) a többi szálloda átlagos értékelésénél?
df2 = df.groupby(['Hotel name', 'Pool'])['Score'].mean(
).reset_index()  # Hotelek és medencék, értékelések átlaga
# Medencével rendelkező és nem rendelkező hotelek összesített átlaga
ertek = df2.groupby("Pool")["Score"].mean()
print(ertek['YES'] - ertek['NO'])  # Pont különbség

# 4. Hány ponttal magasabb a teniszpályával(Tennis court) rendelkező szállodák átlagos értékelése
# (Score) a többi szálloda átlagos értékelésénél?
df2 = df.groupby(['Hotel name', 'Tennis court'])['Score'].mean(
).reset_index()  # Hotelek és tenisz pályák, értékelések átlaga
# Tenisz pályával rendelkező és nem rendelkező hotelek összesített átlaga
ertek = df2.groupby("Tennis court")["Score"].mean()
print(ertek['YES'] - ertek['NO'])  # Pont különbség


# # Manuális nem pontos megoldás

# In[3]:


def simulate_dice_rolls(n):
    import random
    rolls = []
    for i in range(n):
        rolls.append(random.randint(1, 6))
    return rolls


def longest_6_in_row(rolls):
    max = 0
    count = 0
    for i in range(len(rolls)):
        count = 0
        if rolls[i] == 6:
            count += 1
        for j in range(1, len(rolls)-i):
            if rolls[i+j] == 6:
                count += 1
            else:
                break
        if count > max:
            max = count
    return max


n = int(input('n: '))
rolls = simulate_dice_rolls(n)
print('n: ', n)
for roll in rolls:
    print(roll, end='')
max_series = longest_6_in_row(rolls)
print(f'\nA leghosszabb 6-os sorozat hossza: {max_series}')


# ### 3. feladat [10p]
#
# A [hotels.txt](hotels.txt) szövegfájl Las Vegas-i szállodák értékeléséről tartalmaz adatokat. Minden sor egy szállóvendég által kiosztott értékeléshez tartozik. Készíts programot, amely kiszámítja és kiírja az alábbi statisztikákat:
#
# - Hány db értékelés van összesen az egyes szállodákra vonatkozóan?
# - A szobák száma (`Nr. rooms`) alapján melyik az öt legnagyobb szálloda?
# - Hány ponttal magasabb a medencével (`Pool`) rendelkező szállodák átlagos értékelése (`Score`) a többi szálloda átlagos értékelésénél?

# In[4]:


filename = '/home/g14/uni/sze_python_programozas/data/hotels.txt'


def get_data(filename):
    with open(filename, 'r') as f:
        # skip the first line
        f.readline()
        lines = f.readlines()
        # read into a list  split by | return the list
        lines = [line.split(';') for line in lines]
        data = []
        # remove the newline character from the last element of each line
        for line in lines:
            line[-1] = line[-1].strip()
            continue
        for line in lines:
            data.append(line)
        return data


def get_reviews(datas):
    reviews = {}
    for data in datas:
        if data[0] not in reviews:
            reviews[data[0]] = 1
        else:
            reviews[data[0]] += 1
    print(reviews)
    return reviews


def top5_rooms(datas):
    hotels = {}
    for data in datas:
        if data[0] not in hotels:
            hotels[data[0]] = int(data[1])
        else:
            continue
    hotels = sorted(hotels.items(), key=lambda x: x[1], reverse=True)
    print(hotels[0:5])


def get_pool_score(datas, rewiews):
    has_pool = {}
    no_pool = {}
    for data in datas:
        # Has pool
        if data[2] == 'YES':
            if data[0] not in has_pool:
                has_pool[data[0]] = int(data[-1])
            else:
                has_pool[data[0]] += int(data[-1])
        # No pool
        else:
            if data[0] not in no_pool:
                no_pool[data[0]] = int(data[-1])
            else:
                no_pool[data[0]] += int(data[-1])

    has_pool_counter = 0
    no_pool_counter = 0
    has_pool_data = 0
    no_pool_data = 0
    for data in has_pool:
        value = has_pool[data]
        value = value / rewiews[data]
        has_pool[data] = value
        has_pool_counter += 1
        has_pool_data += value
    for data in no_pool:
        value = no_pool[data]
        value = value / rewiews[data]
        no_pool[data] = value
        no_pool_counter += 1
        no_pool_data += value

    has_pool_data = has_pool_data / has_pool_counter
    no_pool_data = no_pool_data / no_pool_counter

    diff = has_pool_data - no_pool_data

    print('\n')
    print(diff)


data = get_data(filename)
reviews = get_reviews(data)
top5_rooms(data)
get_pool_score(data, reviews)
