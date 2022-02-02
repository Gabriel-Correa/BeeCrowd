product1 = input().split(" ")
product2 = input().split(" ")
code1, quantity1, price1 = product1
code2, quantity2, price2 = product2

total = (int(quantity1)*float(price1)) + (int(quantity2)*float(price2))
print("VALOR A PAGAR: R$ {:.2f}".format(total))