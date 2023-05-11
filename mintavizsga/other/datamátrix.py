#A data objektum egy nullákból és egyesekból álló négyzetet tartalmaz, listák listájaként reprezentálva.
# Készítsünk programot, amely megadja leghosszabb csupa nullából álló átlós vonal hosszát a négyzetben!
# A program ne csak megadott data objektumra, hanem tetszőleges, ugyanilyen formátumú bemenetre is!

data = [[1,0,1,0],
        [1,0,0,1],
        [0,1,1,0],
        [0,0,0,0]]

rows = len(data)
cols = len(data[0])

max = 0

for i in range(rows):
    sum = 0
    for j in range(cols):
        if data[i][j] == 0:
            for k in range(1, min(rows - i, cols - j)):
                if sum == 0:
                    sum += 1
                if data[i + k][j + k] == 0:
                    sum += 1
    if sum > max:
        max = sum
    sum = 0

    for j in range(cols - 1, -1, -1):
        if data[i][j] == 0:
            for k in range(1, min(rows - i, j + 1)):
                if sum == 0:
                    sum += 1
                if data[i + k][j - k] == 0:
                    sum += 1
    if sum > max:
        max = sum

print(f"Legrövidebb csupa nullából álló átlós vonal hossza: {max}")