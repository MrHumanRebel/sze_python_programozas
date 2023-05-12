#A houston.txt szövegfájl a texasi Houston időjárásról tartalmaz napi bontású adatokat.
# A hőmérséklet értékek (* _hőm) Fahrenheit-fokban,
# a csapadék mennyiségének értékei (* _csap) hüvelyben vannak megadva.
# A rekordok és az év adott napjához tartozó átlagok az 1880 óta eltelt időszakra vonatkoznak.
# Készítsünk programot, amely beolvassa a szövegfájl tartalmát, majd válaszol a következő kérdésekre:

#1. Mikor volt a legnagyobb az eltérés a napi maximális és a napi minimális hőmérséklet között?
#2. Celcius fokban kifejezve mennyi volt a legalancsonyabb és legmagasabb hőmérséklet,
# amit Houstonban valaha mértek? (C = (F - 32) * 5/9) Melyik évben mérték ezt?
#3. Melyik hónapban mennyi volt az összes csapadék mm-ben? (1 hüvely = 25.4 mm)

import pandas as pd

df = pd.read_csv('C:\\Users\\Dorián\\PycharmProjects\\PythonVizsgaFelkészülés1Feladatok\\tables\\houston.txt', sep='|', skiprows=3)
#print(df.info())

#1. Mikor volt a legnagyobb az eltérés a napi maximális és a napi minimális hőmérséklet között?

df['hőmkül'] = abs(df['napi_min_hőm']-df['napi_max_hőm'])#Hőmérséklet különbségek abszolútértéke
maxhömkülindex = df['hőmkül'].idxmax() #Megkeressük a hőmérsékletek közül a maximális értéknek az indexét.
print('Dátum:', df.loc[maxhömkülindex]['dátum'], 'Maximális eltérés:', max(df['hőmkül'])) #Vissza adjuk az index szerinti sort.

#2. Celcius fokban kifejezve mennyi volt a legalacsonyabb és legmagasabb hőmérséklet,
# amit Houstonban valaha mértek? (C = (F - 32) * 5/9) Melyik évben mérték ezt?

rekordmin = df['rekord_min_hőm'].min()
rekordmin = ((rekordmin-32)* (5/9))
rekordminidx = df['rekord_min_hőm'].idxmin()
rekordminev = df.loc[rekordminidx]['rekord_min_hőm_év']
print(f'A rekord minimum hőmérséklet: {rekordmin}°C méghozzá {rekordminev}. évben')

rekordmax = df['rekord_max_hőm'].max()
rekordmax = ((rekordmax-32)* (5/9))
rekordmaxidx = df['rekord_max_hőm'].idxmax()
rekordmaxev = df.loc[rekordmaxidx]['rekord_max_hőm_év']
print(f'A rekord maximum hőmérséklet: {rekordmax}°C méghozzá a {rekordmaxev}. évben')

#3. Melyik hónapban mennyi volt az összes csapadék mm-ben? (1 hüvely = 25.4 mm)
import datetime as dt

df['napi_csap_mm'] = df['napi_csap']*25.4 #Napi csapadék mennyiség hüvelyben.
df['honap'] = pd.to_datetime(df['dátum']).dt.month #Hónap oszlop létrehozása és dátum oszlop dátummá alakítása.
honapok = df.groupby("honap").sum()["napi_csap_mm"]#Havi csapadékmennyiségek összeadása.
print(honapok)


