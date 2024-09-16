print('===' *10)
print('10 TERMOS DE UMA PA')
print('===' *10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo, razao):
    print('{}'. format(c), end=' -> ')
print('FIM')

print('===' *10)
print('10 TERMOS DE UMA PA 2.0')
print('===' *10)
prim = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
dec = 1
while dec <= 10:
    print('{} -> '.format(prim), end=' ')
    prim += raz
    dec += 1
mais = int(input('Quantos termos você quer mostrar a mais? '))