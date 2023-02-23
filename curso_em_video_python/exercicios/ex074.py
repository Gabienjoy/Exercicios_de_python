# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

import random
'''
numero = random.sample(range(0, 100), 5)
tupla = tuple(numero)


print(f'O número maior da tupla é: {max(tupla)}')
print(f'O número menor da tupla é: {min(tupla)}')
print(tupla)
'''
# solução Guanabara

numero = (random.randint(1, 10), random.randint(1, 10), random.randint(
    1, 10), random.randint(1, 10), random.randint(1, 10))


print(numero)
print(f'O número maior da tupla é: {max(numero)}')
print(f'O número menor da tupla é: {min(numero)}')
