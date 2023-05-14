#!/usr/bin/env python
# coding: utf-8

# # 1. feladat [14p]
# Az A , B , C , ..., Z betűk manókat jelölnek, a sztringként megadott friends táblázat pedig
# definiálja azokat párokat, akik ismerik egymást. (Ha az X sor Y oszlopában 1-es áll, akkor X és
# Y ismeri egymást. A reláció szimmetrikus, azaz ha X ismeri Y -t, akkor Y is ismeri X -et.)
# Készítsünk programot, amely kiírja, hogy melyik két manónak van a legtöbb közös ismerőse! A
# program ne csak a megadott friends táblázatra működjön, hanem tetszőleges, ugyanilyen
# formátumú bemenetre is!
# 

# In[54]:


friends = ( # Úgy gépeltem be szóval lehet nem 100% pontos, ez valami óborzalom adatmegadás :)
 ' ABCDEFGHIJKLMNOPQRSTUVWXYZ\n' +
 'A1     1111    1           \n' +
 'B 1 1   1       11   1     \n' +
 'C  11        1             \n' +
 'D 111      1              1\n' +
 'E    1       1  1        1 \n' +
 'F     1     1    1       1 \n' +
 'G1     1 1           1     \n' +
 'H11    11      1   1    1  \n' +
 'I1    111      1     1     \n' +
 'J1        1        1   1   \n' +
 'K   1      1     1      11 \n' +
 'L     1     1    11    1   \n' +
 'M  1 1       11   1   1   1\n' +
 'N            1111   1      \n' +
 'O1     11     11     1 1 1 \n' +
 'P 1  1      11 1 11   1  1 \n' +
 'Q 1           1 11 11 11   \n' +
 'R     1             1 11 1 \n' +
 'S       1     1    1 1 111 \n' +
 'T              1 11 1    1 \n' +
 'U 1    1 11  1    1  1 1 1 \n' +
 'V           1         1   1\n' +
 'W          1   1  1 1 1    \n' +
 'X       1  1    1  1    1  \n' +
 'Y    11        1   111   1 \n' +
 'Z   1         1  1 1  1    1'
)

def find_most_common_friends(friends):
    common_friends = {}
    
    # Bontsun fel a sorokat és oszlopokat
    rows = friends.split('\n')    
    #print(rows)
    cols = rows.pop(0)
    #print(cols)
    cols = cols.strip()
    #print(cols)
    
    # Számoljuk meg, hogy hányan ismerik egymást és tároljuk el egy dictionary-ben
    for i in range(len(cols)):
        for j in range(i+1, len(cols)):
            person1 = cols[i]
            person2 = cols[j]
            count = 0
            for row in rows:
                if row[i+1] == '1' and row[j+1] == '1':
                    count += 1
            common_friends[(person1, person2)] = count
            
    print(common_friends)
    # Számoljuk meg, hogy ki ismeri a legtöbbet és adjuk vissza a párt
    max_count = 0
    max_pair = None
    for pair, count in common_friends.items():
        if count > max_count:
            max_count = count
            max_pair = pair
    print(max_pair)


find_most_common_friends(friends)


# # 2. feladat [10p]
# A dry_bean.txt (dry_bean.txt) szövegfájl 13 611 db lefényképezett babszemről tartalmaz adatokat.
# Minden sor egy babszemnek felel meg. Az első 16 oszlop méret- és alakjellemzőket tartalmaz (pl.
# kerület, terület, konvex burok területe, excentricitás), az utolsó oszlop pedig a növény fajtáját adja
# meg (SEKER, BARBUNYA, BOMBAY, CALI, DERMASON, HOROZ vagy SIRA). Készítsünk
# programot, amely beolvassa a fájl tartalmát, majd válaszol az alábbi kérdésekre!
# 
# 1. Mi az egyes fajtákhoz tartozó babszemek százalékos aránya?
# 2. Melyik fajta szemeinek a legnagyobb az átlagos excentricitása?
# 3. Hány konvex alakú babszem található az adathalmazban?
# 

# # Pandas

# In[ ]:


import pandas as pd

df = pd.read_csv('C:\\Users\\Dorián\\PycharmProjects\\PythonVizsgaFelkészülés1Feladatok\\tables\\dry_bean.txt', sep=',', skiprows=4)
#print(df.info())

#1. Mi az egyes fajtákhoz tartozó babszemek százalékos aránya?
bean_counts = df['Class'].value_counts()
total_count = bean_counts.sum()
bean_percentages = bean_counts / total_count * 100
print(bean_percentages)

#2. Melyik fajta szemeinek a legnagyobb az átlagos excentricitása?
max_fajta = df.groupby('Class')['Eccentricity'].mean().idxmax()
max_szama = df.groupby('Class')['Eccentricity'].mean().max()
print(f'{max_fajta} szemeinek a legnagyobb az átlagos excentricitása, méghozzá {max_szama}')

#3. Hány konvex alakú babszem található az adathalmazban?
print(len(df[df['ConvexArea']==df['Area']]))
#Nem tudom hogy 0-e, de ez tűnik logikusnak.


# # Manuális nem pontos megoldás

# In[78]:


filename = '/home/g14/uni/sze_python_programozas/data/dry_bean.txt'

def get_data(filename):
    with open(filename, 'r') as f:
        # skip the first four line
        for i in range(5):
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

def percentage(data):
    alldata = len(data)
    beans = {}
    for item in data:
        if item[-1] not in beans:
            beans[item[-1]] = 1, 1 / alldata * 100
        else:
            beans[item[-1]] = beans[item[-1]][0] + 1, beans[item[-1]][0] / alldata * 100
    beans = sorted(beans.items(), key=lambda x: x[1][1], reverse=True)
    print(beans)
    

def highest_eccentri(data):
    beans = {}
    for item in data:
        if item[-1] not in beans:
            beans[item[-1]] = 1, float(item[5]), 0
        else:
            beans[item[-1]] = beans[item[-1]][0] + 1, beans[item[-1]][1] + float(item[5]), beans[item[-1]][1]/int(beans[item[-1]][0])*100
    beans = sorted(beans.items(), key=lambda x: x[1][2], reverse=True)
    print(beans)    

def konvex(data):
    beans = {}
    knvx = 0
    for item in data:
        if float(item[6]) > 0:
            knvx += 1
    print(knvx)

data = get_data(filename)
percentage(data)
highest_eccentri(data)
konvex(data)

