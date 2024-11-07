# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:49:06 2024

@author: Simon
"""
import numpy as np
import math

#Promedio aritmético
def promedio(array):
    """
    Calcua el promedio de una lista de números
    -----------
    arrray : array
        lista con números
    
    retorna
    ------------
    promedio : float
        proedio aritmético de los numeros
    """
    lenArray = len(array)
    totalArray = sum(array)
    mean = totalArray/lenArray
    
    return mean

def mediana(lista):
    """

    Parameters
    ----------
    lista : list
        Toma una lista de valores

    Devuelve la mediana de los valores
    -------
    float/int
    """
    listaNan = []
    for i in listaNan:
        if math.isfinite(i):
            listaNan.append(i)
    
    listaNan = listaNan.sort()
    largoLista = len(listaNan)
    valorMedio = len(listaNan)//2
    
    if largoLista%2 != 0:           
        return lista[valorMedio]
    
    else:
        mediana = (listaNan[valorMedio]+listaNan[valorMedio-1])/2  
        return mediana


def moda(lista):
    """
    Parameters
    ----------
    lista : list
        Una lista donde se repinten los datos

    Returns
    -------
        el valor que más se repite
    """
    
    listaDatos = []
    listaFrecuencia = []
    
    for i in lista:
        if i not in listaDatos:
            listaDatos.append(i)
            
    
    for j in listaDatos:
        cont = 0
        for k in lista:
            if j == k:
                cont +=1
        listaFrecuencia.append(cont)
    
    iMax = 0
    valMax = listaFrecuencia[0]
    
    for i in range(1,len(listaFrecuencia)):
        if listaFrecuencia[i] > valMax:
            iMax = i
            valMax = listaFrecuencia[i]
    
    return listaFrecuencia[iMax]

nombre = "C:/Users/Simon/Downloads/bsc_sel (1).dat"
archivo = open(nombre,"r")
contenido = archivo.readlines()[1:]


spyType = []

for elementos in contenido:
    elemNew = elementos.split("   ")
    spyType.append(elemNew)


    

print(spyType)
archivo.close()
