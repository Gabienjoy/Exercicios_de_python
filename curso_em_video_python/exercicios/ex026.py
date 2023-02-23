# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

from itertools import count


frase = str(input('Digite uma frase: '))
a = frase.upper().count('A')
b = frase.upper().find('A') + 1
c = frase.upper().rfind('A') + 1

print(f'A letra A  apareceu: {a} vezes')
print(f'A primeira letra A apareceu na posição {b}')
print(f'A primeira letra A apareceu na posição {c}')
