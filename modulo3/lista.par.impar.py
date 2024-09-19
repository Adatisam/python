num = []
par = list()
impar = list()
while True:
    num.append(int(input('Digite os valores: ')))
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print('-='*10)
print(f'A lista dos {len(num)} elementos digitados é {num}')
print(f'A lista completa de pares é {par}')
print(f'A lista completa de ímpares é {impar}')