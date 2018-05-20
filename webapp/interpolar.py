# -*- coding: utf-8 -*-
"""
Created on Sat May 19 20:18:02 2018

Diferencias divididas

@author: emaga
"""

class TablaDiferencias:
    def __init__(self,diferencias,orden):
        self.diferencias = diferencias
        self.orden = orden


def diferencias(arrayX,arrayY):
    
    orden = len(arrayX)-1
    listDifer = []
    listDifer.append(arrayY)
    i=0 
    while(i<orden):
      j = 0  
      difOrden = []
      while(j < len(listDifer[i])-1):
          h = arrayX[j+i+1] - arrayX[j] 
          dif = (listDifer[i][j+1] - listDifer[i][j]) / h 
          difOrden.append(dif)
          j +=1
      listDifer.append(difOrden)
      i+=1    
    return  TablaDiferencias(listDifer,orden)      

def interpolaX(arrayX,arrayY,x):
    if x in arrayX:
        return arrayY[arrayX.index(x)]
    n = len(arrayX)
    if x > arrayX[0] and x < arrayX[n-1]:
        difs = diferencias(arrayX,arrayY)
        orden = difs.orden
        i = 0
        pol = 0
        while i <= orden:
            pol = pol + (difs.diferencias[i][0] * sumPol(x,arrayX,i))
            i += 1
        return pol
    else:
        return "valor no se puede interpolar"


def sumPol(x,array,n):
    i = 0
    res = 1

    while i<n:
        res = res * (x - array[i])
        i +=1
    return res