valor = float(input())

def calculo_quantidade_notas_moedas (total):
    print("NOTAS:")
    notas =[100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
    moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]
    for nota in notas:
        quantidade_notas = int(total/nota)
        print("{0} nota(s) de R$ {1:.2f}".format(quantidade_notas, nota))
        total = round(float(total%nota),2)
    print("MOEDAS:")
    for moeda in moedas:
        quantidade_moedas = int(total/moeda)
        print("{0} moeda(s) de R$ {1:.2f}".format(quantidade_moedas, moeda))
        total = round(float(total%moeda),2)


calculo_quantidade_notas_moedas(valor)