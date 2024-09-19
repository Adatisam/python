lista = []
while True:
    lista.append(int(input('Digite o valor: ')))
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()      
    if resp == 'N':
        break
print('=-='*10)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
