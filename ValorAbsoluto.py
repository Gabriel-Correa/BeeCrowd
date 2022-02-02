
a, b, c = input().split(" ")
def maiorAB(a,b):
    return int(((a+b)+abs(a-b))/2)

maior = maiorAB(int(a), int(b))
if maior<int(c):
    maior = int(c)
print("{0} eh o maior".format(maior))