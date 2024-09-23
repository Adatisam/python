pessoa = {'nome': 'Matheus', 'sexo': 'M', 'idade': 22}
print(pessoa)
print(pessoa['nome'])
print(f'O {pessoa["nome"]} tem {pessoa["idade"]} anos com sexo {pessoa["sexo"]}.')
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
#for k in pessoa.keys():
    #print(k)
#for i in pessoa.items():
    #print(i)
#for v in pessoa.values():
    #print(v)
pessoa['nome'] = 'Murilo'
print(pessoa)
for m, n in pessoa.items():
    print(f'{m} = {n}')