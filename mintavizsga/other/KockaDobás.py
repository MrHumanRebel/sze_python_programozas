#Készíts programot, amely bekéri a felhasználótól 'n' értékét,
# szimulál darab kockadobást, majd kiírja, hogy mi volt a leghosszabb 6-os sorozat hossza!
# Példa futási eredmény:
#n: 50
#31554643644341364414422455514666664664563666113524
#A leghosszabb 6-os sorozat hossza: 5

import random

n = int(input('n:'))
#Kockadobás generálás
def six_in_row(n):
    rolls=[]
    for i in range(n):
        rolls.append(random.randint(1,6))
    longest_sequence = 0
    current_sequence = 0
    #Leghosszabb 6os sor keresés
    for roll in rolls:
        if roll == 6:
            current_sequence +=1
            if current_sequence>longest_sequence:
                longest_sequence = current_sequence
        else:
            current_sequence = 0
    print("A dobások eredménye: " + "".join(str(x) for x in rolls))
    print(f"A leghosszabb 6-os sorozat hossza: {longest_sequence}")

six_in_row(n)
