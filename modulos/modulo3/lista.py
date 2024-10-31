listagem = list()
preco = list()
while True:
    listagem.append(str(input('Nome do produto: ')))
    preco.append(float(input('Preço: R$'))) 
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        break
print('-'*30)
print('LISTAGEM DE PREÇOS')
print('-'*30)
for pos in range(len(listagem)) and range(len(preco)):
    print(f'{listagem[pos]:.<30}', end='')
    print(f'R${preco[pos]}')