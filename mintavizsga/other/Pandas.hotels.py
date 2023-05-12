#A hotels.txt szövegfájl Las Vegas-i szállodák értékeléséről tartalmaz adatokat.
#Minden sor egy szállóvendég által kiosztott értékeléshez tartozik.
#Készíts programot, amely kiszámítja és kiírja az alábbi statisztikákat:
    #1. Hány db értékelés van összesen az egyes szállodákra vonatkozóan?
    #2. A szobák száma (Nr. rooms) alapján melyik az öt legnagyobb szálloda?
    #3. Hány ponttal magasabb a medencével (Pool) rendelkező szállodák átlagos értékelése
    #(Score) a többi szálloda átlagos értékelésénél?
    #4. Hány ponttal magasabb a teniszpályával(Tennis court) rendelkező szállodák átlagos értékelése
    #(Score) a többi szálloda átlagos értékelésénél?

import pandas as pd

df = pd.read_csv('C:\\Users\\Dorián\\PycharmProjects\\PythonVizsgaFelkészülés1Feladatok\\tables\\hotels.txt', sep =';')

#Szállodák csoportosítása  a nevük szerint.
gb = df.groupby('Hotel name')

#1. Hány db értékelés van összesen az egyes szállodákra vonatkozóan?
print(gb['Score'].count())

#2. A szobák száma (Nr. rooms) alapján melyik az öt legnagyobb szálloda?
print(gb['Nr. rooms'].first().sort_values(ascending=False).head(5))

#3. Hány ponttal magasabb a medencével (Pool) rendelkezeő szállodák átlagos értéklése
    #(Score) a többi szálloda átlagos értékelésénél?
df2 = df.groupby(['Hotel name', 'Pool'])['Score'].mean().reset_index()#Hotelek és medencék, értékelések átlaga
ertek = df2.groupby("Pool")["Score"].mean()#Medencével rendelkező és nem rendelkező hotelek összesített átlaga
print(ertek['YES'] - ertek['NO'])#Pont különbség

#4. Hány ponttal magasabb a teniszpályával(Tennis court) rendelkező szállodák átlagos értékelése
    #(Score) a többi szálloda átlagos értékelésénél?
df2 = df.groupby(['Hotel name', 'Tennis court'])['Score'].mean().reset_index()#Hotelek és tenisz pályák, értékelések átlaga
ertek = df2.groupby("Tennis court")["Score"].mean()#Tenisz pályával rendelkező és nem rendelkező hotelek összesített átlaga
print(ertek['YES'] - ertek['NO'])#Pont különbség