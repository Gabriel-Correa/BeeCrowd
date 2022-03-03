numero_de_testes = int(input())
lista_numeros = []

for n in range(numero_de_testes):
    lista_numeros.append(int(input()))


for numero in lista_numeros:
    if numero>0:
        if (numero%2) == 0:
            print("EVEN POSITIVE")
        if (numero%2) == 1:
            print("ODD POSITIVE")
    if numero<0:
        if (numero%2) == 0:
            print("EVEN NEGATIVE")
        if (numero%2) == 1:
            print("ODD NEGATIVE")
    if numero == 0:
        print("NULL")