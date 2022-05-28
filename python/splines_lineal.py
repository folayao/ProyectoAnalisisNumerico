import numpy as np
from eliminacion_gaussiana import eliminacion_gausiana

def splines_lineal(x, y):
    n = len(x)-1    # Columnas
    m = 2*n         # Filas
    #Indice de inicio de columna
    cont = 0
    #Indice de valores entradas de las funciones
    contX = 0
    matriz = np.zeros((m, m))
    vector_terminos = np.zeros(m)

    #Inicializar matrix cero, caso unico
    matriz[0][0] = x[contX]
    matriz[0][1] = 1
    vector_terminos[0] = y[contX]
    contX += 1
    for i in range(1,2*n):       
        matriz[i][cont*2] = x[contX]
        matriz[i][cont*2 +1] = 1
        vector_terminos[i] = y[contX]
        #Cambio de valores entrada, cambia una vez llenada una fila par.
        if i % 2 == 0:
            contX += 1
        #Cambio del valor de inicio para llenar columnas, cambia cada dos iteraciones, es decir, al llenar fila impar.
        if i % 2  != 0:
            cont += 1
    
    # print(matriz.tolist())
    print(matriz)
    print()
    print(vector_terminos)
    print()
    x = np.linalg.solve(matriz, vector_terminos)
    # x = eliminacion_gausiana(matriz.tolist(), vector_terminos.tolist(), m)
    print(x)
     
X = [1,2,4]
Y = [141,112.7,125.63] 
splines_lineal(X,Y)