
#Identidad
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
    
#Matriz de ceros
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

#Extraer columna
def columna(A, col):
    column = []
    for i in range(len(A)):
        column.append(A[i][col])
    return column

# res = dot(A[0], 1,2,columna(A, 0), 0, 1)
# print(f'res: {res}')