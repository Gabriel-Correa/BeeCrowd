id, quantidade = map(lambda x:int(x),input().split(" "))

cardapio = [{
   'id':1,
   'especificacao':'Cachorro Quente',
   'preco':4.00 
},
{
   'id':2,
   'especificacao':'X-Salada',
   'preco':4.50 
},
{
   'id':3,
   'especificacao':'X-Bacon',
   'preco':5.00 
},
{
   'id':4,
   'especificacao':'Torrada Simples',
   'preco':2.00 
},
{
   'id':5,
   'especificacao':'Refrigerante',
   'preco':1.50 
}]

def search(id):
    for lanche in cardapio:
        if lanche['id'] == id:
            return lanche

def fechar_conta(id, quantidade):
    valor_lanche = float(search(id)['preco'])
    return float(valor_lanche*quantidade)

total = fechar_conta(id, quantidade)
print("Total: R$ {:.2f}".format(total))
