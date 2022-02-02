A, B, C, D = map(lambda x:int(x),input().split(" "))

def teste_logico(a, b, c, d):
    cd = c+d
    ab = a+b
    if b>c and d>a:
        if cd>ab:
            if c>0 and d>0:
                if a % 2 == 0:
                    print("Valores aceitos")
                else:
                    print("Valores nao aceitos")
            else:
                print("Valores nao aceitos")   
        else:
            print("Valores nao aceitos")
    else:
        print("Valores nao aceitos")

teste_logico(A, B, C, D)                          
            
                    
        



