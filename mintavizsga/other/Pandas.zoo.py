# A zoo.txt több száz gerinces állatfaj várható élettartamáról tartalmaz becsléseket,
# észak-amerikai állatkertek törzskönyvi adatai alapján.
# Készítsünk programot, amely beolvassa a szövegfájl tartalmát, majd válaszol az alábbi kérdésekre!

# 1. Melyik a 10 legmagasabb várható élettartamú (mle) állatfaj?
# 2. Átlagosan mennyi a várható élettartam az egyes rendszertani osztályokban ( taxonomy_class)?
# 3. Melyik fajnál a legnagyobb a különbség a hímek és a nőstények várható élettartama között (male_mle, female_mle )?
# 4. A sample_size oszlop azt adja meg, hogy az adott fajból hány egyedről van mérési adat.
# Összesen hány hüllőről ( Reptilia ) van mérési adat az adathalmazban?
import pandas as pd

df = pd.read_csv(
    '/home/g14/uni/sze_python_programozas/data/zoo.txt', sep='|', skiprows=1)
# print(df.info())

# 1. Melyik a 10 legmagasabb várható élettartamú (mle) állatfaj?
top10 = df.nlargest(10, 'mle')
print(top10[['common_name', 'mle']])

# 2. Átlagosan mennyi a várható élettartam az egyes rendszertani osztályokban ( taxonomy_class)?
print(df.groupby('taxonomy_class')['mle'].mean().sort_values(ascending=False))

# 3. Melyik fajnál a legnagyobb a különbség a hímek és a nőstények várható élettartama között (male_mle, female_mle )?
df['diff_mle'] = abs(df['male_mle']-df['female_mle'])
maxindx = df['diff_mle'].idxmax()
max = df['diff_mle'].max()
print(df['common_name'][maxindx],
      'fajnál a legnagyobb a különbség a hímek és a nőstények várható élettartama között, méghozzá', max, 'évvel.')

# 4. A sample_size oszlop azt adja meg, hogy az adott fajból hány egyedről van mérési adat.
# Összesen hány hüllőről ( Reptilia ) van mérési adat az adathalmazban?
reptilia_data = df[df['taxonomy_class'] == 'Reptilia']
reptilia_sample_size = reptilia_data['sample_size'].sum()
print(reptilia_sample_size)
