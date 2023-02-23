# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import choice

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolhido = choice(lista)
n = int(input('Adivinhe o número que o computador vai escolher de 0 a 10: '))
palpite = 0
while n != escolhido:
    n = int(input(
        f'Você errou, tente novamente!!\n' 'Adivinhe o número que o computador vai escolher de 0 a 10:'))
    palpite += 1
print(
    f'O número escolhido foi {escolhido}. Parabéns, você acertou depois de {palpite} tentativas!')
