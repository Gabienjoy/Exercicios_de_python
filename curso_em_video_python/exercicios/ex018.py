# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
# para usar as funções seno, conseno e tangente precisa converter o número para radiano

from math import cos, tan, sin, radians

ang = float(input('Digite o angulo que você deseja: '))

seno = sin(radians(ang))
coseno = cos(radians(ang))
tangente = tan(radians(ang))

print(
    f'O valor do seno, coseno e tangente, é, respectivamente: {seno:.2f}, {coseno:.2f}, {tangente:.2f}')
