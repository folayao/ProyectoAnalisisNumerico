import math
from tabulate import tabulate

def punto_fijo(f, xi, tol, g, maxIter, tError):
    headers=["ite","x","Error"]
    table=[]
    if f(xi) == 0:
        print(f'El valor {xi} es raiz')
    else:
        ite = 0
        error = tol + 1
        table.append([ite,xi, error])

        while(error >= tol and ite < maxIter):
            xn = g(xi)
            if tError == 0:
                error = abs(xn - xi)
            else:
                error = abs((xn - xi)/xn)
            ite += 1
            xi = xn
            table.append([ite,xi, error])

        print(tabulate(table, headers))
        if error < tol:
            print(f'{xi} es raiz con tolerancia {format(tol, ".1E")} en iter {ite}')
        else:
            print('No llegamos')

f = lambda x: math.exp(-x) - x
g = lambda x: math.exp(-x)

punto_fijo(f, 0.5, 0.00005, g, 50, 0)