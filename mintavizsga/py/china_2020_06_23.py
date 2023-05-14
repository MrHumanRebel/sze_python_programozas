#!/usr/bin/env python
# coding: utf-8

# # 1. feladat [8p]
# 
#  Alex és Bob és Charlie közös programot szerveznek. Aszabad időintervallumaik az intervals szótárban vannak megadva. Készítsünk programot, amely kiszámítja, hogy hány olyan nap van, amikor mindhárman ráérnekl Az intervallumok zártak, azaz a végpontok szabad időpontnak tekintendők. A program ne csak a megadott intervals adatszerkezetre működjön, hanem tetszőleges, ugyanilyen formátumú bemenetre is! 

# In[3]:


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


# In[4]:


""" for people in intervals.values():
    print(names[people_counter])
    people_counter += 1
    for date in people:
        for current in date:
            current = dt.datetime.strptime(current, '%Y-%m-%d')
            print(current) """


""" max_start = dt.datetime.strptime('1850-01-01', '%Y-%m-%d')
max_stop  = dt.datetime.strptime('1850-01-01', '%Y-%m-%d')
for people in intervals.values():
    for date in people:
        start_date = dt.datetime.strptime(date[0], '%Y-%m-%d')
        stop_date = dt.datetime.strptime(date[1], '%Y-%m-%d')
        if start_date > max_start:
            max_start = start_date
        if stop_date > max_stop:
            max_stop = stop_date
        
print(max_start)  
print(max_stop)
print('\n')

people_counter = 0
all_ok = 0
for people in intervals.values():
    ok = 0
    print(names[people_counter])
    people_counter += 1
    for date in people:
        start_date = dt.datetime.strptime(date[0], '%Y-%m-%d')
        stop_date = dt.datetime.strptime(date[1], '%Y-%m-%d')
        print(start_date)
        print(stop_date)
        if start_date >= max_start and stop_date <= max_stop:
            ok += 1
            print('ok')
    if ok > 0:
        all_ok += 1

print(all_ok) """


# # 2. feladat [12p] 
# 
# A china.txt Kína mezőgazdaságáról tartalmaz összesitő adatokat, az 1949 és 2008 közötti időszakból. Készitsünk programot, amely beolvassa a szövegfájl tartalmát, majd válaszol az alábbi kérdésekre! 
# - Összesen hány tonna trágyát használtak a 60-as években? (Áru: Total fertilizer consumption ) 
# - Melyik évben volt a legmagasabb a mezőgazdaságban dolgozók száma? (Áru: Ag employment (primary industry) ) 
# - A rizstermeles (Kategória: Crop production , Áru: Rice ) melyik évben hányszorosa volt az 1949-es értéknek? 
# - 2007-ben melyik 5 terménynek volt átlagosan a legnagyobb a hektáronkénti hozama? (A termelési mennyiségek a crop production , a vetési területek a crop sown area kategóriában van megadva.) 
# 

# In[37]:


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



