import math
A, B, C = map(lambda x:float(x),input().split(" "))

def formula_delta(a, b, c):
    return (b**2)-4*a*c

def formula_baskara(a, b, c):
    delta = formula_delta(a, b, c)
    base = 2*a
    if delta<0 or base==0:
        print("Impossivel calcular")
    else:
        resultado1 = (-b +math.sqrt(delta))/base
        resultado2 = (-b -math.sqrt(delta))/base
        print("R1 = {0:.5f}\nR2 = {1:.5f}".format(resultado1, resultado2))

formula_baskara(A, B, C)


