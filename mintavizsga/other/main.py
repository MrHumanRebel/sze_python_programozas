#A china.txt Kína mezőgazdaságáról tartalmaz összesitő adatokat, az 1949 és 2008 közötti időszakból.
# Készitsünk programot, amely beolvassa a szövegfájl tartalmát, majd válaszol az alábbi kérdésekre!

#1. Összesen hány tonna trágyát használtak a 60-as években? (Áru: Total fertilizer consumption )
#2. Melyik évben volt a legmagasabb a mezőgazdaságban dolgozók száma? (Áru: Ag employment (primary industry) )
#3. A rizstermeles (Kategória: Crop production , Áru: Rice ) melyik évben hányszorosa volt az 1949-es értéknek?
#4. 2007-ben melyik 5 terménynek volt átlagosan a legnagyobb a hektáronkénti hozama?
# (A termelési mennyiségek a crop production , a vetési területek a crop sown area kategóriában van megadva.)

import pandas as pd

df = pd.read_csv('C:\\Users\\Dorián\\PycharmProjects\\PythonVizsgaFelkészülés1Feladatok\\tables\\china.txt', sep='\t', skiprows=1)
print(df.info())
print(df)
#1. Összesen hány tonna trágyát használtak a 60-as években? (Áru: Total fertilizer consumption )

total_fertilizer = df[(df['Ev'] >= 1960) & (df['Ev'] <= 1969)&(df['Aru']=='Total fertilizer consumption')].sum()
#print(f"Az 1960-as években összesen {total_fertilizer} tonna trágyát használtak.")













