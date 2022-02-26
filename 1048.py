salario = float(input(""))

def percentual(a):
    return a/100

def reajuste(a, b):
    return a*b

def aumento_salarial(a, b):
    
    return a+b

if salario>0 and salario<=400:
    aumento = 15
    porcento = percentual(aumento)
    aumento = reajuste(salario, porcento)
    salario_total = aumento_salarial(salario+aumento)
elif salario>400 and salario<=800:
    aumento = 12
    porcento = percentual(aumento)
    aumento = reajuste(salario, porcento)
    salario_total = aumento_salarial(salario+aumento)
elif salario>800 and salario<=1200:
    aumento = 10
    porcento = percentual(aumento)
    aumento = reajuste(salario, porcento)
    salario_total = salario+aumento
elif salario>1200 and salario<=2000:
    aumento = 7
    porcento = percentual(aumento)
    aumento = reajuste(salario, porcento)
    salario_total = aumento_salarial(salario+aumento)
elif salario>2000:
    aumento = 4
    porcento = percentual(aumento)
    aumento = reajuste(salario, porcento)
    salario_total = aumento_salarial(salario+aumento)

print(f'Novo salario: {salario_total:.2f}\nReajuste ganho: {aumento:.2f}\nEm percentual: {porcento*100:.0f} %')