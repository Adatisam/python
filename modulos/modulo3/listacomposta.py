pessoa = list()
dado = list()
maior = menor = 0
for c in range(0, 4):
    pessoa.append(str(input('Nome: ')))
    pessoa.append(int(input('Idade: ')))
    dado.append(pessoa[:])
    dado.clear()
for p in dado:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        maior +=1
    else:
        print(f'{p[0]} é menor de idade')
        menor +=1
print(f'Temos {maior} maiores e {menor} menores de idade')