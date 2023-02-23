# Aprimore o desafio anterior, mostrando no final:  A) A soma de todos os valores pares digitados.B) A soma dos valores da terceira coluna.C) O maior valor da segunda linha.

matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma= soma_coluna = maior = 0

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input('Digite um número: '))
        if matriz[linha][coluna] % 2 == 0:
            soma += matriz[linha][coluna]


for linha in range(3):
    for coluna in range(3):
        print(f'{matriz[linha][coluna]}', end=' ')
    print()

print('*' *30)
for linha in range(0,3):
    soma_coluna += (matriz[linha][2])
print(f'A soma dos valores da terceira coluna é {soma_coluna}')
print(f'A soma dos valores pares é: {soma}')
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior}')