x, y = map(lambda x:float(x),input().split(" "))

if x>0 and y>0:
    print("Q1")
elif x>0 and y<0:
    print("Q4")
elif x<0 and y>0:
    print("Q2")
elif x<0 and y<0:
    print("Q3")
elif y==0 and x!=0.0:
    print("Eixo X")
elif x==0 and y!=0.0:
    print("Eixo Y")
else:
    print("Origem")