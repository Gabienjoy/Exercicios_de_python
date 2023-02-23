# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão: '))
dez = n1 + (10-1) * n2

for c in range(n1, dez + n2, n2):
    print(f'{c}')
