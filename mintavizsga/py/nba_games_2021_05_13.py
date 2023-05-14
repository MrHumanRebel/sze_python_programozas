#!/usr/bin/env python
# coding: utf-8

# # 1. feladat [10p]
# Készítsünk programot, amely bekér a felhasználótól két sztringet, majd kiírja a mindkét sztringben megtalálható
# bigramok számát! Bigramnak a 2 karakter hosszú részsztringet nevezzük, pl. papamaci sztring bigramfelbontása pa - ap - pa - am - ma - ac - ci . A program ne tekintse különbözőnek a kis és nagybetűket! Példa
# futási eredmény:
# 1. sztring: PapaMaci
# 2. sztring: MamaMaci
# közös bigramok száma: 4

# In[1]:


import pandas as pd
data = input("Add meg az első sztringet: ")
data_2 = input("Add meg a második sztringet: ")


def bigram(data):
    data = data.lower()
    bigram = []
    str = ""
    for i in range(len(data)):
        if len(str) == 2:
            bigram.append(str)
            str = ""
            str += data[i]
        else:
            str += data[i]
        if i == len(data) - 1:
            bigram.append(str)
    return bigram


def common_bigram(data, data_2):
    common_bigrams = []
    counter = 0
    for i in data:
        for j in data_2:
            if i == j:
                common_bigrams.append(i)
                counter += 1
    print(f'Közös bigrammok száma: {counter}')
    return common_bigrams, counter


bigrammm = common_bigram(bigram(data), bigram(data_2))


# # 2. feladat [14p]
# Az nba_games.txt (nba_games.txt) az amerikai professzionális kosárlabda bajnokság (NBA) mérkőzéseiről
# tartalmaz adatokat, a 2013-astól a 2019-es szezonig. Készítsünk programot, amely beolvassa a szövegfájl
# tartalmát, majd válaszol az alábbi kérdésekre!
# 1. A mérkőzések hány százalékát nyerte meg a hazai ( home ) csapat?
# 2. Hány mérőzésen szedtek le a csapatok 130-nál több lepattanót ( REB )?
# 3. Melyik mérkőzésen született a legnagyobb különbségű győzelem?
# 4. Mi a csapatok erősorrendje a győzelmek száma alapján?

# # Pandas

# In[ ]:


df = pd.read_csv(
    '/home/g14/uni/sze_python_programozas/data/nba_games.txt', sep='|', skiprows=1)
# 1. A mérkőzések hány százalékát nyerte meg a hazai ( home ) csapat?
print('A mérkőzések ', (sum(df['PTS_home'] > df['PTS_away']) /
      len(df['PTS_home'])) * 100, '%-át nyerte meg a hazai csapat.')

# 2. Hány mérőzésen szedtek le a csapatok 130-nál több lepattanót ( REB )?
print(len(df[(df['REB_home']+df['REB_away']) > 130]),
      'mérkőzésen szedtek le a csapatok 130-nál több lepattanót.')

# 3. Melyik mérkőzésen született a legnagyobb különbségű győzelem?
print(df.iloc[abs(df['PTS_home']-df['PTS_away']).idxmax()])

# 4. Mi a csapatok erősorrendje a győzelmek száma alapján?
hazaigyozelem = df[(df['PTS_home'] > df['PTS_away'])
                   ].groupby('TEAM_home').size()
hazaivereseg = df[(df['PTS_home'] < df['PTS_away'])
                  ].groupby('TEAM_home').size()
print((hazaigyozelem + hazaivereseg).sort_values(ascending=False))


# # Manuális nem pontos megoldás

# In[1]:


def read_file(path):
    data = open(path)
    nba = []
    next(data)
    next(data)
    for line in data:
        date = int((line[0]+line[1]+line[2]+line[3]))
        if date >= 2013 and date <= 2019:
            nba.append(line.strip().split("|"))
    return nba


def home_team_win_percentage(nba):
    wins = 0
    loses = 0
    for i in nba:
        if (int(i[4]) > int(i[5])):
            wins += 1
        else:
            loses += 1
    print(f'Az otthoni csapat győzelmének aránya: {wins/(wins+loses)*100:.2f}')
    return wins/(wins+loses)*100


def count_reb(nba):
    rebs = 0
    for i in nba:
        total_rebs = int(i[6]) + int(i[7])
        if (total_rebs > 130):
            rebs += 1
    print(f'A 130-nál több lepattanóval rendelkező meccsek száma: {rebs}')
    return rebs


def top_diff_win(nba):
    max_diff = 0
    index = None
    for i in nba:
        if (int(i[4]) > int(i[5])):
            diff = int(i[4]) - int(i[5])
            if (diff > max_diff):
                max_diff = diff
                index = i
        else:
            diff = int(i[5]) - int(i[4])
            if (diff > max_diff):
                max_diff = diff
                index = i
    for i in range(1, (len(index)-8)):
        print(index[i], end=" ")
    return index


def teams_power_order(nba):
    nba = sorted(nba, key=lambda x: x[2])
    nba_teams = []
    counter = 0
    current_team = nba[0][2]
    for i in range(len(nba)):
        if nba[i][2] == current_team:
            counter += int(nba[i][4])
        else:
            nba_teams.append([current_team, counter])
            counter = 0
            current_team = str(nba[i][2])
            counter += int(nba[i][4])
    nba_teams = sorted(nba_teams, key=lambda x: x[1], reverse=True)
    for i in nba_teams:
        print(i[0])
    return nba_teams


nba_data = read_file("/home/g14/uni/sze_python_programozas/data/nba_games.txt")
print('\n')
home_wins = home_team_win_percentage(nba_data)
print('\n')
rebs_count = count_reb(nba_data)
print('\n')
win_max = top_diff_win(nba_data)
print('\n')
sort_team = teams_power_order(nba_data)
