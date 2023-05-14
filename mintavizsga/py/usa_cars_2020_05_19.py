#!/usr/bin/env python
# coding: utf-8

# # 1. feladat [8p]
# A data objektum egy nullákból és egyesekból álló négyzetet tartalmaz, listák listájaként reprezentálva. Készítsünk programot, amely megadja leghosszabb csupa nullából álló átlós vonal hosszát a négyzetben! A program ne csak megadott data objektumra, hanem tetszőleges, ugyanilyen formátumú bemenetre is!

# In[30]:


data = [[1,0,1,0],
        [1,0,0,1],
        [0,1,1,0],
        [0,0,0,0]]

rows = len(data)
cols = len(data[0])

max = 0

for i in range(rows):
    sum = 0
    for j in range(cols):
        if data[i][j] == 0:
            for k in range(1, min(rows-i, cols-j)):
                if sum == 0: 
                    sum += 1
                if data[i+k][j+k] == 0:
                    sum += 1
    if sum > max:
        max = sum
    sum = 0
    
    for j in range(cols-1, -1, -1):
        if data[i][j] == 0:
            for k in range(1, min(rows-i, j+1)):
                if sum == 0: 
                    sum += 1
                if data[i+k][j-k] == 0:
                    sum += 1
    if sum > max:
        max = sum

print(f"Legrövidebb csupa nullából álló átlós vonal hossza: {max}")


# # 2. feladat [12 p]
# 
# Disclaimer: Nem rendelkezünk az eredeti adatokkal, ezért generált minta adatokat használunk fel!
# 
# Az usa_cars.txt szövegfájl eladásra meghirdetett autókról és autóalkatrészekről tartalmaz adatokat. Készítsünk programot, amely beolvassa a szövegfájl tartalmát, majd válaszol az alábbi kérdésekre:
# 
# - Melyik a 3 legrégebbi évjáratú termék?
# - Melyik a ledrágább Audi, BMW, Chevrolet, Ford, Nissan, Maserati és Toyota?
# - Melyik államban árulják a legtöbb piros Fordot?
# - Hányadik leggyakoribb szín az adathalazban a piros?
# 

# # Pandas

# In[ ]:


import pandas as pd

df = pd.read_csv('C:\\Users\\Dorián\\PycharmProjects\\PythonVizsgaFelkészülés1Feladatok\\tables\\usa_cars.txt', sep =',')
#print(df.info())
#Melyik a 3 legrégebbi évjáratú termék?
print(df.sort_values('Evjarat').head(3))

#Melyik a ledrágább Audi, BMW, Chevrolet, Ford, Nissan, Maserati és Toyota?
audi_rows = df[df['Marka']=='Audi']
print(audi_rows.loc[audi_rows['Ar'].idxmax()])
print()
bmw_rows = df[df['Marka']=='BMW']
print(bmw_rows.loc[bmw_rows['Ar'].idxmax()])
print()
chev_rows = df[df['Marka']=='Chevrolet']
print(chev_rows.loc[chev_rows['Ar'].idxmax()])
print()
ford_rows = df[df['Marka']=='Ford']
print(ford_rows.loc[ford_rows['Ar'].idxmax()])
print()
nissan_rows = df[df['Marka']=='Nissan']
print(nissan_rows.loc[nissan_rows['Ar'].idxmax()])
print()
mas_rows = df[df['Marka']=='Maserati']
print(mas_rows.loc[mas_rows['Ar'].idxmax()])
print()
toy_rows = df[df['Marka']=='Toyota']
print(toy_rows.loc[toy_rows['Ar'].idxmax()])

#Melyik államban árulják a legtöbb piros Fordot?
red_fords= df[(df['Marka']=='Ford') & (df['Szin']=='Red')]
state_counts = red_fords['Allam'].value_counts()
print(state_counts.idxmax())

