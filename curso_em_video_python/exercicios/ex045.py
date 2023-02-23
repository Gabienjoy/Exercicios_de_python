# Crie um programa que faça o computador jogar Jokenpô com você.
from random import choice

lista = [1, 2, 3]
jogada_pc = choice(lista)

print('VAMOS JOGAR JOKENPÔ?')
print('ESCOLHA ENTRE PEDRA, PAPEL E TESOURA!')

jogada = int(input('Digite 1- PEDRA, 2- PAPEL OU 3- TESOURA: '))

print(f'O computador escolheu: {jogada_pc}')


if jogada_pc == jogada:
    print('Empate, tente novamente!')
elif jogada_pc == 1 and jogada == 2:
    print('Você ganhou!')
    print('Pedra perde para papel.')
elif jogada_pc == 1 and jogada == 3:
    print('Você perdeu!')
    print('Pedra vence tesoura.')
elif jogada_pc == 2 and jogada == 1:
    print('Você perdeu!')
    print('Papel vence pedra.')
elif jogada_pc == 2 and jogada == 3:
    print('Você ganhou!')
    print('Papel perde tesoura.')
elif jogada_pc == 3 and jogada == 1:
    print('Você ganhou!')
    print('Tesoura perde para pedra.')
elif jogada_pc == 3 and jogada == 2:
    print('Você perdeu!')
    print('Tesoura vence papel.')
