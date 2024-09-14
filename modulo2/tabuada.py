num = int(input('Digite um número: '))
for c in range(1, 11):
    print('{} x {:2} = {}'. format(num, c, num * c))

somaidade = 0
mediaidade = 0
maioridadedehomem = 0
novevelho = ''
totmulher20 = 0
for p in range(1, 3):
    print('----{}˚ PESSOA ----'.format(p))
    nome = str(input('Nome: ')).strip
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M]/[F]: ')).strip
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadedehomem = idade
        novevelho = nome
    if sexo in 'Mm' and idade > maioridadedehomem:
        maioridadedehomem = idade
        novevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média da idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadedehomem, novevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))