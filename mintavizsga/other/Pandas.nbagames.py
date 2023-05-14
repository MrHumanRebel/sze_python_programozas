# Az nba_games.txt (nba_games.txt) az amerikai professzionális kosárlabda bajnokság (NBA)
# mérkőzéseiről tartalmaz adatokat, a 2013-astól a 2019-es szezonig.
# Készítsünk programot, amely beolvassa a szövegfájl tartalmát, majd válaszol az alábbi kérdésekre!
#   1. A mérkőzések hány százalékát nyerte meg a hazai ( home ) csapat?
#   2. Hány mérőzésen szedtek le a csapatok 130-nál több lepattanót ( REB )?
#   3. Melyik mérkőzésen született a legnagyobb különbségű győzelem?
#   4. Mi a csapatok erősorrendje a győzelmek száma alapján?

import pandas as pd
df = pd.read_csv(
    '/home/g14/uni/sze_python_programozas/data/nba_games.txt', sep='|', skiprows=1)
# 1. A mérkőzések hány százalékát nyerte meg a hazai ( home ) csapat?
print('A mérkőzések ', (sum(df['PTS_home'] > df['PTS_away']) /
      len(df['PTS_home'])) * 100, '%-át nyerte meg a hazai csapat.')

# 2. Hány mérőzésen szedtek le a csapatok 130-nál több lepattanót ( REB )?
print(len(df[(df['REB_home']+df['REB_away']) > 130]),
      'mérkőzésen szedtek le a csapatok 130-nál több lepattanót.')

# 3. Melyik mérkőzésen született a legnagyobb különbségű győzelem?
print(df.iloc[abs(df['PTS_home']-df['PTS_away']).idxmax()])

# 4. Mi a csapatok erősorrendje a győzelmek száma alapján?
hazaigyozelem = df[(df['PTS_home'] > df['PTS_away'])
                   ].groupby('TEAM_home').size()
hazaivereseg = df[(df['PTS_home'] < df['PTS_away'])
                  ].groupby('TEAM_home').size()
print((hazaigyozelem + hazaivereseg).sort_values(ascending=False))
