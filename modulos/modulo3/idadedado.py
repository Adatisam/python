galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()
        if pessoa['sexo'] in 'MF':
            break
        print('Por favor digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()
        if resp in 'SN':
            break
        print('ERRO! responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*20)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f} anos.')
print(f'As mulheres cadastradas foram ',end='')
for p in galera:
    if p["sexo"] == 'F':
        print(f'{p["nome"]} ',end='')
print('A lista de pessoas que estão acima da média: ',end='')
for p in galera:
    if p["idade"] >= media:
        print('')
        for k, v in p.items():
            print(f'{k} = {v}; ',end='')
        print('')
print('ENCERRADO')