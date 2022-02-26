num1 = int(input())
num2 = int(input())

organizar_variavel = [num1, num2]
lista_numeros = []

organizar_variavel.sort()
lista_organizada = organizar_variavel
a, b = lista_organizada

for n in range(a, b):
    if (n%2) == 1:
        lista_numeros.append(n)

soma_lista = sum(lista_numeros)

print(soma_lista)