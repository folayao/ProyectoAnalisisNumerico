import math
from tabulate import tabulate

def newton(f, xi, tol,fi, maxIter, tError):
    headers=["ite","x","f(x)","fi(x)","Error"]
    table=[]
    if f(xi) == 0:
        print(f'El valor {xi} es raiz')
    else:
        ite = 0
        error = tol + 1
        table.append([ite,xi, f(xi), fi(xi), format(error, ".1E")])
        while(error >= tol and ite < maxIter):
            xn = xi - f(xi)/fi(xi)
            if tError == 0:
                error = abs(xn - xi)
            else:
                error = abs((xn - xi)/xn)
            ite += 1
            xi = xn
            table.append([ite, xi, f(xi), fi(xi), format(error, ".1E")])

        print(tabulate(table, headers))
        if error < tol:
            print(f'{xi} es raiz con tolerancia {format(tol, ".1E")} en iter {ite}')
        else:
            print('No llegamos')

# f = lambda x: math.exp(-x) - x
# fi = lambda x: -math.exp(-x) - 1
f = lambda x: math.exp(-x) - (x**2)*math.cos(2*x-4) + 6*x + 3
fi = lambda x: -math.exp(-x) - 2*x*math.cos(2*x-4) - 2*(x**2)*math.sin(2*x-4) + 6

newton(f, 0, 0.00005, fi, 10000, 0)