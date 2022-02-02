tempo = int(input())

def convert_tempo (tempo):
    segundos = tempo
    horas = int(segundos/3600)
    segundos = segundos%3600
    minutos = int(segundos/60)
    segundos = segundos%60
    print("{0}:{1}:{2}".format(horas, minutos, segundos))

convert_tempo(tempo)