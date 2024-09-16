from math import factorial
num = int(input('Digite um número para calcular seu fatorial: '))
fac = factorial(num)
while num > 0:
    print('{}'.format(num), end=' ') 
    print(' x ' if num > 1 else ' = ', end=' ')
    num -= 1
print(fac, end=' ')