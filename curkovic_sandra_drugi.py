import numpy as np

# Napisati funkcije koje će raditi konverzije zapisa grafa
#  u ostale dvije strukture podataka (matricu susjedstva, 
# matricu incidencije ili listu susjedstva grafa.


def citajDatoteku(rezultat):
    flag=False
    niz=[]
    f=open("euler.net", "r", encoding='utf8')  #otvaranje datoteke
    for x in f:
        if "*Edges" in x:
            flag=True
        if flag:
            lines=f.readlines()
            for x in lines:
                rezultat=x.split()
              
                niz.append(rezultat)

    return niz
    
def Odvoji_Brojeve(niz):
    i=0
    niz1=[]
    niz2=[]
    d=len(niz)
    for x in niz:
        if(i<=d-1 and i>=0):
            niz1.append(int(niz[i][0])) #stavi u prvi niz prvi broj
            niz2.append(int(niz[i][1])) #stavi u niz drugi broj iz liste
            i=i+1 #povecaj i 
    
    return niz1,niz2
    
    
def UrediNiz(niz1,niz2):
    d=len(niz1)
    for x in range(0,d):
        niz1[x]=niz1[x]-1 #smanji svaki element da odgovara indeksu matrice, ocu da indeks krece od 00 ne 11
        niz2[x]=niz2[x]-1
    
    sve_zajedno=tuple(zip(niz1,niz2)) #dva niza, svaki element stavi u tuple u paru 
    sve_zajedno=sorted(sve_zajedno) #sortiraj
    print(sve_zajedno)
    return sve_zajedno

def NapraviMatricuSusjedstva(sve_zajedno):
    s=(5,5)
    matrica=np.zeros(s) #napravi matricu 5x5 ispunjenu 0
  
    for x in range(5): #usporeduj je li element u nizu (npr. 1 i 2)jednak indeksu matrice i ako je stavi 1
        for y in range(5):
            for z in sve_zajedno:
                if(((x==z[0]) and (y==z[1])) or ((x==z[1]) and (y==z[0]))):
                    matrica[x,y]=1
    print("Matrica susjedstva")
    print(matrica)
    print("---------------------------------------")


def PostaviZaMatricuIncidencije(sve_zajedno):
    b=0
    novo=[]
    for x in sve_zajedno: 
        novo.append(x+(b,)) #u tuple dodaji b koji se povecaje koji ce predstavljat brid
        print(novo)
        b=b+1
    return novo

    

def NapraviMatricuIncidencije(novo):
    s=(5,8)
    matrica1=np.zeros(s)
    for x in range(5): #usporeduj je li element u nizu (npr. 1 i 2)jednak indeksu matrice i ako je stavi 1
        for y in range(8): #matrica je 5x8 (5 tocaka, 8 bridova)
            for z in novo:
                if(((x==z[0]) and (y==z[2])) or ((x==z[1]) and (y==z[2]))): #ako je prvi ili drugi element tuplea(predstavlja x) susjedan trecem elementu tuplea(predstavlja brid) pisi 1
                    matrica1[x,y]=1
    print("Matrica incidencije: ")
    print(matrica1)
    print("-----------------------------------")


    


rezultat=[]
niz=citajDatoteku(rezultat)
niz1,niz2=Odvoji_Brojeve(niz)
sve_zajedno=UrediNiz(niz1,niz2)
NapraviMatricuSusjedstva(sve_zajedno)
novo=PostaviZaMatricuIncidencije(sve_zajedno)
NapraviMatricuIncidencije(novo)


