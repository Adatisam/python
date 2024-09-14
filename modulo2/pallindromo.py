frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('Você digitou {} e o inverso é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palídromo!')
else:
    print('A frase digitada não é palídromo!')
