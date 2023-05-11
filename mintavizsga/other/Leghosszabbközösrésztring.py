#Készíts programot, amely bekér a felhasználótól két sztringet,
#majd kiírja a bennük található leghosszabb közös részsztringet!
#Példa futási eredmény:
#1. sztring: András
#2. sztring: Bandi
#A leghosszabb közös rész: nd

st1 = str(input('1. string: '))
st2 = str(input('2. string: '))

common = ''

for i in range(len(st1)):
    for j in range(i+1,len(st1)+1):
        if st1[i:j] in st2 and len(st1[i:j])>len(common):
            common = st1[i:j]
print(common)