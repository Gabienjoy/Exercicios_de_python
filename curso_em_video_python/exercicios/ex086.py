# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0,0,0],[0,0,0],[0,0,0]]

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input('Digite um número: '))

for linha in range(3):
    for coluna in range(3):
        print(f'{matriz[linha][coluna]}', end=' ')
    print()







'''matriz = [ [0 for i in range(4)] for j in range(4)]
count=0


for linha in range(4):
    for coluna in range(4):
        matriz[linha][coluna] = count
        count += 1

for linha in range(4):
    for coluna in range(4):
        print("%4d" % matriz[linha][coluna], end='')
    print()'''
