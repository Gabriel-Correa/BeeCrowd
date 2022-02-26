x, y, z = map(lambda x:float(x),input().split(" "))

if x+y>z and x+z>y and y+z>x:
    resultado_triangulo = x+y+z
    print("Perimetro = {:.1f}".format(resultado_triangulo))
else:
    resultado_trapezio = ((x+y)*z)/2
    print("Area = {:.1f}".format(resultado_trapezio))