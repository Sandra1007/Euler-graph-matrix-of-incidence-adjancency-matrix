#Napisati funkciju u kojoj se ispituje je li graf Eulerov.
#  Ako je graf Eulerov, ispisati jedan od Eulerovih puteva u grafu
#  (ne koristiti gotova rješenja s interneta).
#
#Graf je Eulerov akko ima sve vrhove parnog stupnja
#stupnjevi iz vrha:koliko puta se vrh ponavlja

def CitajDatoteku (rezultat):
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
                #print(niz)

    return niz

def Pretvori_u_Integer (niz):
    integer1=[]
    integer2=[]
    for x in niz:
        integer1.append(int(x[0]))
        integer2.append(int(x[1]))
    
   
    sve_zajedno=integer1+integer2
    print(sve_zajedno) #stavi u istu listu jer kod neusmjerenog grafa treba gledati oba reda za stupnjeve(koliko ima bridova)
    sve_zajedno=sorted(sve_zajedno)
    return sve_zajedno, integer1,integer2 #vracan ove nizove jer nakadno ocu napravit graf eulerovim

def NadiStupanj (sve_zajedno):
    rj={}
    for x in sve_zajedno:
        if(x not in rj.keys()):
            rj[x]=1
        else:
            rj[x]+=1
        
    return rj   

def ProvjeriParnostStupnja(rjecnik):
    brojac=0 #izbroji koliko je parnih vrhova
    d=len(rjecnik) #duljina rjecnika tako da kad se usporedi broj parnih i duljina rjecnika vidjet ce se jesu li svi vrhovi parni
    for key in rjecnik.keys():
        if((rjecnik[key]%2)==0): #Graf je Eulerov ako ima sve vrhove parnog stupnja
            brojac=brojac+1
    
    if(brojac==d): #ako je broj parnih jednak duljini rjecnika onda je eulerov.
        print("Graf je Eulerov.")
    else:
        print("Graf nije Eulerov.")



rezultat=[]
niz=CitajDatoteku(rezultat)
sve_zajedno,int1,int2=Pretvori_u_Integer(niz)
rjecnik=NadiStupanj(sve_zajedno)
ProvjeriParnostStupnja(rjecnik)
