# Az investments.txt szövegfájl amerikai cégekbe történő befektetésekről tartalmaz adatokat
# (a TechCrunch hírportál alapján).
# Készíts programot, amely kiszámítja és kiírja az alábbi statisztikákat:

# 1. Hány befektetés történt összesen az egyes cégekbe?
# 2. Melyik cégbe fektettek be legtöbbször?
# 3. Melyik cégbe fektették be a legtöbb pénzt?
# 4. Cégkategóriánként hány dollárt fektettek be összesen?
import pandas as pd

df = pd.read_csv(
    '/home/g14/uni/sze_python_programozas/data/investments.txt', sep='|')
# print(df.info())

# 1. Hány befektetés történt összesen az egyes cégekbe?
print(df.groupby('company').size().sort_values(ascending=False))

# 2. Melyik cégbe fektettek be legtöbbször?
print(df.groupby('company').size().sort_values(ascending=False).head(1))

# 3. Melyik cégbe fektették be a legtöbb pénzt?
print(df.groupby('company')['raisedAmt'].sum(
).sort_values(ascending=False).head(1))

# 4. Cégkategóriánként hány dollárt fektettek be összesen?
print(df.groupby('category')['raisedAmt'].sum().sort_values())
