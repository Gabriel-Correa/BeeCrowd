nota1, nota2, nota3, nota4 = map(lambda x:float(x),input().split(" "))

def calculo_media(a, b, c, d):
    return ((a*2)+(b*3)+(c*4)+(d))/10

media1 = calculo_media(nota1, nota2, nota3, nota4)
print("Media: {:.1f}".format(media1))

if 7<media1:
    print("Aluno aprovado.")
elif media1<7 and media1>=5:
    print("Aluno em exame.")
    nota_exame = float(input(""))
    print("Nota do exame: {:.1f}".format(nota_exame))
    media_exame = (media1+nota_exame)/2
    if media_exame>5:
        print("Aluno aprovado.\nMedia final: {:.1f}".format(media_exame))
    else:
        print("Aluno reprovado.")
elif media1<5:
    print("Aluno reprovado.")
