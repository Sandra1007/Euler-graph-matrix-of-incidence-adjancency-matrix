#Napisati funkcije koje računaju:
#broj vrhova u grafu - vertices ++++
# broj bridova u grafu -edges ++++
# stupanj svakog vrha -broj bridova iz vrha ++++
#vrhove s maksimalnim brojem incidentnih bridova 

def CitajDat(rezultat):
    brojac_bridova=0
    flag=False
    niz=[]
    f=open("eva.net", "r", encoding='utf8')  #otvaranje datoteke
    for x in f:
        if "arcs" in x: #arcs su usmjereni bridovi
            flag=True
        if flag:
            lines=f.readlines()
            for x in lines:
                brojac_bridova=brojac_bridova+1
                rezultat=x.split()
                niz.append(rezultat)
    print(niz)
    return niz,brojac_bridova


rezultat=[]
niz,brojac_bridova=CitajDat(rezultat)



