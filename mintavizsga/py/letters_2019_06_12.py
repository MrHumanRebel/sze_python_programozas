#!/usr/bin/env python
# coding: utf-8

# # 1. feladat [8p] 
# Készíts programot, amely kér a felhasználótól egy évszámot, majd megadja, hogy az adott évben hány pénteki nap esett 13-ára! 

# In[5]:


import datetime as dt

year = int(input("Add meg az évet: "))
counter = 0

for month in range(1, 13):
    day = dt.date(year, month, 13)
    #  0: hétfő, 1: kedd, 2: szerda, 3: csütörtök, 4: péntek, 5: szombat, 6: vasárnap
    if day.weekday() == 4:
        counter += 1
        
print(f"A(z) {year}. évi péntek 13-ak száma: {counter}")


# # 2. feladat [10p] 
# A letters objektum egy kisbetűkből álló négyzetet tartalmaz. A sorok sztringként vannak reprezentálva, és egy listába vannak egymás után fűzve. Készíts programot, amely kiírja, hogy mely oszlopban található a legtöbb magánhangzó! A program ne csak a letters objektumra, hanem tetszőleges, ugyanilyen formátumú, bemenetre is működjön! 

# In[6]:


letters = [ "tüzesensütleany", "árinapsugáraazé", "gtetejérőlajuhá", "szbojtárrafölös", "legesdologsütni", "eolynagyonajuhá", "sznakúgyisnagym", "elegevagyonszer", "elemtüzeégfiata", "lszivébenugyleg", "eltetianyájtafa", "luvégenfaluvége", "nnyájamigszerte", "legelészőaddigs", "ubájánafűbenhev" ]
 
# Először is meg kell találnunk, hogy hány oszlop van az adott négyzetben
num_columns = len(letters[0])

# Létrehozunk egy üres listát, amelyben minden oszlophoz hozzárendeljük a magánhangzók számát
vowels_per_column = [0] * num_columns

# Végigmegyünk minden oszlopon és soron, majd megszámoljuk a magánhangzókat az adott oszlopban
for col in range(num_columns):
    for row in range(len(letters)):
        if letters[row][col] in "aeiouáéíóöőúüű":
            vowels_per_column[col] += 1

# Megkeressük a legtöbb magánhangzót tartalmazó oszlop sorszámát
max_vowels_index = vowels_per_column.index(max(vowels_per_column))

print(f"A legtöbb magánhangzó a(z) {max_vowels_index+1}. oszlopban található, {max(vowels_per_column)} db magánhangzóval.")

