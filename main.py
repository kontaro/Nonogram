import numpy as np


def createNonogram(n,m):#n and m refers to lenght of matrice
    nonogram=np.zeros((n,m))
    return nonogram
def imprimirNonograma(state):
    hoal=0;

def leerPistas():
    listaIzquierda=0

def reglas(nonogram,Pistas,n,m):
    #pistas=Pistas.split()
    x=0
    for listP in Pistas:

        if(listP==0):
            for y in range(m):
                nonogram[x,y]=1
        if(listP==m):
            for y in range(m):
                nonogram[x,y]=2

        x=x+1
    return nonogram


#def Resolver(nonogram,PLeft,PRight):



pistas=[0,4,3]
nonogram=createNonogram(3,4)
nonogram=reglas(nonogram,pistas,3,4)
print(nonogram)
