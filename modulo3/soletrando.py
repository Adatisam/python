palavra = str(input('Digite a palavra para o SOLETRANDO: '))
for p in palavra:
    print(f'\nNa palavra {palavra.upper()}, temos ',end='')
    for letra in p:
        if letra.lower() in 'qwertyuiopçlkjhgfdsazxcvbnm':
            print(letra, end='')