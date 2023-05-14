# Az usa_cars.txt szövegfájl eladásra meghirdetett autókról és autóalkatrészekről tartalmaz adatokat.
# Készítsünk programot, amely beolvassa a szövegfájl tartalmát, majd válaszol az alábbi kérdésekre:

# Melyik a 3 legrégebbi évjáratú termék?
# Melyik a ledrágább Audi, BMW, Chevrolet, Ford, Nissan, Maserati és Toyota?
# Melyik államban árulják a legtöbb piros Fordot?
# Hányadik leggyakoribb szín az adathalazban a piros?

import pandas as pd

df = pd.read_csv(
    '/home/g14/uni/sze_python_programozas/data/usa_cars.txt', sep=',')
# print(df.info())
# Melyik a 3 legrégebbi évjáratú termék?
print(df.sort_values('Evjarat').head(3))

# Melyik a ledrágább Audi, BMW, Chevrolet, Ford, Nissan, Maserati és Toyota?
audi_rows = df[df['Marka'] == 'Audi']
print(audi_rows.loc[audi_rows['Ar'].idxmax()])
print()
bmw_rows = df[df['Marka'] == 'BMW']
print(bmw_rows.loc[bmw_rows['Ar'].idxmax()])
print()
chev_rows = df[df['Marka'] == 'Chevrolet']
print(chev_rows.loc[chev_rows['Ar'].idxmax()])
print()
ford_rows = df[df['Marka'] == 'Ford']
print(ford_rows.loc[ford_rows['Ar'].idxmax()])
print()
nissan_rows = df[df['Marka'] == 'Nissan']
print(nissan_rows.loc[nissan_rows['Ar'].idxmax()])
print()
mas_rows = df[df['Marka'] == 'Maserati']
print(mas_rows.loc[mas_rows['Ar'].idxmax()])
print()
toy_rows = df[df['Marka'] == 'Toyota']
print(toy_rows.loc[toy_rows['Ar'].idxmax()])

# Melyik államban árulják a legtöbb piros Fordot?
red_fords = df[(df['Marka'] == 'Ford') & (df['Szin'] == 'Red')]
state_counts = red_fords['Allam'].value_counts()
print(state_counts.idxmax())

# Hányadik leggyakoribb szín az adathalazban a piros?
# Összes szín, melyikből hány darab van.
color_counts = df['Szin'].value_counts()
red_count = color_counts.get('Red', 0)  # Ezekből a pirosak.
red_ratio = red_count/color_counts.sum()  # A pirosak hányada
red_rank = (color_counts >= red_count).sum()  # A pirosak a 9. helyen állnak.
print(red_rank)
