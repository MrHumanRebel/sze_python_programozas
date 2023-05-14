#!/usr/bin/env python
# coding: utf-8

# #  1. feladat [14p]
# Az A , B , C , ..., Z betűk manókat jelölnek, a friends lista pedig megadja azokat párokat,
# akik ismerik egymást. Készítsünk programot, amely kiírja, hogy melyik manónak van a legtöbb
# olyan másodszintű ismerőse, aki nem elsőszintű ismerős! Elsőszintű ismerősöknek az
# ismerősöket, másodszintű ismerősöknek az ismerősök ismerőseit nevezzük. Holtverseny esetén
# elég egy manó nevét kiírni. A program ne csak a megadott friends listára működjön, hanem
# tetszőleges, ugyanilyen formátumú bemenetre is!

# In[24]:


import datetime as dt
import pandas as pd
friends = ['I-N', 'L-W', 'F-R', 'F-Z', 'B-D', 'L-Q', 'I-U', 'A-N', 'E-F', 'A-I',
           'S-T', 'B-S', 'B-E', 'F-P', 'D-V', 'C-V', 'J-S', 'G-I', 'A-C', 'N-X',
           'K-N', 'Q-Y', 'A-U', 'O-Z', 'S-U', 'E-L', 'B-V', 'Y-Z', 'H-O', 'D-U',
           'A-K', 'F-W', 'N-T', 'H-T', 'R-T']

data = []

""" for i in range(len(friends)):
    friends[i] = friends[i].replace('-', '')
    friends[i] = friends[i].split(',')
    data.append(friends[i])

for i in range(len(data)):
    print(data[i]) """

# Beta version

stats = {}
for i in range(len(friends)):
    friends[i] = friends[i].replace('-', '')

for i in range(len(friends)):
    friends[i] = friends[i].replace('-', '')
    for j in range(len(friends[i])):
        for k in range(i+1, len(friends)):
            for x in range(len(friends[k])):
                if friends[k][x] == friends[i][j]:
                    if friends[k][j] not in stats:
                        stats[friends[k][j]] = 1
                    else:
                        stats[friends[k][j]] += 1
stats = sorted(stats.items(), key=lambda x: x[1], reverse=True)
print(stats)


# In[ ]:


""" stats = {}
for i in range(len(friends)):
    friends[i] = friends[i].replace('-', '')

for i in range(len(friends)):
    friends[i] = friends[i].replace('-', '')
    for j in range(len(friends[i])):
        for k in range(i+1,len(friends)):
            for x in range(len(friends[k])):
                if friends[k][x] == friends[i][j]:
                    if friends[k][j] not in stats:
                        stats[friends[k][j]] = 1
                    else:
                        stats[friends[k][j]] += 1
stats = sorted(stats.items(), key=lambda x: x[1], reverse=True)       
print(stats) """


# # 2. feladat [10p]
# A covid19_stats.txt (covid19_stats.txt) szövegfájl a COVID-19 vírussal kapcsolatos statisztikákat
# tartalmaz a 2020.01.23 és 2021.05.11 közötti időszakból, országonkénti bontásban. Minden sor
# azt adja meg, hogy az adott napon az adott országban hány igazolt fertőzés történt ( Confirmed ), hányan gyógyultak meg ( Recovered ) illetve hányan hunytak el a vírus miatt ( Deaths ).
# Készítsünk programot, amely beolvassa a fájl tartalmát, majd válaszol az alábbi kérdésekre!
# 1. Melyek azok az országok, ahol már 2020. januárjában megjelent a vírus?
# 2. Az adathalmaz utolsó napján hány fertőzött volt Németországban ( Germany )?
# 3. Hol volt a legmagasabb az elhunytak aránya a fertőzöttek számához viszonyítva?

# # Pandas

# In[ ]:


df = pd.read_csv(
    '/home/g14/uni/sze_python_programozas/data/covid19_stats.txt', sep=',', skiprows=1)

# print(df.info())

# 1. Melyek azok az országok, ahol már 2020. januárjában megjelent a vírus?
pd.to_datetime(df['Date'])
print(df['Country'][(df['Date'] >= '2020-01') &
      (df['Date'] < '2020-02') & (df['Confirmed'] > 0)])

# 2. Az adathalmaz utolsó napján hány fertőzött volt Németországban ( Germany )?
datemax = df['Date'].max()
print(df[(df['Country'] == 'Germany') & (df['Date'] == datemax)]['Confirmed'])

# 3. Hol volt a legmagasabb az elhunytak aránya a fertőzöttek számához viszonyítva?
print((df.groupby('Country')['Deaths'].sum() /
      df.groupby('Country')['Confirmed'].sum()).idxmax())


# # Manuális nem pontos megoldás

# In[16]:


filename = '/home/g14/uni/sze_python_programozas/data/covid19_stats.txt'


def get_data(filename):
    with open(filename, 'r') as f:
        # skip the first two line
        for i in range(2):
            f.readline()
        lines = f.readlines()
        # read into a list  split by tab
        lines = [line.split(',') for line in lines]
        # remove the newline character from the last element of each line
        for line in lines:
            line[-1] = line[-1].strip()
            continue
        data = []
        for line in lines:
            data.append(line)
        return data


def virus_2020jan(data):
    countries = {}
    for item in data:
        if dt.datetime.strptime(item[0], '%Y-%m-%d') >= dt.datetime.strptime('2020-01-01', '%Y-%m-%d'):
            if item[1] not in countries:
                countries[item[1]] = 1
            else:
                countries[item[1]] += 1
    print(countries)


def germany_latest(data):
    stats = {}
    for item in data:
        if item[1] == 'Germany':
            stats[item[1]] = item[2]
    print(stats)


def death_rate(data):
    stats = {}
    for item in data:
        if item[1] not in stats and item[4] != '0':
            stats[item[1]] = item[2], item[4], int(item[2]) / int(item[4])
        else:
            if item[4] != '0' and int(item[2]) / int(item[4]) > stats[item[1]][2]:
                stats[item[1]] = item[2], item[4], int(item[2]) / int(item[4])
    print(stats)


data = get_data(filename)
virus_2020jan(data)
germany_latest(data)
death_rate(data)
