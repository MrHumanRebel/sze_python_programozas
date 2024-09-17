#!/usr/bin/env python
# coding: utf-8

# # 1. feladat [8p]
# 
#  Alex és Bob és Charlie közös programot szerveznek. Aszabad időintervallumaik az intervals szótárban vannak megadva. Készítsünk programot, amely kiszámítja, hogy hány olyan nap van, amikor mindhárman ráérnekl Az intervallumok zártak, azaz a végpontok szabad időpontnak tekintendők. A program ne csak a megadott intervals adatszerkezetre működjön, hanem tetszőleges, ugyanilyen formátumú bemenetre is! 

# In[ ]:


import datetime as dt

intervals = {
'Alex': [('2020-06-20','2020-06-23'), ('2020-06-30', '2020-07-05')],
'Bob' : [('2020-06-18','2020-06-21'), ('2020-06-24','2020-07-01'), ('2020-07-03', '2020-07-04')],
'Charlie': [('2020-06-21', '2020-06-28'), ('2020-07-02', '2020-07-10')],
}

common_days = set()
for intervals_list in intervals.values():
    for interval in intervals_list:
        startdate = dt.datetime.strptime(interval[0], '%Y-%m-%d').date()
        enddate = dt.datetime.strptime(interval[1], '%Y-%m-%d').date()
        common_days |= set([startdate + dt.timedelta(days=x) for x in range((enddate-startdate).days+1)])
        
freedays = 0
for day in common_days:
    counter = 0
    for intervals_list in intervals.values():
        for interval in intervals_list:
            startdate = dt.datetime.strptime(interval[0], '%Y-%m-%d').date()
            enddate = dt.datetime.strptime(interval[1], '%Y-%m-%d').date()
            if startdate <= day <= enddate:
                counter += 1
    if counter == 3:
        freedays += 1
  
print(freedays)


# # Részmegoldások

# In[ ]:


import datetime as dt

intervals = {
'Alex': [('2020-06-20','2020-06-23'), ('2020-06-30', '2020-07-05')],
'Bob' : [('2020-06-18','2020-06-21'), ('2020-06-24','2020-07-01'), ('2020-07-03', '2020-07-04')],
'Charlie': [('2020-06-21', '2020-06-28'), ('2020-07-02', '2020-07-10')],
}
people_counter = 0
names = list(intervals.keys())

min = 5000
for i in intervals.values():
    people_counter += 1
    ok_counter = 0
    for j in i:
        start = dt.datetime.strptime(j[0], '%Y-%m-%d')
        end = dt.datetime.strptime(j[1], '%Y-%m-%d')
        for k in (i):
            new_start = dt.datetime.strptime(j[0], '%Y-%m-%d')
            new_end = dt.datetime.strptime(j[1], '%Y-%m-%d')
            if new_start >= start and new_end <= end:
                ok_counter += 1
    ok_counter = ok_counter - 1 # mert a saját intervallumát is bele számolja
    if ok_counter < min:
        min = ok_counter
            
print(min)  


# # 2. feladat [12p] 
# 
# A china.txt Kína mezőgazdaságáról tartalmaz összesitő adatokat, az 1949 és 2008 közötti időszakból. Készitsünk programot, amely beolvassa a szövegfájl tartalmát, majd válaszol az alábbi kérdésekre! 
# - Összesen hány tonna trágyát használtak a 60-as években? (Áru: Total fertilizer consumption ) 
# - Melyik évben volt a legmagasabb a mezőgazdaságban dolgozók száma? (Áru: Ag employment (primary industry) ) 
# - A rizstermeles (Kategória: Crop production , Áru: Rice ) melyik évben hányszorosa volt az 1949-es értéknek? 
# - 2007-ben melyik 5 terménynek volt átlagosan a legnagyobb a hektáronkénti hozama? (A termelési mennyiségek a crop production , a vetési területek a crop sown area kategóriában van megadva.) 
# 

# # Pandas

# In[2]:


import pandas as pd

df = pd.read_csv("/home/g14/uni/sze_python_programozas/data/china.txt", delimiter="\t", decimal=",", skiprows=1)

# 1. feladat
fertilizer_usage = df.loc[(df["Ev"].between(1960, 1970, inclusive="left")) & (df["Aru"] == "Total fertilizer consumption")]
fertilizer_tons = fertilizer_usage["Mennyiseg"].sum() * 1000
print(f"{fertilizer_tons} t\n")

