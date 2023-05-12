#A covid19_stats.txt (covid19_stats.txt) szövegfájl a COVID-19 vírussal kapcsolatos statisztikákat
# tartalmaz a 2020.01.23 és 2021.05.11 közötti időszakból, országonkénti bontásban.
# Minden sor azt adja meg, hogy az adott napon az adott országban hány
# igazolt fertőzés történt ( Confirmed ), hányan gyógyultak meg ( Recovered ) illetve hányan hunytak el
# a vírus miatt ( Deaths ). Készítsünk programot, amely beolvassa a fájl tartalmát, majd válaszol az
# alábbi kérdésekre!

#1. Melyek azok az országok, ahol már 2020. januárjában megjelent a vírus?
#2. Az adathalmaz utolsó napján hány fertőzött volt Németországban ( Germany )?
#3. Hol volt a legmagasabb az elhunytak aránya a fertőzöttek számához viszonyítva?

import pandas as pd

df = pd.read_csv('C:\\Users\\Dorián\\PycharmProjects\\PythonVizsgaFelkészülés1Feladatok\\tables\\covid19_stats.txt', sep=',', skiprows=1)

#print(df.info())

#1. Melyek azok az országok, ahol már 2020. januárjában megjelent a vírus?
pd.to_datetime(df['Date'])
print(df['Country'][(df['Date']>= '2020-01')&(df['Date']< '2020-02') & (df['Confirmed']>0)])

#2. Az adathalmaz utolsó napján hány fertőzött volt Németországban ( Germany )?
datemax = df['Date'].max()
print(df[(df['Country']=='Germany')&(df['Date']==datemax)]['Confirmed'])

#3. Hol volt a legmagasabb az elhunytak aránya a fertőzöttek számához viszonyítva?
print((df.groupby('Country')['Deaths'].sum() / df.groupby('Country')['Confirmed'].sum()).idxmax())

