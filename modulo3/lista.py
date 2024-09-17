while True:
    print('Informe 4 produtos e seus preços')
    listagem = (str(input('Nome do produto: ')), float(input('Preço: R$')), 
                str(input('Nome do produto: ')), float(input('Preço: R$')), 
                str(input('Nome do produto: ')), float(input('Preço: R$')), 
                str(input('Nome do produto: ')), float(input('Preço: R$')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? caso aceitar a lista ira reiniciar [S/N]: ')).strip().upper()
    if resp == 'N':
        break
print('-'*30)
print('LISTAGEM DE PREÇOS')
print('-'*30)
for pos in range(len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>10}')