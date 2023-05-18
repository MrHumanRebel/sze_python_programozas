#!/usr/bin/env python
# coding: utf-8

# # 1. feladat [8p]
# Tomi egy ’r’ méter sugarú, kör alakú tűzrakó helyet szeretne szegélykővel körbekeríteni. Az áruházban 85 cm és 100 cm hosszúságú szegélykövek kaphatók. A körbekerítésnél Tomi vagy csak 85 cm-es vagy csak 100 cm-es szegélyköveket használ, és szabályos sokszög alakban helyezi el őket. Az a cél, hogy a szegély kerülete a lehető legkisebb legyen, de a szegély alkotta sokszögből ne lógjon ki az ’r’ sugarú kör. Készítsünk programot, amely bekéri ’r’ értékét, majd kiszámítja, hogy melyik hosszúságú szegélykőből hányat kell venni, hogy optimális körbekerítést kapjunk! Segítség: Az ’a’ oldalhosszúságú szabályos sokszög beírt körének a sugara
# (a/2)/tg(π/n)
# 

# In[16]:


import math

eredeti_r = float(input('Adja meg a szegélykő sugárát cm-ben: '))
optim = {}

for n in range(12,2,-1): # 3 szögletűtől 12 szögletűig
    eredeti_kerulet = 2 * eredeti_r * math.pi
    szegely100 = 0
    szegely85 = 0
    
    a = 2 * eredeti_r * math.sin(math.pi/n) #Megvan az eredeti kör kerülete, adott N számú szabályos sökszög oldalhossza kellene ide
    szokszog_r = (a/2)/(math.tan(math.pi/n))
    print(f'{n} szögletű szegélykő belső sugara: {szokszog_r:.2f} cm')
        
    while szokszog_r >= 100:
        szegely100 += 1
        szokszog_r -= 100
    while szokszog_r >= 85:
        szegely85 += 1
        szokszog_r -= 85
    if szokszog_r < 85:
        szegely85 += 1
    optim[n] = {'100': szegely100, '85': szegely85}
    
print('\n')
print(optim)


# # 2. feladat [12p]
# 
# Disclaimer: Nem rendelkezünk az eredeti adatokkal, ezért generált minta adatokat használunk fel!
# 
# A dog_breeds.txt szövegfájl kutyafajták jellemzőit tartalmazza az American Kennel Club leírása alapján. Az adatok felnőtt példányokra vonatkoznak. Készítsünk programot, amely beolvassa a szövegfájl tartalmát, majd válaszol az alábbi kérdésekre!
# - Melyik az 5 legnehezebb fajta a weight_low_lbs oszlop alapján?
# -	Melyek azok a fajták, ahol a maximális és a minimális testmagasság között legalább 25 cm a különbség? (1 hüvelyk = 2,54 cm)
# -	Az átlagosnál alacsonyabb fajták között melyik a legnagyobb súlyú? (a height_low_inches és a weight_low_lbs oszlop alapján)
# -	Milyen kezdőbetűjű fajtából hány darab van az adathalmazban?
# 

# # Pandas

# In[ ]:


import pandas as pd

df = pd.read_csv('/home/g14/uni/sze_python_programozas/data/dog_breeds.txt', sep ='|')

#print(df.info())

#1. Melyik az 5 legnehezebb fajta a weight_low_lbs oszlop alapján?
print(df.groupby('Breed')['Weight_low_lbs'].max().sort_values(ascending=False).head(5))

#2. Melyek azok a fajták, ahol a maximális és a minimális testmagasság között legalább 25 cm a különbség? (1 hüvelyk = 2,54 cm)
df['Height_high_inches'] = df['Height_high_inches'].apply(lambda x: x * 2.54)  # cm-re váltás
df['Height_low_inches'] = df['Height_low_inches'].apply(lambda x: x * 2.54)    # cm-re váltás
filtered_df = df[(df['Height_high_inches'] - df['Height_low_inches']) >= 25]['Breed']
print(filtered_df)

#3. Az átlagosnál alacsonyabb fajták között melyik a legnagyobb súlyú?
# (a height_low_inches és a weight_low_lbs oszlop alapján)
avg_height = (df['Height_low_inches'].mean())
shorter_breeds = df[df['Height_low_inches'] < avg_height]
max_weight_breed = shorter_breeds.loc[shorter_breeds['Weight_low_lbs'].idxmax()]['Breed']
print(max_weight_breed)

#4. Milyen kezdőbetűjű fajtából hány darab van az adathalmazban?
letter_count = df.groupby(df['Breed'].str[0])['Breed'].count()
print(letter_count)


# # Manuális nem pontos megoldás

# In[ ]:


filename = '/home/g14/uni/sze_python_programozas/data/dog_breeds.txt'

def get_data(filename):
    with open(filename, 'r') as f:
        # skip the first two line
        for i in range(2):
            f.readline()
        lines = f.readlines()
        # read into a list  split by , 
        lines = [line.split('|') for line in lines]    
        # remove the newline character from the last element of each line
        for line in lines:
            line[-1] = line[-1].strip()
            continue
        data = [] 
        for line in lines:
            data.append(line) 
        return data

def weighty(data):
    data = sorted(data, key = lambda x: x[3], reverse=True)
    print(data[0:5])

def min25cm(data):
    dogs = {}
    for item in data:
        if (float(item[2])-float(item[1]))*2.54 >= 25:
            dogs[item[0]] = item[1], item[2]
    print(dogs)


def avg_height(data):
    sum = 0
    counter = 0
    for item in data:
        sum += float(item[1])
        counter += 1
    avg = sum/counter
    return avg


def high_weight(data):
    dog = []
    avg = avg_height(data)
    max = 0
    for item in data:
        if float(item[1]) < avg:
            if float(item[3]) > max:
                max = float(item[3])
                dog = item
    print(dog)
    
def start_letter(data):
    letter_counts = {}
    letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for letter in letter_list:
        for item in data:
            current_letter = item[0][0].lower()
            if current_letter == letter:
                if current_letter not in letter_counts:
                    letter_counts[current_letter] = 1
                else:
                    letter_counts[current_letter] += 1           
    print(letter_counts)   


data = get_data(filename)
weighty(data)
min25cm(data)
high_weight(data)
start_letter(data)

