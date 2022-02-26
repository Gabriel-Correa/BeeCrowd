x, y = map(lambda x:int(x),input().split(" "))

lista_numeros = [x,y]
lista_numeros.sort()
lista_ordenada = lista_numeros
a, b = lista_ordenada

if (b%a)==0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")