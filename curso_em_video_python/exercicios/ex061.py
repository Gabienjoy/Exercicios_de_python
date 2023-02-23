# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão: '))
termo = n1
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end=' ')
    termo = termo + n2
    cont += 1
print('Fim!')
