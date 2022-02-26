num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

lista_numeros = [num1, num2, num3, num4, num5]

numeros_pares = 0
numeros_impares = 0
numeros_positivos = 0
numeros_negativos = 0

for lista_numeros in lista_numeros:
    if (lista_numeros%2) == 0:
        numeros_pares = numeros_pares + 1
    elif(lista_numeros%2) == 1:
        numeros_impares = numeros_impares +1
    if lista_numeros>0:
        numeros_positivos = numeros_positivos +1
    elif lista_numeros<0:
        numeros_negativos = numeros_negativos +1

print(f'{numeros_pares} valor(es) par(es)\n{numeros_impares} valor(es) impar(es)\n{numeros_positivos} valor(es) positivo(s)\n{numeros_negativos} valor(es) negativo(s)')