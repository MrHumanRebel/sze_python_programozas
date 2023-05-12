#A dog_breeds.txt szövegfájl kutyafajták jellemzőit tartalmazza az American Kennel Club leírása alapján.
# Az adatok felnőtt példányokra vonatkoznak. Készítsünk programot, amely beolvassa a szövegfájl tartalmát,
# majd válaszol az alábbi kérdésekre!

#1. Melyik az 5 legnehezebb fajta a weight_low_lbs oszlop alapján?
#2. Melyek azok a fajták, ahol a maximális és a minimális testmagasság között legalább 25 cm a különbség? (1 hüvelyk = 2,54 cm)
#3. Az átlagosnál alacsonyabb fajták között melyik a legnagyobb súlyú? (a height_low_inches és a weight_low_lbs oszlop alapján)
#4. Milyen kezdőbetűjű fajtából hány darab van az adathalmazban?

import pandas as pd

df = pd.read_csv('C:\\Users\\Dorián\\PycharmProjects\\PythonVizsgaFelkészülés1Feladatok\\tables\\dog_breeds.txt', sep ='|')

#print(df.info())

#1. Melyik az 5 legnehezebb fajta a weight_low_lbs oszlop alapján?
print(df.groupby('Breed')['Weight_low_lbs'].max().sort_values(ascending=False).head(5))

#2. Melyek azok a fajták, ahol a maximális és a minimális testmagasság között legalább 25 cm a különbség? (1 hüvelyk = 2,54 cm)
df['Height_high_inches'] = df['Height_high_inches'].apply(lambda x: x * 2.54)  # cm-re váltás
df['Height_low_inches'] = df['Height_low_inches'].apply(lambda x: x * 2.54)    # cm-re váltás
filtered_df = df[(df['Height_high_inches'] - df['Height_low_inches']) >= 25]['Breed']
print(filtered_df)

#3. Az átlagosnál alacsonyabb fajták között melyik a legnagyobb súlyú?
# (a height_low_inches és a weight_low_lbs oszlop alapján)
avg_height = (df['Height_low_inches'].mean())
shorter_breeds = df[df['Height_low_inches'] < avg_height]
max_weight_breed = shorter_breeds.loc[shorter_breeds['Weight_low_lbs'].idxmax()]['Breed']
print(max_weight_breed)

#4. Milyen kezdőbetűjű fajtából hány darab van az adathalmazban?
letter_count = df.groupby(df['Breed'].str[0])['Breed'].count()
print(letter_count)