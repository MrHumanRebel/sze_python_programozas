#!/usr/bin/env python
# coding: utf-8

# 1. feladat
# 
# Készítsen programot az alábbi feladat megoldására!
# 
# Hány olyan egész szám van a [12,34567] intervallumban, amelyben a számjegyek sorrendjét megfordítva éppen magát a számot kapjuk (pl. ilyen számok: 33, 121, 4554; nem ilyen számok: 12, 122, 34567)?

# In[1]:


lista1 = []
lista2 = []

for i in range(12,34567):
    szamok=str(i)
    lista1.append(szamok)
    szamok2 =szamok[::-1]
    lista2.append(szamok2)

counter=0
for i in range(len(lista1)):
    if lista1[i] == lista2[i]:
        counter+=1
print(counter)


# # Részmegoldás

# In[27]:


def nums():
    counter = 0
    for i in range(12,34567,1):  
        num_as_str = str(i)

        akt_int = 0
        reverse_int= 0
        reverse = ""

        for j in range(len(num_as_str)-1,-1,-1):
            
            reverse = reverse + num_as_str[j]
            
        akt_int = int(num_as_str)
        reverse_int= int(reverse)
        #print("Akt szám: ", num_as_str)
        #print("Reverse szám: ", reverse_int)
        
        if akt_int == reverse_int:
            counter = counter + 1

    return counter
        
nums()


# 
# 
# 2. feladat
# 
# Készítsen függvényt az alábbi feladat megoldására!
# 
# A függvény bemenő paramétere egy lista, ami neveket tartalmaz. A lista helyes, ha nem üres, minden név különböző és mindegyik tartalmaz legalább egy angol (kis vagy nagy) betűt. A függvény ellenőrizze a lista helyességét és ezt adja is vissza eredményként! A függvény másik eredménye egy lista legyen, ami helytelen bemenő lista esetén legyen az üres lista, egyébként meg egy olyan lista, amely a neveknek egy véletlenszerű párosítását tartalmazza! A párosításban minden név pontosan egyszer szerepeljen, vagy az első vagy a második helyen (ahol a hely is legyen véletlenszerű)! Páratlan számú név esetén az egyik pár egyik helye maradjon üresen (pl. a példában ez a 2. pár első helye)!
# 
# Teszteljük a függvény működését, azaz hívjuk meg a függvényt (pl. az alábbi adatokkal), és írjuk ki a kapott eredmény(eke)t! A kiírt adatok elválasztására tabulátort használjunk és a pároknak legyen sorszáma!
# 
# Elvárt futási eredmény:
# 
#  1.	Sára 	Károly
#  2.		Irma
#  3.	Nóra	János
# 
# A nevek lista:
# 
# nevek = ['János', 'Károly', 'Irma', 'Sára', 'Nóra']

# In[2]:


nevek = ['János', 'Károly', 'Irma', 'Sára', 'Nóra']

import random


def ellenorzes_es_parositas(nevek):
    if len(nevek) == 0 or len(nevek) != len(set(nevek)):
        return False, []

    angol_betuk = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for nev in nevek:
        if not any(ch in angol_betuk for ch in nev):
            return False, []

    random.shuffle(nevek)
    parok = []
    if len(nevek) % 2 == 1:
        parok.append((nevek[0], ''))
        nevek = nevek[1:]

    for i in range(0, len(nevek), 2):
        parok.append((nevek[i], nevek[i + 1]))

    return True, parok


# Tesztelés
eredmeny, parok = ellenorzes_es_parositas(nevek)

if eredmeny:
    print("A nevek lista:")
    for i, par in enumerate(parok, start=1):
        print(f"{i}. párosítás: {par[0]} {par[1]}")
else:
    print("Helytelen bemenő lista.")


# # Részmegoldás

# In[39]:


import random

nevek = ['János', 'Károly', 'Irma', 'Sára', 'Nóra']

def helyes(nevek):
    helytelen = False   
    uj = []
    
    if len(nevek) % 2 != 0: #páratlan
        uj.append(" ")
    
    abc = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
           'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
    
    for i in range(len(nevek)):
        akt = nevek[i]
        for j in range(i+1,len(nevek)):
            if akt == nevek[j]:
                print("Nem minden név különböző!")
                helytelen = True
    
    for i in range(len(nevek)):
        akt = nevek[i]
        akt = nevek[i].upper()
        for j in range(len(nevek[i])-1):
            for x in range(len(abc)):
                if akt[0] not in abc:
                    print("Nem megfelelő név!")
                    helytelen = True
    szamlalo = 0
    while szamlalo != len(nevek):
        randomszam = random.randint(0, len(nevek)-1)
        selected = nevek[randomszam]
        if selected not in uj:
            uj.append(nevek[randomszam])
            szamlalo = szamlalo + 1

    if helytelen == True:
        return nevek
    else:
        return uj

