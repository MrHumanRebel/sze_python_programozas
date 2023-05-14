#!/usr/bin/env python
# coding: utf-8

# ### 1. feladat [6p]
#
# Készíts programot, amely bekér a felhasználótól két sztringet, majd kiírja a bennük található leghosszabb közös részsztringet! Példa futási eredmény:
# ```
# 1. sztring: András
# 2. sztring: Bandi
# A leghosszabb közös rész: nd
# ```

# In[62]:


import pandas as pd
from datetime import datetime


def longest_common_substr(s1, s2):
    for i in range(len(s1), 0, -1):
        for j in range(len(s1) - i + 1):
            if s1[j:j + i] in s2:
                return s1[j:j + i]


# In[63]:


longest_common_substr("András", "Bandi")


# ### 2. feladat [8p]
#
# A `birthdays` lista kitalált személyek nevét és születési dátumát tartalmazza. Készíts programot, amely megkeresi, hogy kik állnak életkorban egymáshoz a legközelebb, és hány nap köztük a különbség! A program ne csak a megadott `birthdays` listára működjön, hanem tetszőleges, ugyanilyen formátumú bemenetre is! Feltehetjük, hogy minden név különböző, és legalább két név van megadva.

# In[64]:


birthdays = [
    ('Kovács Andor',   '1999-10-29'),
    ('Kiss Martina',   '2000-02-13'),
    ('Horváth Barna',  '1999-12-05'),
    ('Győri Eszter',   '2000-10-29'),
    ('Nagy Tivadar',   '1999-08-16'),
    ('Tóth Tamara',    '2000-01-30'),
    ('Szakács Sándor', '1999-09-02')
]


# In[65]:


def get_name_of_closest_days_to_each_other(birthdays):

    birthdays = [(name, datetime.strptime(date, '%Y-%m-%d'))
                 for name, date in birthdays]
    birthdays.sort(key=lambda x: x[1])

    for i in range(len(birthdays) - 1):
        diff = (birthdays[i + 1][1] - birthdays[i][1]).days
        if i == 0:
            closest = diff
            closest_names = birthdays[i][0], birthdays[i + 1][0]
        if diff < closest:
            closest = diff
            closest_names = birthdays[i][0], birthdays[i + 1][0]
    print(
        f'Életkorban legközelebb állók: {closest_names[0]}, {closest_names[1]}\n {closest} nap köztük a különbség')


get_name_of_closest_days_to_each_other(birthdays)


# Elvárt futási eredmény:
# ```
#
# Életkorban legközelebb állók: Kiss Martina, Tóth Tamara
# 14 nap köztük a különbség
# ```

# ### 3. feladat [10p]
#
# Az [investments.txt](investments.txt) szövegfájl amerikai cégekbe történő befektetésekről tartalmaz adatokat (a TechCrunch hírportál alapján). Készíts programot, amely kiszámítja és kiírja az alábbi statisztikákat:
#
# - Hány befektetés történt összesen az egyes cégekbe?
# - Melyik cégbe fektették be a legtöbb pénzt?
# - Cégkategóriánként hány dollárt fektettek be összesen?

# # Pandas

# In[ ]:


df = pd.read_csv(
    '/home/g14/uni/sze_python_programozas/data/investments.txt', sep='|')
# print(df.info())

# 1. Hány befektetés történt összesen az egyes cégekbe?
print(df.groupby('company').size().sort_values(ascending=False))

# 2. Melyik cégbe fektettek be legtöbbször?
print(df.groupby('company').size().sort_values(ascending=False).head(1))

# 3. Melyik cégbe fektették be a legtöbb pénzt?
print(df.groupby('company')['raisedAmt'].sum(
).sort_values(ascending=False).head(1))

# 4. Cégkategóriánként hány dollárt fektettek be összesen?
print(df.groupby('category')['raisedAmt'].sum().sort_values())


# # Manuális nem pontos megoldás

# In[66]:


filename = '/home/g14/uni/sze_python_programozas/data/investments.txt'


def get_investments(filename):
    with open(filename, 'r') as f:
        # skip the first line
        f.readline()
        lines = f.readlines()
        # read into a list  split by | return the list
        lines = [line.split('|') for line in lines]
        # remove the newline character from the last element of each line
        for line in lines:
            line[-1] = line[-1].strip()
            continue
        investments = []
        for line in lines:
            investments.append(
                (line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8]))
        return investments


def get_companies(investments):
    companies = {}
    for investment in investments:
        company = investment[0]
        if company not in companies:
            companies[company] = 1
        else:
            companies[company] += 1
    for company in companies:
        print(f'{company} => {companies[company]} db befektetés')
    return companies


def get_categories(investments):
    categories = {}
    for investment in investments:
        categorie = investment[2]
        if categorie not in categories:
            categories[categorie] = 1
        else:
            categories[categorie] += 1
    return categories


def get_inv_by_company(investments):
    companies = get_companies(investments)
    money = {}
    for i in range(len(companies)):
        current_company = list(companies.keys())[i]
        for j in range(len(investments)):
            if current_company == investments[j][0]:
                if current_company not in money:
                    money[current_company] = int(investments[j][6])
                else:
                    money[current_company] += int(investments[j][6])
    money = sorted(money.items(), key=lambda x: x[1], reverse=True)
    print('\n')
    print(
        f'A legtöbb befektetést a {money[0][0]} cégnél tették, összesen {money[0][1]}')


def get_inv_by_categ(investments):
    categories = get_categories(investments)
    money = {}
    for i in range(len(categories)):
        current_categ = list(categories.keys())[i]
        for j in range(len(investments)):
            if current_categ == investments[j][2]:
                if current_categ not in money:
                    money[current_categ] = int(investments[j][6])
                else:
                    money[current_categ] += int(investments[j][6])
    money = sorted(money.items(), key=lambda x: x[1], reverse=True)
    for moni in money:
        print(f'{moni[0]} => {moni[1]}')


investments = get_investments(filename)


# In[67]:


get_inv_by_company(investments)


# In[68]:


get_inv_by_categ(investments)
