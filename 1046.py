tempo_jogo = input().split(' ')
inicio_jogo = int(tempo_jogo[0])
fim_jogo = int(tempo_jogo[1])

if inicio_jogo<fim_jogo:
    tempo = fim_jogo = inicio_jogo
else:
    tempo = (24-inicio_jogo)+fim_jogo

print(f"O JOGO DUROU {tempo} HORA(S)")


