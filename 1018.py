valor = int(input())

def calculo_quantidade_notas (total):
    print(total)
    notas =[100, 50, 20, 10, 5, 2, 1]
    for nota in notas:
        quantidade_notas = int(total/nota)
        print("{0} nota(s) de R$ {1},00".format(quantidade_notas, nota))
        total = total%nota

calculo_quantidade_notas(valor)