#Az a. b.c egész számok pitagoraszi számhármast alkotnak. ha a^2 + b^2 = c^2.
# A numbers lista pozitív egész számokat tartalmaz. Készítsünk programot,
# amely megadja, hogy található-e pitagoraszi számhármas a numbers listában,
# és ha igen, akkor melyik pitagoraszi számhármasban a legnagyobb a c szám számjegyeinek az összege!
# A program ne csak a megadott numbers listára működjön. hanem tetszőleges. ugyanilyen formátumú bemenetre is!

numbers = [ 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17, 19, 23, 24, 25, 29, 31 ]

#Létrehozok egy tuple-t (a,b,c) majd a,b,c-vel végig iterálok a numbers listán.
#Ha ez megvan, akkor megnézem hogy mely esetben igaz a pitragorasz tétel és azokat a számhármasokat elmentem egy triplets listába.
triplets = [(a, b, c) for a in numbers for b in numbers for c in numbers if a**2 + b**2 == c**2]

#
if triplets:
    max_c = max(triplets, key=lambda x: sum(int(d) for d in str(x[2])))
    print('Pitagoraszi számhármasok a listában:', triplets)
    print(f"A legnagyobb összegű c szám a(z) {max_c[2]}, a(z) {max_c} pitagoraszi számhármasban.")
else:
    print("Nem található pitagoraszi számhármas a listában.")