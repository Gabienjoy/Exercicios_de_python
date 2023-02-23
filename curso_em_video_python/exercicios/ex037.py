# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input('Digite um número inteiro qualquer: '))
print('''Escolha a base de conversão:
[1] Binário
[2] Octal
[3] Hexadecimal''')
base = int(input('Escolha sua opção: '))

if base == 1:
    b = bin(n)
    print(f'O número {n} convertido para Binário é igual a {b[2:]}')

elif base == 2:
    o = oct(n)
    print(f'O número {n} convertido para Octal é igual a {o[2:]}')
elif base == 3:
    h = hex(n)
    print(f'O número {n} convertido para Hexadecimal é igual a {h[2:]}')
else:
    print(f'Opção inválida!')
# Usando o {
# [2:] eu corto os dois primeiros digitos do resultado da conversão que não precisam aparecer.
