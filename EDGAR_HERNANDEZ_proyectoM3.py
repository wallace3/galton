import matplotlib.pyplot as pl
import numpy as np

niveles=12
nivelesArray = np.zeros(niveles + 1)   ## utilizamos la función np zeros para definir el tamaño de nuestro arreglo, que en este caso son los niveles
canicas = 3000  #definimos la variable canicas, que son las solicitadas en el proyecto

def generateResults():
    ###  Función para obtener los resultados 
    #de cada una de las cánicas 
    for _ in range(canicas):      #Comenzamos el ciclo por las 3000 canicas
        firstPos = 0           #La primer posición de la cánica es en el valor 0 porque aún no se lanza
        for _ in range(niveles):         #Ciclo por cada uno de los niveles para decidir el camino de la cánica
            if np.random.rand() > 0.5:    # Utilizamos la función rand. que nos da un valor entre 0 y 1 para decidir si va a la derecha o la izquierda
                firstPos += 1
        nivelesArray[firstPos] += 1             #Se suma en 1 en el nivel del resultado de nuestra condicionante
    return nivelesArray   

result = generateResults()   

def createGraph():  

    ### función que generá la gráfica   ##

    pl.bar(range(niveles +1), result)                  #SE pasa el rango para los niveles y la variable result que tiene los valores
    pl.xlabel('Niveles')
    pl.ylabel('Cantidad de Cánicas')
    pl.title('Maquina de Galton - 3000 cánicas')
    pl.show()

createGraph()

