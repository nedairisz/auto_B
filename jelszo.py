
def bekeres():
    fnev=input("\tAdja meg a felhasználónevé! ")
    jszo=input("\tAdja meg a jelszavát! ")
    i=0
    while not(fnev=="bori99" and jszo=="Szivecske>3"):
        print("\tBelépés megtagadva.")
        fnev=input("\tAdja meg a felhasználónevé! ")
        jszo=input("\tAdja meg a jelszavát! ")
        i+=i
    print("\tBelépés engedélyezve.")