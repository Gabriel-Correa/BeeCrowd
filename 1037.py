numero_teste = float(input())

if 0<=numero_teste and numero_teste<=25:
    print("Intervalo [0,25]")
elif 25<numero_teste and numero_teste<=50:
    print("Intervalo (25,50]")
elif 50<numero_teste and numero_teste<=75:
    print("Intervalo (50,75]")
elif 75<numero_teste and numero_teste<=100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")
