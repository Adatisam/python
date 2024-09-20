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

print('//'*30)

numero = []
pares = impares = list()
for c in range(0, 9):
    numero.append(int(input(f'Digite o {c} valor: ')))
    numero.sort()
for i, v in enumerate(numero):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-='*30)
print(f'A lista dos {len(numero)} elementos digitados é {numero}')
print(f'A lista completa de pares é {pares}')
print(f'A lista completa de ímpares é {impares}')