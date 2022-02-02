tempo = int(input())
media_velocidade = int(input())
def calculo_gasto_combustivel (horas, media_velocidade):
    return (horas*media_velocidade)/12
resultado = calculo_gasto_combustivel(tempo, media_velocidade)
print("{0:.3f}".format(resultado))
