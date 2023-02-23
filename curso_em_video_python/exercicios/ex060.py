# Faça um programa que leia um número qualquer e mostre o seu fatorial.

from math import factorial

n = int(input('Digite um valor para saber seu fatorial: '))
f = factorial(n)
c = n

while c > 0:
    print(f'{c}', end='')
    print(' x' if c > 1 else '=', end=' ')
    c -= 1

print(f'{f}')
