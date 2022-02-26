from datetime import timedelta

delta = timedelta(hours=24)

inicio_jogo, fim_jogo = map(lambda x:int(x),input().split(" "))
duração = inicio_jogo - fim_jogo
print(duração)
