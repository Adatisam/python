from math import factorial
num = int(input('Digite um número para calcular seu fatorial: '))
fac = factorial(num)
while num > 0:
    print('{}'.format(num), end=' ') 
    print(' x ' if num > 1 else ' = ', end=' ')
    num -= 1
print(fac)

print('-=' *10)

def fatorial(n, show = False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ',end='')
            else:
                print(' = ',end='')
        f *= c
    return f
print(fatorial(5, show=True))