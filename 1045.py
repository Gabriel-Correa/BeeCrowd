x, y, z = map(lambda x:float(x),input().split(" "))

lista_numeros = [x,y,z]

lista_numeros.sort(reverse=True)

if x>=y+z:
    print("NAO FORMA TRIANGULO")
elif(x**2)==(y**2)+(z**2):
    print("TRIANGULO RETANGULO")
elif(x**2)>(y**2)+(z**2):
    print("TRIANGULO OBTUSANGULO")
elif x==y and y==z and x==z:
    print("TRIANGULO EQUILATERO")
elif x==y!=z or x==z!=y or y==z!=x:
    print("TRIANGULO ISOSCELES")
elif (x**2)<(y**2)+(z**2):
    print("TRIANGULO ACUTANGULO")