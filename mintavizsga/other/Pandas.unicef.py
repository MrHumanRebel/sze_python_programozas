# Az unicef.txt szövegfájl a világ 5 év alatti népességének élelmezési helyzetéről tartalmaz adatokat.
# Az egyes sorok felméréseknek felelnek meg, a felmérések országonként időbeli sorrendben vannak felsorolva.
# Készíts programot, amely beolvassa az unicef.txt tartalmát,
# minden országra kiválasztja a legfrissebb felmérést,
# majd a legfrissebb felmérések alapján kiírja az alábbi statisztikákat:

# 1. Az országok hányadrészében magasabb az Underweight indikátor az Overweight indikátornál?
# 2. Mely 5 országban a legmagasabb a Severe Wasting indikátor?
# 3. Régiónként (United Nations Region) mekkora a 20%-nál nagyobb Stunting indikátorral
# rendelkező országok aránya.
# 4. Hol a legalacsonyabb a tűlsűlyos gyerekek aránya a 10%-nál alacsonyabb Wasting és Stunting indikátorral
# rendelkező országok között?

import pandas as pd

df = pd.read_csv(
    '/home/g14/uni/sze_python_programozas/data/unicef.txt', sep='|')

df2 = df.groupby('Country').last()  # Legfrissebb adatok kinyerése
# print(df.info())

# 1. Az országok hányadrészében magasabb az Underweight indikátor az Overweight indikátornál?
print((df2['Underweight'] > df2['Overweight']).mean())

# 2. Mely 5 országban a legmagasabb a Severe Wasting indikátor?
print(df2['Severe Wasting'].sort_values(ascending=False).head(5))

# 3. Régiónként (United Nations Region) mekkora a 20%-nál nagyobb Stunting indikátorral
# rendelkező országok aránya.
# Stunting oszlop object-ről float típusúvá alakítása.
df2['Stunting'] = df2['Stunting'].str.replace(',', '.').astype(float)
print((df2['Stunting'] > 20).groupby(df2['United Nations Region']).mean())


# 4. Hol a legalacsonyabb a túlsúlyos gyerekek aránya a 10%-nál alacsonyabb Wasting és Stunting indikátorral
# rendelkező országok között?
# Stunting oszlop object-ről float típusúvá alakítása.
df2['Stunting'] = df2['Stunting'].str.replace(',', '.').astype(float)
# Wasting oszlop object-ről float típusúvá alakítása.
df2['Wasting'] = df2['Wasting'].str.replace(',', '.').astype(float)
# Overweight oszlop object-ről float típusúvá alakítása.
df2['Overweight'] = df2['Overweight'].str.replace(',', '.').astype(float)
print(df2[(df2['Wasting'] < 10) & (df2['Stunting'] < 10)]
      ["Overweight"].idxmin())
