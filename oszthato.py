import random

def sorozat():
    lista=[]
    print(f"\t", end="")
    for i in range(0,50,1):
        szam=random.randint(1,100)
        lista.append(szam)
    return lista

def ottel_oszthato(lista):
    szamlalo=0
    for i in range(0, len(lista),1):
        if lista[i]%7==0:
            szamlalo+=1
    return szamlalo