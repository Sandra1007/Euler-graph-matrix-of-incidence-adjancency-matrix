import numpy as np

#Napisati funkciju koja čita datoteku u kojoj je zapisan graf u pajek formatu 
# i sprema podatke o grafu u strukturu podataka po volji 
# (matricu susjedstva, matricu incidencije ili listu susjedstva grafa).


def citajDatoteku(rezultat):
    flag=False
    niz=[]
    f=open("football.net", "r", encoding='utf8')  #otvaranje datoteke
    for x in f:
        if "*Arcs" in x:
            flag=True
        if flag:
            lines=f.readlines()
            for x in lines:
                rezultat=x.split()
                niz.append(rezultat)
    return niz
    
def PretvoriUInteger(niz):
    i=0
    niz1=[]
    niz2=[]
    niz3=[]
    d=len(niz)
    for x in niz:
        if(i<d-1): #da ne ukljucuje edges koji su u fileu ispod arcs
            niz1.append((int(x[0])-1)) #ocu da matrica bude s indeksima 0,0 pa onda smanjujen svaki broj za 1
            niz2.append((int(x[1])-1))
            niz3.append((int(x[2])-1))
            i=i+1 # na kraju filea je napisano edges pa da to ne ukljucuje
    return niz1, niz2, niz3

def PoveziBrojeve(niz1,niz2,niz3):
    niz4=[]
    niz4=tuple(zip(niz1,niz2,niz3)) 
    niz4=sorted(niz4) #sortiraj po redu i povezi prva 3 u redu u tuple i tako ostale
    print(niz4)
    return niz4
    

def NapraviMatricu(niz4):
    s=(35,35)
    matrica=np.zeros(s)
    for x in range(35): 
        for y in range(35): #matrica je 35x35
            for z in niz4:
                if(((x==z[0]) and (y==z[1])) or ((x==z[1]) and (y==z[0]))): #ako je prvi ili drugi element tuplea(predstavlja x) susjedan trecem elementu tuplea(predstavlja brid) pisi 1
                    matrica[x,y]=1
    print("Matrica susjedstva: ")
    print(matrica)
    print("-----------------------------------")
    

rezultat=[]
niz=citajDatoteku(rezultat)
niz1,niz2,niz3=PretvoriUInteger(niz)
niz4=PoveziBrojeve(niz1,niz2,niz3)
NapraviMatricu(niz4)
