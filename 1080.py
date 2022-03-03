lista_numeros = []

for n in range(5):
    lista_numeros.append(int(input()))

print(max(lista_numeros))
print(lista_numeros.index(max(lista_numeros))+1)