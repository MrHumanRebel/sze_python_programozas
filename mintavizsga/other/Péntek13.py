#Készíts programot, amely kér a felhasználótól egy évszámot, majd megadja,
# hogy az adott évben hány pénteki nap esett 13-ára!

import datetime as dt

year = int(input("Add meg az éveszámot:"))
friday13_counter = 0

for month in range(1,13):
    day = dt.date(year, month, 13)
    if day.weekday()==4:
        friday13_counter+=1

print(f'A(z) {year}. évi péntek 13-ak száma: {friday13_counter}')
