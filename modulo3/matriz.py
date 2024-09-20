matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = mai = col = 0
for i in range(0, 3):
    for c in range(0, 3):
        matriz[i] [c] = int(input(f'Digite os valores para [{i}, {c}]: '))
print('='*30)
for i in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[i][c]:^5}]',end='')
        if matriz[i][c] % 2 == 0:
            par += matriz[i][c]
    print()
print('='*30)  
print(f'A soma dos números pares é {par}.')
for i in range(0, 3):
    col += matriz[i][c]
print(f'A soma dos valores da terceira coluna é {col}.')
for c in range(0, 3):
    if c == 0:
        mai = matriz[i][c]
    elif matriz[i][c] > mai:
        mai = matriz[i][c]
print(f'O maior valor é de {mai}')