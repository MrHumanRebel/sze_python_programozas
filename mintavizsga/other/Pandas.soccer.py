# A soccer.txt szövegfájl európai első osztályú labdarúgó mérkőzésekről tartalmaz adatokat,
# a 2015-16-os szezonból.
# Az utolsó 9 oszlop fogadóirodák odds-ait tartalmazza hazai csapat győzelmére ( B365H • BwH • IWH ),
# a döntetlenre ( B365D. BWD . IWD ) ill. a vendégcsapat győzelmére ( B365A . BWA . IwA ).
# Készitsünk programot, amely beolvassa a szövegfájl tartalmát, majd válaszol az alábbi kérdésekre!

# 1. Melyik bajnokságban ( country ) mennyi volt a mérkőzésenkénti gólátlag?
# 2. Melyik fogadóiroda adta átlagosan a legmagasabb odds-okat a hazai csapat győzelméért?
# 3. Melyik bajnokságban született a legtöbb döntetlen?
# 4. A B365 fogadóiroda szerfloat melyik eredmény volt a legváratlanabb (azaz a legmagasabb odds értékű)?

import pandas as pd

df = pd.read_csv(
    '/home/g14/uni/sze_python_programozas/data/soccer.txt', sep=',', skiprows=1)
# print(df.info())
# print(df)

# 1. Melyik bajnokságban ( country ) mennyi volt a mérkőzésenkénti gólátlag?
df['goals'] = df['home_team_goal']+df['away_team_goal']
print(df.groupby('country')['goals'].mean())

# 2. Melyik fogadóiroda adta átlagosan a legmagasabb odds-okat a hazai csapat győzelméért?
max_home_odds = df[['B365H', 'BWH', 'IWH']].mean().max()
max_home_odds_bookie = df[['B365H', 'BWH', 'IWH']].mean().idxmax()
print(f"{max_home_odds_bookie}: {max_home_odds}")

# 3. Melyik bajnokságban született a legtöbb döntetlen?
df['goalsequal'] = df['home_team_goal'] == df['away_team_goal']
print(df.groupby(df['country'])['goalsequal'].sum().idxmax())

# 4. A B365 fogadóiroda melyik eredmény volt a legváratlanabb (azaz a legmagasabb odds értékű)?
max_odds = df[['B365H', 'B365D', 'B365A']].max().max()
max_odds_bookie = df[['B365H', 'B365D', 'B365A']].max().idxmax()
print(f'A {max_odds_bookie} fogadóiroda {max_odds} eredménye volt a legváratlanabb.')
