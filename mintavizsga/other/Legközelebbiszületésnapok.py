#A birthdays lista kitalált személyek nevét és születési dátumát tartalmazza.
#Készíts programot, amely megkeresi, hogy kik állnak életkorban egymáshoz a legközelebb,
# és hány nap köztük a különbség!
# A program ne csak a megadott birthdays listára működjön, hanem tetszőleges,
# ugyanilyen formátumú bemenetre is! Feltehetjük, hogy minden név különböző,
# és legalább két név van megadva.

birthdays = [
    ('Kovács Andor',   '1999-10-29'),
    ('Kiss Martina',   '2000-02-13'),
    ('Horváth Barna',  '1999-12-05'),
    ('Győri Eszter',   '2000-10-29'),
    ('Nagy Tivadar',   '1999-08-16'),
    ('Tóth Tamara',    '2000-01-30'),
    ('Szakács Sándor', '1999-09-02')
]

import datetime

def closest_birthdays(birthdays):
    birthdays = sorted(birthdays, key=lambda x: datetime.datetime.strptime(x[1], '%Y-%m-%d')) #Dátumszerint növekvő sorba rendezés
    closest_days = float('inf')
    closest_pair = None
    for i in range(len(birthdays) - 1):
        current_days = (datetime.datetime.strptime(birthdays[i+1][1], '%Y-%m-%d') - datetime.datetime.strptime(birthdays[i][1], '%Y-%m-%d')).days #két dátum különbsége
        if current_days < closest_days:
            closest_days = current_days
            closest_pair = (birthdays[i], birthdays[i+1])
    return closest_pair, closest_days

closest_pair, closest_days = closest_birthdays(birthdays)

print(f"A legközelebbi két születésnap: {closest_pair[0][0]} ({closest_pair[0][1]}) és {closest_pair[1][0]} ({closest_pair[1][1]}) közötti időszak: {closest_days} nap.")

