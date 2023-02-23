# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

print('*'*20)
print('    ÍMPAR OU PAR?')
print('*'*20)
print('    Vamos jogar?')
print('*'*20)
v = 0

while True:
    computador = randint(1, 11)
    jogador = int(input(('Escolha um valor: ')))
    total = computador + jogador
    tipo = ' '
    while tipo not in 'IP':
        tipo = str(input(('Escolha ímpar ou par [I/P]: '))).strip().upper()[0]
    print(
        f' Você jogou {jogador} e o computador jogou {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('*'*20)
            print('Você venceu!')
            print('*'*20)
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('*'*20)
            print('Você venceu!')
            print('*'*20)
            v += 1
        else:
            print('*'*20)
            print('Você perdeu!')
            print('*'*20)

            break
    print('Vamos jogar novamente...')
print(f'Gamer Over! Você venceu {v} vezes!!')
