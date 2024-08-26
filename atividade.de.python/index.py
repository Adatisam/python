print('Para sabermos quanto de tinta sera usado, Digite:')
lado1 = float(input('Um lado da parede: '))
lado2 = float(input('Um outro lado da parede: '))
altura = float(input('A altura da parede: '))
volume = lado1 * lado2 * altura
print('Para pintar tudo sera necessario', volume, 'm3')