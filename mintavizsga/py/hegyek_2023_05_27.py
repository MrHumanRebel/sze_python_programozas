#!/usr/bin/env python
# coding: utf-8

# Hány olyan egész szám van a [12,3456] intervallumban, 
# amelyben a számjegyek összege osztható a szám jegyeinek darabszámával 
# (pl. ilyen számok: 13, 123, 1111; nem ilyen számok: 12, 122, 2345)?

# In[2]:


counter = 0
for i in range(12,3456):
    num_as_str = str(i)
    sum = 0
    hossz = len(num_as_str)
    for j in range(len(num_as_str)):
        sum = sum + int(num_as_str[j])
    if sum % hossz == 0:
        counter = counter + 1
        #print(i)
        
print(counter)


# # Alternatív megoldás

# In[1]:


counter = 0
for i in range(12,3456):
    szamok=str(i)
    hossz=len(szamok)
    osszeg=0
    for j in szamok:
        osszeg+=int(j)
    if osszeg % hossz == 0:
        counter+=1
print(counter)


# Sajnos hiányzik a feladat szövege, ezért csak a megoldás látható.

# In[16]:


mtx = [[1,0,0], [0,1,1]]

def mtx_check(mtx):
    ures = []
    uj = []
    sor = len(mtx)
    for i in range(len(mtx)):
        #print(mtx[i])
        sor_ok = False
        minden_sorban_elem = True
        binaris = True
        helyes = True
        hossz = len(mtx)
        if len(mtx) >= 1:
            sor_ok = True
        else:
            print("Hibás minimum elemszám")
        for j in range(hossz-1):
            if len(mtx[j+1]) != len(mtx[j]):
                minden_sorban_elem = False
                print("A sorméret nem azonos!")
        for j in range(len(mtx[i])):
            #print(mtx[i][j])
            if (int(mtx[i][j]) != 0) and (int(mtx[i][j]) != 1):
                binaris  = False 
                print("Nem binaris számok")
    
    for i in range(len(mtx)):
        sum = 0
        for j in range(len(mtx[i])):
            sum = sum + int(mtx[i][j]) * 2**(len(mtx[i])-j-1)
        uj.append(sum)
    
    if sor_ok == False or minden_sorban_elem == False or binaris == False:
        helyes = False
        print("Üres mátrix")
        return ures
    else:
        print("Helyes mátrix")
        print(uj)
        return helyes, uj
    
helyes_e = mtx_check(mtx)  


# A hegyek.txt adatfájl Magyarország legmagasabb hegycsúcsait tartalmazza. 
# A felsorolás a tengerszint feletti magasságon alapul, a legmagasabbtól az alacsonyabbak felé haladva.
# Nyissa meg a fájlt és határozza meg az alábbi statisztikákat!
# 
# a) Hány csúcsot tartalmaz a lista a Mátrából?
# b) Melyik hegységből szerepel a legtöbb hegycsúcs a listán?
# c) Gyűjtse ki a különböző hegységek legmagasabb csúcsait, és rendezze őket magasság szerint csökkenő sorrendbe!
# d) Akad néhány méterre azonos magasságú hegy a fenti listában. 
# Melyik magassághoz tartozik a legtöbb hegy? Melyek ezek a hegyek? 

# In[17]:


import pandas as pd

df = pd.read_csv('/home/g14/uni/sze_python_programozas/data/hegyek.txt',sep='	')
# df.info()

# Hány csúcsot tartalmaz a lista a Mátrából?
szam = len(df[df['Hegység'] == 'Mátra'])
print(szam)
    

# Melyik hegységből szerepel a legtöbb hegycsúcs a listán? 
szam = df.groupby('Hegység')['Hegycsúcs neve'].size().max()
hegysor = df.groupby('Hegység')['Hegycsúcs neve'].size().idxmax()
print(hegysor, " ", szam)

# Gyűjtse ki a különböző hegységek legmagasabb csúcsait, 
# és rendezze őket magasság szerint csökkenő sorrendbe! 
hegysegek = df.groupby('Hegység').max().sort_values('Magasság (m)', ascending=False)    
print(hegysegek)
      

# Akad néhány méterre azonos magasságú hegy a fenti listában. 
# Melyik magassághoz tartozik a legtöbb hegy? 
# Melyek ezek a hegyek? 

azonosmagassag = df[['Hegység','Magasság (m)']].sort_values(ascending=False,by='Magasság (m)').groupby('Magasság (m)').size().max()
azonosmagassagmeter = df[['Hegység','Magasság (m)']].sort_values(ascending=False,by='Magasság (m)').groupby('Magasság (m)').size().idxmax()
print(f'{azonosmagassagmeter} méterhez tartozik a legtöbb hegy, méghozzá {azonosmagassag} db')
print(df[['Hegység','Hegycsúcs neve','Magasság (m)']][df['Magasság (m)']== azonosmagassagmeter])

