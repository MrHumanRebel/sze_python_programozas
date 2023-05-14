#!/usr/bin/env python
# coding: utf-8

# # 1. feladat [8p]
#
#  Készítsünk programot, amely bekér a felhasználótól egy n természetes számot, felbontja az összes lehetséges módon 3 különbözö természetes szám összegére, és kiírja ezeket a felbontásokat! A tagok sorrendje ne számítson, azaz pl. 1 + 2 + 3 és 1 + 3 + 2 ne számítson különbözőnek! Példa futási eredmény:
#
# n: 7
#
# - 0 + 1 + 6
# - 0 + 2 + 5
# - 0 + 3 + 4
# - 1 + 2 + 4

# In[19]:


import pandas as pd
n = int(input("n: "))

for i in range(0, n, 1):
    for j in range(0, n, 1):
        for k in range(0, n, 1):
            if i+j+k == n and i != j and i != k and j != k and i < j < k:
                print(i, j, k)


# # 2. feladat [12p]
#
# A zoo.txt több száz gerinces állatfaj várható élettartamáról tartalmaz becsléseket, észak-amerikai állatkertek törzskönyvi adatai alapján. Készítsünk programot, amely beolvassa a szövegfájl tartalmát. majd válaszol az alábbi kérdésekre!
# - Melyik a 10 legmagasabb várható élettartamú (mle) állatfaj?
# - Átlagosan mennyi a várható élettartam az egyes rendszertani osztályokban ( taxonomy_class)?
# - Melyik fajnál a legnagyobb a különbség a hímek és a nőstények várható élettartama között (male_mle, female_mle )?
# - A sample_size oszlop azt adja meg, hogy az adott fajból hány egyedről van mérési adat. Összesen hány hüllőről ( Reptilia ) van mérési adat az adathalmazban?
#

# # Pandas

# In[ ]:


df = pd.read_csv(
    '/home/g14/uni/sze_python_programozas/data/zoo.txt', sep='|', skiprows=1)
# print(df.info())

# 1. Melyik a 10 legmagasabb várható élettartamú (mle) állatfaj?
top10 = df.nlargest(10, 'mle')
print(top10[['common_name', 'mle']])

# 2. Átlagosan mennyi a várható élettartam az egyes rendszertani osztályokban ( taxonomy_class)?
print(df.groupby('taxonomy_class')['mle'].mean().sort_values(ascending=False))

# 3. Melyik fajnál a legnagyobb a különbség a hímek és a nőstények várható élettartama között (male_mle, female_mle )?
df['diff_mle'] = abs(df['male_mle']-df['female_mle'])
maxindx = df['diff_mle'].idxmax()
max = df['diff_mle'].max()
print(df['common_name'][maxindx],
      'fajnál a legnagyobb a különbség a hímek és a nőstények várható élettartama között, méghozzá', max, 'évvel.')

# 4. A sample_size oszlop azt adja meg, hogy az adott fajból hány egyedről van mérési adat.
# Összesen hány hüllőről ( Reptilia ) van mérési adat az adathalmazban?
reptilia_data = df[df['taxonomy_class'] == 'Reptilia']
reptilia_sample_size = reptilia_data['sample_size'].sum()
print(reptilia_sample_size)


# # Manuális nem pontos megoldás

# In[1]:


filename = '/home/g14/uni/sze_python_programozas/data/zoo.txt'


def get_data(filename):
    with open(filename, 'r') as f:
        # skip the first two line
        for i in range(2):
            f.readline()
        lines = f.readlines()
        # read into a list  split by tab
        lines = [line.split('|') for line in lines]
        # remove the newline character from the last element of each line
        for line in lines:
            line[-1] = line[-1].strip()
            continue
        data = []
        for line in lines:
            data.append(line)
        return data


def highest_life_exp(data):
    animals = {}
    data = sorted(data, key=lambda x: x[4], reverse=True)
    for i in range(10):
        print(data[i][0])


def avg_life_exp(data):
    animals = {}
    for item in data:
        if item[4] != '':
            if item[2] not in animals:
                animals[item[2]] = [float(item[4]), 1]
            else:
                animals[item[2]][0] += float(item[4])
                animals[item[2]][1] += 1
    avg_animals = {}
    for item in animals:
        avg_animals[item] = animals[item][0] / animals[item][1]
    print(avg_animals)


def male_female_mle_diff(data):
    # 9  male mle
    # 13 female mle
    animals = {}
    for item in data:
        if item[9] != '' and item[13] != '':
            if item[0] not in animals:
                animals[item[0]] = abs(float(item[9]) - float(item[13]))
    animals = sorted(animals, key=lambda x: x[1], reverse=True)
    print(animals[0])


def sample(data):
    animals = {}
    for item in data:
        if item[2] == 'Reptilia':
            if item[2] not in animals:
                animals[item[2]] = float(item[3])
            else:
                animals[item[2]] += float(item[3])
    print(animals)


data = get_data(filename)
highest_life_exp(data)
avg_life_exp(data)
male_female_mle_diff(data)
sample(data)
