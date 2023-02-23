# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

t = int(input('Digite um número que você deseja saber a tabuada: '))

for c in range(0, 11):
    m = t*c
    print(f'{t}x{c}:{m}')
