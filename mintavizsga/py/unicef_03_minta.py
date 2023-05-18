#!/usr/bin/env python
# coding: utf-8

# ### 1. feladat [6p]
# 
# Készíts (teljeskörűen paraméterezett) függvényt, amely bemenetként megkapja pozitív egész számok egy nemüres listáját, és visszaadja a lista azon elemét, amelyikben a számjegyek összege a legnagyobb. Hívd meg a függvényt a `[245, 1132, 98, 465, 14231, 7854, 2542]` listával és írd ki a kapott eredményt!

# In[ ]:


def sum_numplaces(list):
    max = 0
    for item in list:
        sum = 0
        item = str(item)
        for i in range(len(item)):
            sum += int(item[i])
        if sum > max:
            max = sum
            num = item
    return num
            
sum_numplaces([245, 1132, 98, 465, 14231, 7854, 2542])


# ### 2. feladat [8p]
# Az `edges` lista kitalált személyekből képezett párokat tartalmaz. Egy pár azt jelenti, hogy az adott személyek ismeri egymást. Készíts függvényt, amely egy adott, ilyen felépítésű listára meghatározza azt a 2 személyt, akiknek a legtöbb közös ismerősük van! Ha több ilyen személypár is lenne, akkor az egyik ilyen pár legyen az eredmény! Hívd meg a függvényt az `edges` listára és írd ki a kapott eredményeket!

# In[8]:


edges = [
    ("Adél", "Dezső"), ("Géza", "Mihály"), ("Károly", "Adél"), ("Antal", "Mihály"), ("Károly", "Sára"),
    ("Mihály", "Vilma"), ("Dezső", "Vilma"), ("Vilma", "Antal"), ("Károly", "Mihály"), ("Elvira", "Adél"),
    ("Izabella", "Adél"), ("Mihály", "Izabella"), ("Géza", "Vilma"), ("Károly", "Elvira"), ("Elvira", "Mihály"),
    ("Géza", "Dezső"), ("Sára", "Adél"), ("Géza", "Adél"), ("Géza", "Izabella"), ("Izabella", "Dezső")    
]


# In[16]:


from collections import defaultdict
from itertools import combinations

def friends(edges):
    ismerosok = defaultdict(set)
    for x,y in edges:
        ismerosok[x].add(y)
        ismerosok[y].add(x)
    kozosismerosok = [(len(ismerosok[x] & ismerosok[y]), x, y) for x,y in combinations(ismerosok, 2)]
    print(f'A legtöbb közös ismerőssel rendelkező pár: {max(kozosismerosok)[1]} és {max(kozosismerosok)[2]}')
    print(f'Ennyi közös ismerősük van: {max(kozosismerosok)[0]}')

friends(edges)


# # Részmegoldás

# In[17]:


def friends(edges):
    array = len(edges)
    persons = {}
    for item in edges:
        for name in item:
            if name not in persons:
                persons[name] = 1
            else:
                persons[name] += 1
    persons = sorted(persons.items(), key=lambda x: x[1], reverse=True)
    print(f'A legtöbb barátja van: {persons[0][0]} ({persons[0][1]} fő)')
    
friends(edges)


# ### 3. feladat [10p]
# 
# Az [unicef.txt](unicef.txt) szövegfájl a világ 5 év alatti népességének élelmezési helyzetéről tartalmaz adatokat. Az egyes sorok felméréseknek felelnek meg, a felmérések országonként időbeli sorrendben vannak felsorolva. Készíts programot, amely beolvassa az `unicef.txt` tartalmát, minden országra kiválasztja a legfrissebb felmérést, majd a legfrissebb felmérések alapján kiírja az alábbi statisztikákat:
# 
# 1. Az országok hányadrészében magasabb az `Underweight` indikátor az `Overweight` indikátornál?
# 2. Mely 5 országban a legmagasabb a `Severe Wasting` indikátor?
# 3. Régiónként (`United Nations Region`) mekkora a 20%-nál nagyobb `Stunting` indikátorral rendelkező országok aránya.

# # Pandas

# In[ ]:


import pandas as pd

df = pd.read_csv('C:\\Users\\Dorián\\PycharmProjects\\PythonVizsgaFelkészülés1Feladatok\\tables\\unicef.txt', sep='|')

df2 = df.groupby('Country').last()#Legfrissebb adatok kinyerése
#print(df.info())

#1. Az országok hányadrészében magasabb az Underweight indikátor az Overweight indikátornál?
print((df2['Underweight']>df2['Overweight']).mean())

#2. Mely 5 országban a legmagasabb a Severe Wasting indikátor?
print(df2['Severe Wasting'].sort_values(ascending=False).head(5))

#3. Régiónként (United Nations Region) mekkora a 20%-nál nagyobb Stunting indikátorral
# rendelkező országok aránya.
df2['Stunting'] = df2['Stunting'].str.replace(',', '.').astype(float) #Stunting oszlop object-ről float típusúvá alakítása.
print((df2['Stunting']>20).groupby(df2['United Nations Region']).mean())


#4. Hol a legalacsonyabb a túlsúlyos gyerekek aránya a 10%-nál alacsonyabb Wasting és Stunting indikátorral
#rendelkező országok között?
df2['Stunting'] = df2['Stunting'].str.replace(',', '.').astype(float) #Stunting oszlop object-ről float típusúvá alakítása.
df2['Wasting'] = df2['Wasting'].str.replace(',', '.').astype(float) #Wasting oszlop object-ről float típusúvá alakítása.
df2['Overweight'] = df2['Overweight'].str.replace(',', '.').astype(float) #Overweight oszlop object-ről float típusúvá alakítása.
print(df2[(df2['Wasting']<10) & (df2['Stunting']<10)]["Overweight"].idxmin())


# # Manuális nem pontos megoldás

# In[ ]:


filename = '/home/g14/uni/sze_python_programozas/data/unicef.txt'

def get_unicef(filename):
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
        data = [] 
        for line in lines:
            data.append(line[0:11]) 
        return data

def get_latest(datas):
    latest_data = []
    array = len(datas)
    for i in range(len(datas)):
        current = datas[i][0]
        if i == array - 1:
            latest_data.append(datas[i])
            break   
        next = datas[i+1][0]
        #print(f'Current: {current}')
        #print(f'Next: {next}')
        if next != current:
            latest_data.append(datas[i])
        else:
            continue
    return latest_data

def underw_bigger_overw(datas):
    counter = 0
    alldata = len(datas)    
    for data in datas:
        data
        if data[9] == '' or data[10] == '':
            continue
        else:
            underw = float(data[9].replace(',', '.'))
            overw = float(data[10].replace(',', '.'))
        if underw > overw:
            counter += 1
        else:
            continue
    percentage = counter / alldata * 100
    print(f'{percentage:.2f}%')

def get_stunting(datas):
    counter = 0
    alldata = len(datas)
    regions = {}
    for data in datas:
        if data[1] not in regions:
            regions[data[1]] = 1
        else:
            regions[data[1]] += 1
    regions = list(regions.keys())
    for region in regions:
        for data in datas:
            if data[1] == region:
                if data[8] == '':
                    continue
                if float(data[8].replace(',', '.')) > 20.0:
                    counter += 1
    percentage = counter / alldata * 100
    print(f'{percentage:.2f}%')
        

def top5_sevwast(datas):
    datas = sorted(datas, key=lambda x: x[7], reverse=True)
    for i in range(5):
        print(datas[i][0])
  

data = get_unicef(filename)
data = get_latest(data)
underw_bigger_overw(data)
top5_sevwast(data)
get_stunting(data)

