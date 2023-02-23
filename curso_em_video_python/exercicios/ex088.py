# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
import enum
from random import randint

lista= []
jogo=[]
quant= int(input('Quantos jogos você deseja? '))
total= 1
while total <= quant:
    conta = 0
    while True:
        num= randint(1,60)
        if num not in lista:
            lista.append(num)
            conta += 1
        if conta >= 6:
            break
    lista.sort()
    jogo.append(lista[:])
    lista.clear()
    total += 1 
for i, l in enumerate(jogo):
    print(F'A lista de jogos gerados é {i+1}: {l}')