# 2. feladat
max_ag_employment = df.loc[df["Aru"] == "Ag employment (primary industry)"].max()
print(f"{max_ag_employment['Ev']}\n")

# 3. feladat
rice_prod = df.loc[(df["Kategoria"] == "Crop production") & (df["Aru"] == "Rice")].copy()
rice_prod_base_quantity = rice_prod.loc[df["Ev"] == 1949, "Mennyiseg"].item()

rice_prod["1949-hez kepest"] = rice_prod["Mennyiseg"].divide(rice_prod_base_quantity)
rice_prod_diff = rice_prod[['Ev', '1949-hez kepest']]
print(f"{rice_prod_diff}\n")

# 4. feladat
crop_prod_2007 = df.loc[(df["Ev"] == 2007) & (df["Kategoria"] == "Crop production")][["Aru", "Mennyiseg"]].copy()
crop_prod_2007 = crop_prod_2007.rename(columns={"Mennyiseg": "1000 t"})

crop_sown_area_2007 = df.loc[(df["Ev"] == 2007) & (df["Kategoria"] == "Crop sown area")][["Aru", "Mennyiseg"]].copy()
crop_sown_area_2007 = crop_sown_area_2007.rename(columns={"Mennyiseg": "1000 ha"})

crop_data_2007 = pd.merge(crop_prod_2007, crop_sown_area_2007, on="Aru")
crop_data_2007["Atlag hozam (t / ha)"] = crop_data_2007["1000 t"].divide(crop_data_2007["1000 ha"]).multiply(1000)

top_5_crops = crop_data_2007.sort_values(by="Atlag hozam (t / ha)", ascending=False)[:5]
print(f"4. feladat:\n {top_5_crops}")


# # Manuális nem pontos megoldás

# In[ ]:


filename = '/home/g14/uni/sze_python_programozas/data/china.txt'

def get_data(filename):
    with open(filename, 'r') as f:
        # skip the first two line
        for i in range(2):
            f.readline()
        lines = f.readlines()
        # read into a list  split by tab
        lines = [line.split('\t') for line in lines]    
        # remove the newline character from the last element of each line
        for line in lines:
            line[-1] = line[-1].strip()
            continue
        data = [] 
        for line in lines:
            data.append(line) 
        return data

def tragya_60s(data):
    sum = 0
    for item in data:
        if item[2] == 'Total fertilizer consumption' and int(item[0])>=1960 and int(item[0])<=1969:
            sum += int(item[3])
    print(sum)

def ag_workers(data):
    stats = {}
    for item in data:
        if item[2] == 'Ag employment (primary industry)':
            year = item[0]
            workers = item[3]
            if year not in stats:
                stats[year] = workers
            else:
                if workers > stats[year]:
                    stats[year] = workers
    stats = sorted(stats.items(), key=lambda x: x[1], reverse=True)
    print(stats)
    
def rice_1949_base(data):
    base = 0
    stats = {}
    for item in data:
        if item[1] == 'Crop production' and item[2] == 'Rice' and item[0] == '1949':
            base = float(item[3].replace(',','.'))
            break
    for item in data:
        if item[1] == 'Crop production' and item[2] == 'Rice':
            perbase = float(item[3].replace(',','.')) / base
            stats[item[0]] = perbase
    print(stats)
    
def top5_hekt_2007(data):
    crops = {}
    sown = {}
    for item in data:
        if item[0] == '2007' and item[1] == 'Crop production':
            if item[2] not in crops:
                crops[item[2]] = float(item[3].replace(',','.'))
            else:
                crops[item[2]] += float(item[3].replace(',','.'))
        if item[0] == '2007' and item[1] == 'Crop sown area':
            if item[2] not in sown:
                sown[item[2]] = float(item[3].replace(',','.'))
            else:
                crops[item[2]] += float(item[3].replace(',','.'))
    mean = {}
    for item in crops:
        if item in sown and item in crops:
            mean[item] = crops[item] / sown[item]
    mean = sorted(mean.items(), key=lambda x: x[1], reverse=True)
    print(mean) 
    
    
    
data = get_data(filename)
tragya_60s(data)
ag_workers(data)
rice_1949_base(data)
top5_hekt_2007(data)

