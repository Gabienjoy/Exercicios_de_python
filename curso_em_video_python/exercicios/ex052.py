# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n1 = int(input('Digite um número: '))
div = 0
for c in range(1, n1 + 1):
    if n1 % c == 0:
        print('\033[33m', end='')
        div = div + 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
print(f'\n\033[mO número {n1} foi divisivel {div} vezes.')

if div == 2:
    print(f'E por isso, o número {n1} é primo.')
else:
    print(f'E por isso, o número {n1} não é primo.')
