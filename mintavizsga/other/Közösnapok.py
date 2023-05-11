# Alex és Bob és Charlie közös programot szerveznek.
# A szabad időintervallumaik az intervals szótárban vannak megadva.
# Készítsünk programot, amely kiszámítja, hogy hány olyan nap van, amikor mindhárman ráérnek.
# Az intervallumok zártak, azaz a végpontok szabad időpontnak tekintendők.
# A program ne csak a megadott intervals adatszerkezetre működjön, hanem tetszőleges,
# ugyanilyen formátumú bemenetre is!

import datetime as dt

intervals = {
'Alex': [('2020-06-20','2020-06-23'), ('2020-06-30', '2020-07-05')],
'Bob' : [('2020-06-18','2020-06-21'), ('2020-06-24','2020-07-01'), ('2020-07-03', '2020-07-04')],
'Charlie': [('2020-06-21', '2020-06-28'), ('2020-07-02', '2020-07-10')],
}

# Először megkeressük az összes közös napot
common_days = set()
for intervals_list in intervals.values():
    for interval in intervals_list:
        start_date = dt.datetime.strptime(interval[0], '%Y-%m-%d').date()
        end_date = dt.datetime.strptime(interval[1], '%Y-%m-%d').date()
        common_days |= set([start_date + dt.timedelta(days=x) for x in range((end_date-start_date).days+1)])

# Majd megszámoljuk, hogy hány olyan nap van, amikor mindhárman ráérnek
free_days = 0
for day in common_days:
    free_count = 0
    for intervals_list in intervals.values():
        for interval in intervals_list:
            start_date = dt.datetime.strptime(interval[0], '%Y-%m-%d').date()
            end_date = dt.datetime.strptime(interval[1], '%Y-%m-%d').date()
            if start_date <= day <= end_date:
                free_count += 1
    if free_count == 3:
        free_days += 1

print(f"Összesen {free_days} nap van, amikor mindhárman ráérnek.")