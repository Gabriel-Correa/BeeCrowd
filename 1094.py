numero_de_testes = int(input())

cobaias = {'C': 0, 'R': 0, 'S': 0}


def impressão(total, porcentagem_coelho, porcentagem_rato, porcentagem_sapo):
    print(f'Total: {total} cobaias')
    print(f'Total de coelhos:', cobaias['C'])
    print(f'Total de ratos:', cobaias['R'])
    print(f'Total de sapos:', cobaias['S'])
    print(f'Percentual de coelhos: {porcentagem_coelho:.2f} %')
    print(f'Percentual de ratos: {porcentagem_rato:.2f} %')
    print(f'Percentual de sapos: {porcentagem_sapo:.2f} %')


def total_cobaias(cobaias):
    return cobaias['C'] + cobaias['R'] + cobaias['S']


def porcentagem(cobaia, total_cobaias):
    return float((cobaia/total_cobaias)*100)


def main():

    for n in range(numero_de_testes):
        quantidade, identificador = (input()).split(' ')
        quantidade = int(quantidade)
        cobaias[identificador] += quantidade

    total = total_cobaias(cobaias)

    porcentagem_coelho = porcentagem(cobaias['C'], total)
    porcentagem_sapo = porcentagem(cobaias['S'], total)
    porcentagem_rato = porcentagem(cobaias['R'], total)
    impressão(total, porcentagem_coelho, porcentagem_rato, porcentagem_sapo)


main()
