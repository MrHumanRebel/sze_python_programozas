#Készítsünk programot, amely bekér a felhasználótól egy n természetes számot,
# felbontja az összes lehetséges módon 3 különbözö természetes szám összegére,
# és kiírja ezeket a felbontásokat!
# A tagok sorrendje ne számítson, azaz pl. 1 + 2 + 3 és 1 + 3 + 2 ne számítson különbözőnek!
# Példa futási eredmény:

#n: 7

#0 + 1 + 6
#0 + 2 + 5
#0 + 3 + 4
#1 + 2 + 4

n = int(input("n: "))

for i in range(0,n,1):
    for j in range(0,n,1):
        for k in range(0,n,1):
            if i+j+k == n and i != j and i != k and j!=k and i<j<k:
                print(i,j,k)