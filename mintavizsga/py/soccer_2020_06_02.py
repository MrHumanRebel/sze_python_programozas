#!/usr/bin/env python
# coding: utf-8

# # 1. feladat [8p]
#
# Az a. b.c egész számok pitagoraszi számhármast alkotnak. ha a^2 + b^2 = c^2. A numbers lista pozitív egész számokat tartalmaz. Készítsünk programot. amely megadja. hogy található-e pitagoraszi számhármas a numbers listában, és ha igen, akkor melyik pitagoraszi számhármasban a legnagyobb a c szám számjegyeinek az összege! A program ne csak a megadott numbers listára működjön. hanem tetszőleges. ugyanilyen formátumú bemenetre is!

# In[81]:


import pandas as pd
numbers = [2, 3, 4, 5, 6, 7, 8, 11, 12, 13,
           14, 15, 16, 17, 19, 23, 24, 25, 29, 31]


def pite_three(numbers):
    max = 0
    for i in range(len(numbers)):
        sum = 0
        current_a = numbers[i]**2
        for j in range(i+1, len(numbers)):
            current_b = numbers[j]**2
            for k in range(j+1, len(numbers)):
                current_c = numbers[k]**2
                if current_a+current_b == current_c:
                    print(
                        f'Pitagoraszi szamharmas: {numbers[i]}, {numbers[j]}, {numbers[k]}')
                    id = str(numbers[k])
                    for x in range(len(id)):
                        sum += int(id[x])
                    if sum > max:
                        max = int(sum)
    print(f'A legnagyobb c szam szamjegyeinek osszege: {max}')


pite_three(numbers)


# # 2. feladat [12p]
# A soccer.txt szövegfájl európai első osztályú labdarúgó mérkőzésekről tartalmaz adatokat. a 2015-16-os szezonból. Az utolsó 9 oszlop fogadóirodák odds-ait tartalmazza hazai csapat győzelmére ( B365H • BwH • IWH ), a döntetlenre ( B365D. BWD . IWD ) ill. a vendégcsapat győzelmére ( B365A . BWA . IwA ). Készitsünk programot, amely beolvassa a szövegfájl tartalmát, majd válaszol az alábbi kérdésekre!
# - Melyik bajnokságban ( country ) mennyi volt a mérkőzésenkénti gólátlag?
# - Melyik fogadóiroda adta átlagosan a legmagasabb odds-okat a hazai csapat győzelméért?
# - Melyik bajnokságban született a legtöbb döntetlen?
# - A B365 fogadóiroda szerfloat melyik eredmény volt a legváratlanabb (azaz a legmagasabb odds értékű)?
#

# # Pandas

# In[ ]:


df = pd.read_csv(
    '/home/g14/uni/sze_python_programozas/data/soccer.txt', sep=',', skiprows=1)
# print(df.info())
# print(df)

# 1. Melyik bajnokságban ( country ) mennyi volt a mérkőzésenkénti gólátlag?
df['goals'] = df['home_team_goal']+df['away_team_goal']
print(df.groupby('country')['goals'].mean())

# 2. Melyik fogadóiroda adta átlagosan a legmagasabb odds-okat a hazai csapat győzelméért?
max_home_odds = df[['B365H', 'BWH', 'IWH']].mean().max()
max_home_odds_bookie = df[['B365H', 'BWH', 'IWH']].mean().idxmax()
print(f"{max_home_odds_bookie}: {max_home_odds}")

# 3. Melyik bajnokságban született a legtöbb döntetlen?
df['goalsequal'] = df['home_team_goal'] == df['away_team_goal']
print(df.groupby(df['country'])['goalsequal'].sum().idxmax())

# 4. A B365 fogadóiroda melyik eredmény volt a legváratlanabb (azaz a legmagasabb odds értékű)?
max_odds = df[['B365H', 'B365D', 'B365A']].max().max()
max_odds_bookie = df[['B365H', 'B365D', 'B365A']].max().idxmax()
print(f'A {max_odds_bookie} fogadóiroda {max_odds} eredménye volt a legváratlanabb.')


# # Manuális nem pontos megoldás

# In[ ]:


filename = '/home/g14/uni/sze_python_programozas/data/soccer.txt'


def get_data(filename):
    with open(filename, 'r') as f:
        # skip the first two line
        for i in range(2):
            f.readline()
        lines = f.readlines()
        # read into a list  split by ,
        lines = [line.split(',') for line in lines]
        # remove the newline character from the last element of each line
        for line in lines:
            line[-1] = line[-1].strip()
            continue
        data = []
        for line in lines:
            data.append(line)
        return data


def country_golatlag(data):
    goals = {}
    for item in data:
        if item[0] not in goals:
            goals[item[0]] = (int(item[4]) + int(item[5]))
        else:
            goals[item[0]] += (int(item[4]) + int(item[5]))
    matches = {}
    for item in data:
        if item[0] not in matches:
            matches[item[0]] = 1
        else:
            matches[item[0]] += 1
    for i in matches:
        print(f'Golatlag {i}-ban: {goals[i]/matches[i]}')


def avg_high_odds(data):
    stats = {}  # 6 ,9 ,12
    for item in data:
        if item[6] != '':
            if 'B365H' not in stats:
                stats['B365H'] = {'ODDS': float(item[6]), 'MATCHES': 1}
            else:
                stats['B365H']['ODDS'] += float(item[6])
                stats['B365H']['MATCHES'] += 1
        if item[9] != '':
            if 'BWH' not in stats:
                stats['BWH'] = {'ODDS': float(item[9]), 'MATCHES': 1}
            else:
                stats['BWH']['ODDS'] += float(item[9])
                stats['BWH']['MATCHES'] += 1
        if item[12] != '':
            if 'IWH' not in stats:
                stats['IWH'] = {'ODDS': float(item[12]), 'MATCHES': 1}
            else:
                stats['IWH']['ODDS'] += float(item[12])
                stats['IWH']['MATCHES'] += 1
    avg = {}
    avg['B365H'] = stats['B365H']['ODDS']/stats['B365H']['MATCHES']
    avg['BWH'] = stats['BWH']['ODDS']/stats['BWH']['MATCHES']
    avg['IWH'] = stats['IWH']['ODDS']/stats['IWH']['MATCHES']
    avg = sorted(avg.items(), key=lambda x: x[1], reverse=True)
    print(f' B365H : {avg[0][1]}')


def dontetlen(data):
    stats = {}
    for item in data:
        if item[4] == item[5]:
            if item[0] not in stats:
                stats[item[0]] = 1
            else:
                stats[item[0]] += 1
    stats = sorted(stats.items(), key=lambda x: x[1], reverse=True)
    print(f'Döntetlenek száma: {stats}')


def b365(data):
    max = 0.0
    counter = 0
    idx = 0
    for item in data:
        if item[6] != '':
            if float(item[6]) > max:
                max = float(item[6])
                idx = counter
        if item[7] != '':
            if float(item[7]) > max:
                max = float(item[7])
                idx = counter
        if item[8] != '':
            if float(item[8]) > max:
                max = float(item[8])
                idx = counter
        counter += 1

    print(
        f'A legnagyobb odds a B365 szerint: {max}, a meccs adatai: {data[idx][0:6]}')


data = get_data(filename)
country_golatlag(data)
avg_high_odds(data)
dontetlen(data)
b365(data)
