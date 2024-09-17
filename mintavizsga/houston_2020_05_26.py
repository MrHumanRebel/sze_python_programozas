#!/usr/bin/env python
# coding: utf-8

# # 1. feladat [8 p]
# 
# A words lista sztringeket tartalmaz. Készítsünk programot, amely megadja, hogy az angol ABC melyik betűje fordul elő a legtöbb szóban! A program ne tegyen különbséget a kis- és nagybetűk között, illetve ne csak a megadott words listára működjön, hanem tetszőleges, ugyanilyen formátumú bemenetre is!

# In[1]:


words = [
    'Apple', 'Apricot', 'Avocado', 'Banana', 'Blueberry',
    'Cherry', 'Coconut', 'Grape', 'Grapefruit', 'Fig',
    'Kiwi', 'Lemon', 'Lime', 'Mandarin', 'Mango',
    'Melon','Nectarine', 'Orange', 'Papaya', 'Peach',
    'Pear', 'Pineapple', 'Plum', 'Raspberry', 'Strawberry'
]

words = [word.lower() for word in words]
letters = {}

for item in words:
    for letter in item:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
letters = sorted(letters.items(), key=lambda x: x[1], reverse=True)
print(letters[0])


# # 2. feladat [12 p]
# 
# A houston.txt szövegfájl a texasi Houston időjárásról tartalmaz napi bontású adatokat. A hőmérséklet értékek (* _hőm) Fahrenheit-fokban, a csapadék mennyiségének értékei (* _csap) hüvelyben vannak megadva. A rekordok és az év adott napjához tartozó átlagok az 1880 óta eltelt időszakra vonatkoznak. észítsünk programot, amely beolvassa a szövegfájl tartalmát, majd válaszol a következő kérdésekre:
# 
# - Mikor volt a legnagyobb az eltérés a napi maximális és a napi minimális hőmérséklet között?
# - Celcius fokban kifejezve mennyi volt a legalancsonyabb és legmagasabb hőmérséklet, amit Houstonban valaha mértek? (C = (F - 32) * 5/9) Melyik évben mérték ezt?
# - Melyik hónapban mennyi volt az összes csapadék mm-ben? (1 hüvely = 25.4 mm)

# # Pandas

# In[2]:


import pandas as pd

df = pd.read_csv('/home/g14/uni/sze_python_programozas/data/houston.txt', sep='|', skiprows=3)
#print(df.info())

#1. Mikor volt a legnagyobb az eltérés a napi maximális és a napi minimális hőmérséklet között?

df['hőmkül'] = abs(df['napi_min_hőm']-df['napi_max_hőm'])#Hőmérséklet különbségek abszolútértéke
maxhömkülindex = df['hőmkül'].idxmax() #Megkeressük a hőmérsékletek közül a maximális értéknek az indexét.
print('Dátum:', df.loc[maxhömkülindex]['dátum'], 'Maximális eltérés:', max(df['hőmkül'])) #Vissza adjuk az index szerinti sort.

#2. Celcius fokban kifejezve mennyi volt a legalacsonyabb és legmagasabb hőmérséklet,
# amit Houstonban valaha mértek? (C = (F - 32) * 5/9) Melyik évben mérték ezt?

rekordmin = df['rekord_min_hőm'].min()
rekordmin = ((rekordmin-32)* (5/9))
rekordminidx = df['rekord_min_hőm'].idxmin()
rekordminev = df.loc[rekordminidx]['rekord_min_hőm_év']
print(f'A rekord minimum hőmérséklet: {rekordmin}°C méghozzá {rekordminev}. évben')

rekordmax = df['rekord_max_hőm'].max()
rekordmax = ((rekordmax-32)* (5/9))
rekordmaxidx = df['rekord_max_hőm'].idxmax()
rekordmaxev = df.loc[rekordmaxidx]['rekord_max_hőm_év']
print(f'A rekord maximum hőmérséklet: {rekordmax}°C méghozzá a {rekordmaxev}. évben')

#3. Melyik hónapban mennyi volt az összes csapadék mm-ben? (1 hüvely = 25.4 mm)
import datetime as dt

df['napi_csap_mm'] = df['napi_csap']*25.4 #Napi csapadék mennyiség hüvelyben.
df['honap'] = pd.to_datetime(df['dátum']).dt.month #Hónap oszlop létrehozása és dátum oszlop dátummá alakítása.
honapok = df.groupby("honap").sum()["napi_csap_mm"]#Havi csapadékmennyiségek összeadása.
print(honapok)


# # Manuális nem pontos megoldás

# In[3]:


filename = '/home/g14/uni/sze_python_programozas/data/houston.txt'

def get_data(filename):
    with open(filename, 'r') as f:
        # skip the first four line
        for i in range(4):
            f.readline()
        lines = f.readlines()
        # read into a list  split by | return the list 
        lines = [line.split('|') for line in lines]    
        # remove the newline character from the last element of each line
        for line in lines:
            line[-1] = line[-1].strip()
            continue
        data = [] 
        for line in lines:
            data.append(line) 
        return data

def maxdiff(data):
    diff = 0
    idx = 0
    counter = 0
    for item in data:
        act_diff = abs(float(item[2]) - float(item[3]))
        if act_diff > diff:
            diff = act_diff
            idx = counter
        counter += 1
    print(f' A legnagyobb különbség {data[idx][0]} napon volt, a különbség {diff:.2f} volt')

def minmax(data):
    min_temp = 1000
    max_temp = -1000
    min_idx = 0
    max_idx = 0
    counter = 0
    for item in data:
        if float(item[6]) < min_temp:
            min_temp = float(item[6])
            min_idx = counter
        if float(item[7]) > max_temp:
            max_temp = float(item[7])
            max_idx = counter
        counter += 1
    min_temp = (min_temp-32) * 5/9
    max_temp = (max_temp-32) * 5/9
    print(f' A legkisebb hőmérséklet: {min_temp:.2f} volt, amit {data[min_idx][0]} napon mértünk')
    print(f' A legnagyobb hőmérséklet: {max_temp:.2f} volt, amit {data[max_idx][0]} napon mértünk')


def rain_by_moth(data):
    desired_data = {}
    for item in data:
        year = item[0].split('-')[0]
        month = item[0].split('-')[1]
        date = year + '-' + month
        if date not in desired_data:
            desired_data[date] = float(item[11]) * 25.4
        else:
            desired_data[date] += float(item[11]) * 25.4
    print(desired_data)
        

data = get_data(filename)
maxdiff(data)
minmax(data)
rain_by_moth(data)

