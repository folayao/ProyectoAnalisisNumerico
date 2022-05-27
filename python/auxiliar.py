import math

def eye(n):
    x = []
    for i in range(n):
        filai = []
        for j in range(n):
            if i == j:
                filai.append(1)
            else:
                filai.append(0) 
        x.append(filai)
    return x

def zero(n):
    x = []
    for i in range(n):
        filai = []
        for j in range(n):
            filai.append(0) 
        x.append(filai)
    return x

#Producto punto de filas
def dot(x, xi, xf, y, yi, yf):
    sum = 0
    dif = xi - yi
    for i in range(xi, xf+1):
        sum += x[i]*y[i-dif]
    return sum

def dot(x, y):
    n = len(x)
    sum = 0
    for i in range(n):
        sum += x[i]*y[i]
    return sum

#Extraer columna
def columna(A, col):
    column = []
    for i in range(len(A)):
        column.append(A[i][col])
    return column

def factorizar(A):
    n = len(A)
    D = zero(n)
    L = zero(n)
    U = zero(n)
    
    for i in range(n):
        for j in range(n):
            if i == j:
                D[i][j] = A[i][j]
            elif i > j:
                L[i][j] = -A[i][j]
            else:
                U[i][j] = -A[i][j]

    return D, L, U
A = [[4, 3, -2, -7],
     [3, 12, 8, -3],
     [2, 3, -9, 3],
     [1, -2, -5, 6],]

D,L, U = factorizar(A) 
print(D ,'\n',L,'\n',U,'\n') 

def inversa_D(D):
    n = len(D)
    for i in range(n):
        D[i][i] = 1/D[i][i]
    return D

def suma_vectores(a, b):
    n = len(a)
    y = []
    for i in range(n):
        y.append(a[i] + b[i])
    return y

def resta_vectores(a, b):
    n = len(a)
    y = []
    for i in range(n):
        y.append(a[i] - b[i])
    return y

def suma_matrices(A, B):
    n = len(A)
    Y = zero(n)
    for i in range(n):
        for j in range(n):
            Y[i][j] = A[i][j] + B[i][j]
    return Y


def prod_matrices(A, B):
    n = len(A)
    Y = zero(n)
    for i in range(n):
        for j in range(n):
            Y[i][j] = dot(A[i], columna(B, j))
    return Y

def prod_matriz_vector(A, b):
    n = len(A)
    y = []
    for i in range(n):
        y.append(dot(A[i], b))
    return y

def norma(a):
    n = len(a) 
    total = 0 
    for i in range(n):
        total += (a[i])*(a[i])
    total = math.sqrt(total) 
    return total  

# res = dot(A[0], 1,2,columna(A, 0), 0, 1)
# print(f'res: {res}')
# A = [[1,2,3],[4,5,6],[7,8,9]]
# B = [[9,8,7],[6,5,4],[3,2,1]]
# b = [1,2,3]
b = [20, 18, 31, 12]

# print(prod_matrices(A,b))
