lista_numeros = (input().split(" "))

lista_int = list(map(int, lista_numeros))

for numero in lista_int:
    if numero>0:
        if (numero%2) == 0:
            print("ODD POSITIVE")
        if (numero%2) == 1:
            print("EVEN POSITIVE")
    if numero<0:
        if (numero%2) == 0:
            print("ODD NEGATIVE")
        if (numero%2) == 1:
            print("EVEN NEGATIVE")
    if numero == 0:
        print("NULL")