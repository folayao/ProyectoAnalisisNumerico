

def dif_divididas(x,y):
    n = len(x)
    difdiv = []
    # fila = []
    
    #Llenar con los datos que ya conocemos
    
    for i in range(n):
        fila = []
        fila.append(x[i])
        fila.append(y[i])
        if i == 0: 
            difdiv.append(fila)
            continue

        for d in range(1,i+1):
            num = fila[len(fila)-1] - difdiv[i-1][d]
            den = x[i] - x[i-d]
            diferencia = num/den
            fila.append(diferencia)
        difdiv.append(fila)   
    print(' '*80, 'TABLA')
    for i in range(len(difdiv)):
        print(f'{difdiv[i]}\r\n')

X = [1,1.2,1.4,1.6,1.8,2]
Y = [0.6747,0.8491,1.1214,1.4921,1.9607,2.5258] 
dif_divididas(X,Y)