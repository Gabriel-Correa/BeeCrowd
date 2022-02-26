num1, num2, num3, num4, num5, num6 = map(lambda x:float(x),input().split(" "))

numeros_positivos = 0

lista_numeros = [num1, num2, num3, num4, num5, num6]

lista_numeros_positivos = []

for lista_numeros in lista_numeros:
    if lista_numeros>0:
        numeros_positivos = numeros_positivos + 1
        lista_numeros_positivos.append(lista_numeros)

media_lista = sum(lista_numeros_positivos)/len(lista_numeros_positivos)

print(f'{numeros_positivos} valores positivos')
print(f'{media_lista:.1f}')