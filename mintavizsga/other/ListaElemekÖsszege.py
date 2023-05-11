#Készíts (teljeskörűen paraméterezett) függvényt,
#amely bemenetként megkapja pozitív egész számok egy nemüres listáját,
#és visszaadja a lista azon elemét, amelyikben a számjegyek összege a legnagyobb.
#Hívd meg a függvényt a [245, 1132, 98, 465, 14231, 7854, 2542] listával és írd ki a kapott eredményt!

def sum_nums(list):
    max_sum = 0
    max_value = list[0]
    for item in list:
        maximum = sum([int(c) for c in str(item)])
        if maximum > max_sum:
            max_sum = maximum
            max_value = item
    return max_value

print(sum_nums([245, 1132, 98, 465, 14232, 7854, 2542]))