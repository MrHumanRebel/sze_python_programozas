#A letters objektum egy kisbetűkből álló négyzetet tartalmaz.
#A sorok sztringként vannak reprezentálva, és egy listába vannak egymás után fűzve.
# Készíts programot, amely kiírja, hogy mely oszlopban található a legtöbb magánhangzó!
# A program ne csak a letters objektumra, hanem tetszőleges, ugyanilyen formátumú, bemenetre is működjön!

import itertools

letters = ["tüzesensütleany",
           "árinapsugáraazé",
           "gtetejérőlajuhá",
           "szbojtárrafölös",
           "legesdologsütni",
           "eolynagyonajuhá",
           "sznakúgyisnagym",
           "elegevagyonszer",
           "elemtüzeégfiata",
           "lszivébenugyleg",
           "eltetianyájtafa",
           "luvégenfaluvége",
           "nnyájamigszerte",
           "legelészőaddigs",
           "ubájánafűbenhev"]


# Mátrix megfordítása és oszlopok sorokká alakítása
matrix = list(itertools.zip_longest(*letters, fillvalue=' '))

vowels = 'aáeéiíoöőüűuú'

max_vowels = 0
max_column = 0
for i, col in enumerate(matrix):
    num_vowels = 0
    for letter in col:
        if letter.lower() in vowels:
            num_vowels += 1
    if num_vowels > max_vowels:
        max_vowels = num_vowels
        max_column = i

print(f"A legtöbb ({max_vowels}) magánhangzó a(z) {max_column+1}. oszlopban található.")



