#Készítsünk programot, amely bekér a felhasználótól két sztringet,
#majd kiírja a mindkét sztringben megtalálható bigramok számát!
#Bigramnak nevezzük a 2 karakter hosszú rész sztringeket.
#pl: papamaci = pa-ap-pa-am-ma-ac-ci
#pl: mamamaci = ma-am-ma-am-ma-ac-ci
#A program ne tekintse különbözőnek a kis és nagybetűket.
#Megoldás:
n = str(input("String1: "))
m = str(input("String2: "))
def bigramcounter(n,m):
    n = n.lower() #String1 kisbetűssé tétele
    m = m.lower() #String2 kisbetűssé tétele
    list1 = []  #String1 lista
    list2 = []  #String2 lista
    full1 = set() #String1 halmaz
    full2 = set() #String2 halmaz

    for i in range(len(n)-1): #Végig iterálunk string1-en, bigramokra bontjuk és hozzáadjuk a listához és a halmazhoz a bigramokat.
        bigram = n[i:i+2]
        list1.append(bigram)
        full1.add(bigram)

    for i in range(len(m)-1): #Végig iterálunk string2-őn, bigramokra bontjuk és hozzáadjuk a listához és a halmazhoz a bigramokat.
        bigram = m[i:i+2]
        list2.append(bigram)
        full2.add(bigram)

    out = full1 & full2 #A két halmaz unióját vesszük amivel csak a közös bigramok maradnak benne.
    print(list1)
    print(list2)
    print("Közös bigramok száma:", len(out))

bigramcounter(n,m)