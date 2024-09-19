listanum = []
while True:
    listanum.append(int(input('Digite o valor: ')))
    print('Valor adicionado com sucesso...')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        break
print('='*30)
print(f'Sua lista foi de {listanum}')

print('/-/-'*30)

#versão alternativa:

listanum = list()
while True:
    n = int(input('Digite o valor: '))
    if n not in listanum:
        listanum.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado não adicionado...')
    r = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if r == 'N':
        break
print('='*30)
print(f'Sua lista foi de {listanum}')