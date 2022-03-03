num1 = int(input())
num2 = int(input())
lista_soma = []
lista_numero = []
lista_numero.append(num1)
lista_numero.append(num2)
lista_numero.sort()



for n in range(lista_numero[0]+1, lista_numero[1]):
     if (n%2) == 1:
         lista_soma.append(n)

soma_lista = sum(lista_soma)

print(soma_lista)
