def eliminacion_gausiana(A,b, n):
  Ab=[]
  x=[]
  sum=0
  #Matriz ampliada
  for i in range(n):
    A[i].append(b[i])
    x.append(0)
    Ab = A
    #Eliminacion Gausiana
    for k in range(1, n-1): #Array de pivotes
        for i in range(k+1, n): #Hallar multiplicador, vuelve cero Ab[i][k]
            M = Ab[i][k]/Ab[k][k]
            Ab[i][k] = 0
            
            for j in range(k+1, n+1): #Resta la filaActual - anterios*multiplicador
                Ab[i][j] = Ab[i][j] - M*Ab[k][j]
    
    
    #Sustitución regresiva
    for k in range(n, 1, -1):
        sum = 0
        for j in range(k+1, n):
            sum += Ab[k][j]*x[j]
        x[k-1] = (Ab[k][n+1] - sum)/Ab[k][k]

A = [[-7, 2, -3, 4],
     [5, -1, 14, -1],
     [1, 9, -7, 5],
     [-12, 13, -8, -4],]
  
b = [-12, 13, 31, -32]

eliminacion_gausiana(A, b, 4)