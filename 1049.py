filo = str(input())

if filo == 'vertebrado':
    tipo = str(input())
    if tipo == 'ave':
        alimento = str(input())
        if alimento == 'carnivoro':
            print("aguia")
        elif alimento == 'onivoro':
            print("pomba")
    elif tipo == 'mamifero':
        alimento = str(input())
        if alimento == 'onivoro':
            print("homem")
        elif alimento == 'herbivoro':
            print("vaca")
if filo == 'invertebrado':
    tipo = str(input())
    if tipo == 'inseto':
        alimento = str(input())
        if alimento == 'hematofago':
            print("pulga")
        elif alimento == 'herbivoro':
            print('lagarta')
    elif tipo == 'anelideo':
        alimento = str(input())
        if alimento == 'hematofago':
            print("sanguessuga")
        elif alimento == 'onivoro':
            print("minhoca")