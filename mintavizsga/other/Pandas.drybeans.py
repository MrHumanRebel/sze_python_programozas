#A dry_bean.txt (dry_bean.txt) szövegfájl 13 611 db lefényképezett babszemről tartalmaz adatokat.
#Minden sor egy babszemnek felel meg. Az első 16 oszlop méret- és alakjellemzőket tartalmaz (pl.
#kerület, terület, konvex burok területe, excentricitás), az utolsó oszlop pedig a növény fajtáját adja
#meg (SEKER, BARBUNYA, BOMBAY, CALI, DERMASON, HOROZ vagy SIRA). Készítsünk
#programot, amely beolvassa a fájl tartalmát, majd válaszol az alábbi kérdésekre!

#1. Mi az egyes fajtákhoz tartozó babszemek százalékos aránya?
#2. Melyik fajta szemeinek a legnagyobb az átlagos excentricitása?
#3. Hány konvex alakú babszem található az adathalmazban?

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
