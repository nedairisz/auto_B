from Auto import Auto

def beolvas():
    fajl=open("auto.txt", "r", encoding="utf-8")
    fajl.readline()
    nyers_lista=fajl.readlines()
    fajl.close()

    kocsi=[]
    for i in range(0,len(nyers_lista),1):
        sorok=nyers_lista[i]
        sor_tag=sorok.strip().split("$")
        nev=sor_tag[0]
        gyd=int(sor_tag[1])
        peldany=Auto(nev, gyd)
        kocsi.append(peldany)
    return kocsi

def tabla(kocsi: Auto):
    print(f"\t{kocsi.nev}: {len(kocsi.nev)} hosszú.")

def flotta(kocsi):
    print(f"\tAutók száma: {len(kocsi)}.")

def ertekes(kocsi):
    lf_index=0
    for i in range(0,len(kocsi),1):
        if kocsi[lf_index].gyd<kocsi[i].gyd:
            lf_index=i
    return lf_index

def kiiras(kocsi: Auto):
    fajl=open("kiir.txt", "w", encoding="utf-8")
    fajl.write(f"\t{kocsi.nev}: {len(kocsi.nev)} hosszú.")
    fajl.close()

