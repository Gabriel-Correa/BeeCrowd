import math
x1, y1 =input().split(" ")
x2, y2 = input().split(" ")
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)
def produtoNotavel(a, b):
    return (a-b)**2
def distance(a, b):
    return math.sqrt(a+b)
x = produtoNotavel(x2, x1)
y = produtoNotavel(y2, y1)
resultado = distance(x, y)
print("{:.4f}".format(resultado))