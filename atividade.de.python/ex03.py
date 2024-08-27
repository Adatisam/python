import emoji
print(emoji.emojize("Olá, Mundo! :earth_americas:", use_aliases=True))

from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadrada de {} é de {:.2f}' .format(num, floor(raiz)))

import random
num2 = random.randint(1, 50)
print('Enquanto voce escolhe {} eu escolho {}' .format(num, num2))