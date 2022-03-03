numero_de_testes = int(input())
lista_numeros = []

for n in range(numero_de_testes):
    lista_numeros.append(int(input()))

dentro_do_intervalo = []
fora_do_intervalo = []

for n in lista_numeros:
    if n>=10 and n<=20:
        dentro_do_intervalo.append(n)
    else:
        fora_do_intervalo.append(n)

print(f'{len(dentro_do_intervalo)} in\n{len(fora_do_intervalo)} out')
