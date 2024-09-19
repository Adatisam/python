num = []
mai = 0
men = 0
for c in range(0,6):
    num.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c ==0: 
        mai = men = num[c]
    else: 
        if num[c] > mai:
            mai = num[c]
        if num[c] < men:
            men = num[c]
print('-=-'*30)
print(f'O maior valor digitado foi {mai} na posição ',end='')
for i, v in enumerate(num):
    if v == mai:
        print(f'{i}')
print(f'O menor valor digitado foi {men} na posição ',end='')
for i, v in enumerate(num):
    if v == men:
        print(f'{i}')