uj_nevek = helyes(nevek)

line = 1
for i in range(0,len(uj_nevek),2):
    print(line,". parositas: ",uj_nevek[i], uj_nevek[i+1])
    line = line + 1


# 3. feladat
# 
# Készítsen programot az alábbi feladatok megoldására!
# 
# A log.txt fájl egy szerverhez intézett kérésekről tartalmaz adatokat.
# 
# A fájlban lévő adatok alapján határozza meg az alábbi statisztikákat!
# 
# a) Hány db különböző IP című számítógép használta a szervert?
# b) Melyik (IP című) számítógépről jött a legtöbb kérés és mennyi?
# c) Melyik az az 5 számítógép, amelyiken a leghosszabb ideig 'dolgoztak'? A 'dolgozás' idejét az adott számítógéphez tartozó, időben legelső és legutolsó kérés közt eltelt idő adja! Olyan eredménylistát készítsen, amelyben szerepel az adott számítógépek IP címe, az első és az utolsó kérés ideje, valamint a köztük eltelt idő (óó:pp:mm alakban)! A lista az eltelt idő szerint legyen csökkenően rendezve!
# 

# In[40]:


import pandas as pd
import datetime as dt

df = pd.read_csv('/home/g14/uni/sze_python_programozas/data/log.txt',sep=';')

#a) Hány db különböző IP című számítógép használta a szervert?
szgep = df.groupby('ip')['ip'].size().count()
print(f'{szgep} db különböző ip című számítógépet használ a szerver.')

#b) Melyik (IP című) számítógépről jött a legtöbb kérés és mennyi?
szam = df.groupby('ip')['ip'].size().max()
ipsor = df.groupby('ip')['ip'].size().idxmax()
print(f"{ipsor} ip című számítógépről jött a legtöbb hívás, szám szerint: {szam}.")

#c) Melyik az az 5 számítógép, amelyiken a leghosszabb ideig 'dolgoztak'?
df['time'] = pd.to_datetime(df['time'], format='%H:%M:%S')
timemaximum = df.groupby('ip')['time'].max()
timeminimum = df.groupby('ip')['time'].min()
kulonbseg = timemaximum-timeminimum
print(kulonbseg.sort_values(ascending = False).head(5))


# # Manuális nem pontos részmegoldás

# In[42]:


import datetime


filename = '/home/g14/uni/sze_python_programozas/data/log.txt'

def get_data(filename):
    with open(filename, 'r') as f:
        # skip the firstline
        f.readline()
        lines = f.readlines()
        # read into a list  split by | return the list 
        lines = [line.split(';') for line in lines]    
        # remove the newline character from the last element of each line
        for line in lines:
            line[-1] = line[-1].strip()
            continue
        data = [] 
        for line in lines:
            data.append(line) 
        return data



def diff_ip(data):
    
    different_ips = []
    counter = 0
    
    for i in range(len(data)):
        if data[i][0] not in different_ips:
            different_ips.append(data[i][0])
            counter = counter + 1      
    print("Hány db különböző IP című számítógép használta a szervert?")
    print(counter)
    return counter



def get_top_query(data):
    different_ips = []
    max = 0
    ip = ""

    for i in range(len(data)):
        if data[i][0] not in different_ips:
            different_ips.append(data[i][0])
    
    for i in range(len(different_ips)):
        counter = 0
        for j in range(len(data)):
            if different_ips[i] in data[j][0]:
                counter = counter + 1
        if counter > max:
            max = counter
            ip = different_ips[i]
    print("Melyik (IP című) számítógépről jött a legtöbb kérés és mennyi?")
    print(ip, ' : ', max, ' db kérés')
    return ip, max



def top5(data):
    different_ips = []
    start = []
    stop = []    
    
    for i in range(len(data)):
        if data[i][0] not in different_ips:
            different_ips.append(data[i][0])
      
    for i in range(len(different_ips)):
        elso = False
        for j in range(len(data)):
            if elso == False and different_ips[i] == data[j][0]:
                elso = True
                start.append(data[j][1])
                #print(data[j][1])
        elso = False
        for j in range(len(data)-1,0,-1):
            if elso == False and different_ips[i] == data[j][0]:
                elso = True
                stop.append(data[j][1])
                #print(data[j][1])
    
            
                
                
data = get_data(filename)
diff_ip(data)
print('\n')
get_top_query(data)
print('\n')
top5(data)

