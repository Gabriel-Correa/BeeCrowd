numero_de_testes = int(input())


for n in range(numero_de_testes):
    lista_string = []
    lista_string.extend(input().split(" "))
    lista_numeros = [float(val) for val in lista_string]
    num1, num2, num3 = lista_numeros
    
    media_ponderada = ((num1*2)+(num2*3)+(num3*5))/10

    print(f'{media_ponderada:.1f}')
    


