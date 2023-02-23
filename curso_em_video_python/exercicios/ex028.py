# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import choice

lista = [0, 1, 2, 3, 4, 5]
escolhido = choice(lista)
n = int(input('Adivinhe o número que o computador vai escolher de 0 a 5: '))

if n == escolhido:
    print(f'O número escolhido foi {escolhido}. Parabéns, você acertou!')
else:
    print(f'O número escolhido foi {escolhido}. Você errou, tente novamente!')

# Poderia usar randint: from randint import randint ---> numero = randint(0,5)
