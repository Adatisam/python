from random import randint
num = (randint(1,100), randint(1,100), randint(1,100), randint(1,100), randint(1,100), randint(1,100),)
print(f'Foi sorteado os valores:',end='')
for n in num:
    print(f' {n}', end='')
print(f'\nO maior valor é {max(num)}')
print(f'O menor valro é {min(num)}')
