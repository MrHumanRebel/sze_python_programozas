# A words lista sztringeket tartalmaz. Készítsünk programot, amely megadja,
# hogy az angol ABC melyik betűje fordul elő a legtöbb szóban!
# A program ne tegyen különbséget a kis- és nagybetűk között,
# illetve ne csak a megadott words listára működjön, hanem tetszőleges, ugyanilyen formátumú bemenetre is!

words = [
    'Apple', 'Apricot', 'Avocado', 'Banana', 'Blueberry',
    'Cherry', 'Coconut', 'Grape', 'Grapefruit', 'Fig',
    'Kiwi', 'Lemon', 'Lime', 'Mandarin', 'Mango',
    'Melon','Nectarine', 'Orange', 'Papaya', 'Peach',
    'Pear', 'Pineapple', 'Plum', 'Raspberry', 'Strawberry'
]

words = [word.lower() for word in words] #Mindegyiket kisbetűssé teszem.

letterslist = []
lettersset = set()
outlist = []
for i in range(len(words)): #Végig iterálok a listán.
    for j in words[i]: #Majd végigiterálok az egyes szavakon.
        letterslist.append(j) #Listához és a halmazhoz is hozzáfűzöm őket.
        lettersset.add(j)
letterslist.sort() #A listát sorba rendezem.
lettersset = list(lettersset) #A halmazt iterálhatóvá teszem.
for i in range(len(lettersset)): #Végig iterálok a halmazból lett listán melyben minden betű egyszer szerepel.
    #print(lettersset[i],'=',letterslist.count(lettersset[i]))
    outlist.append(letterslist.count(lettersset[i])) #Egy listához fűzöm a betűk darabszámát.
    out = outlist.index(max(outlist)) #Megkeresem a legnagyobb mennyiségben előforduló betűk számának az  indexét.

print('A legtöbbször előforduló betű a(z):',lettersset[out],', ennyiszer fordul elő:', max(outlist))


