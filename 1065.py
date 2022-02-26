num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

lista_numeros = [num1, num2, num3, num4, num5]

numeros_pares = 0

for lista_numeros in lista_numeros:
    if (lista_numeros%2) == 0:
        numeros_pares = numeros_pares + 1

print(f'{numeros_pares} valores pares')
        