i = 1
j = 7

print(f'I={i} J={j}')


while i != 9 or j != 5:
    j -= 1
    if j == 4:
        i = i + 2
        j = 7
    print(f'I={i} J={j}')
