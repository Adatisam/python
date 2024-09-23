from random import randint
from operator import itemgetter
jogo = {'Jogador1': randint(1, 20),
        'Jogador2': randint(1, 20),
        'Jogador3': randint(1, 20),
        'Jogador4': randint(1, 20)}
ranking = list()
print('Os valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
ranking = sorted(jogo.items(), key= itemgetter(1), reverse= tuple)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
