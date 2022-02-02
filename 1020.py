tempo = int(input())

def convert_tempo (tempo):
    dias = tempo
    anos = int(dias/365)
    dias = dias%365
    meses = int(dias/30)
    dias = dias%30
    print("{0} ano(s)\n{1} mes(es)\n{2} dia(s)".format(anos, meses, dias))

convert_tempo(tempo)