#Hányadik leggyakoribb szín az adathalazban a piros?
color_counts = df['Szin'].value_counts() #Összes szín, melyikből hány darab van.
red_count = color_counts.get('Red', 0) #Ezekből a pirosak.
red_ratio = red_count/color_counts.sum() #A pirosak hányada
red_rank = (color_counts >= red_count).sum() #A pirosak a 9. helyen állnak.
print(red_rank)


# # Manuális nem pontos megoldás

# In[3]:


filename = '/home/g14/uni/sze_python_programozas/data/usa_cars.txt'


def get_data(filename):
    with open(filename, 'r') as f:
        # skip the first line
        f.readline()
        lines = f.readlines()
        # read into a list  split by | return the list 
        lines = [line.split(',') for line in lines]    
        # remove the newline character from the last element of each line
        for line in lines:
            line[-1] = line[-1].strip()
            continue
        data = [] 
        for line in lines:
            data.append(line) 
        return data
        
def oldest_item(data):
    data = sorted(data, key= lambda x: x[1])
    print(f"A top 5 legrégebben gyártott termék: {data[0:3]}")
    
def highest_price(data, brand):
    curr_brand = []
    for item in data:
        if item[0] == brand:
            curr_brand.append(item)
    curr_brand = sorted(curr_brand, key= lambda x: x[2], reverse=True)
    print(f"A legdrágább {brand}: {curr_brand[0]}")
        
    
def red_ford(data):
    ford_red_states = {}
    for item in data:
        if item[0] == 'Ford' and item[4] == 'Red':
            if item[3] not in ford_red_states:
                ford_red_states[item[3]] = 1
            else:
                ford_red_states[item[3]] += 1
    
def red_appearence(data):
    colours = {}
    sum = 0
    for item in data:
        if item[4] not in colours:
            colours[item[4]] = 1
            sum += 1
        else:
            colours[item[4]] += 1
            sum += 1
    for item in colours:
        colours[item] = colours[item]/sum
    colours = sorted(colours.items(), key= lambda x: x[1], reverse=True)
    idx = 0
    for item in colours:
        idx += 1
        if item[0] == 'Red':
            print(f"A piros szín a {idx}. leggyakoribb szín a listában.")     
    

data = get_data(filename)
oldest_item(data)
print('\n')
highest_price(data, 'Audi')
highest_price(data, 'BMW')
highest_price(data, 'Chevrolet')
highest_price(data, 'Ford')
highest_price(data, 'Nissan')
highest_price(data, 'Maserati')
highest_price(data, 'Toyota')
print('\n')
red_ford(data)
print('\n')
red_appearence(data)



# # Random adat generálás

# In[32]:


import random
import string

# Autók márkái
brands = ["Audi", "BMW", "Chevrolet", "Ford", "Nissan", "Maserati", "Toyota", "Honda", "Hyundai", "Kia", "Lexus", "Mazda", "Mercedes", "Porsche", "Subaru", "Volkswagen", "Volvo"]

# Alkatrészek típusai
parts = ["Engine", "Transmission", "Brakes", "Suspension", "Tires", "Exhaust", "Interior", "Exterior"]

# Árak tartománya
min_price = 1000
max_price = 50000

# Államok listája
states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

# Színek listája
colors = ["White", "Black", "Gray", "Silver", "Red", "Blue", "Green", "Yellow", "Orange"]

# Fájl megnyitása írásra
with open("/home/g14/uni/sze_python_programozas/data/usa_cars.txt", "w") as f:
    # Generáljunk 1000 autót és alkatrészt
    for i in range(1000):
        # Véletlenszerűen válasszunk egy márkát és típust
        brand = random.choice(brands)
        part = random.choice(parts)
        
        # Véletlenszerűen generáljuk az évjáratot, árat, államot és színt
        year = random.randint(1990, 2023)
        price = random.randint(min_price, max_price)
        state = random.choice(states)
        color = random.choice(colors)
        
        # Írjuk ki az adatot a fájlba
        f.write(f"{brand},{year},{price},{state},{color},{part}\n")

