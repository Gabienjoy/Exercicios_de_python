# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

cont = soma = media = 0
media = 0
n = 1
resposta = 'S'
while resposta in 'Ss':
    soma += n
    cont += 1
    n = int(input('Digite um número inteiro: '))
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resposta = str(input('Deseja continuar[S/N]? '))

media = soma/cont
print(
    f'Você digitou {cont} númeoros e a média entre eles é {media}, o maior número é {maior} e o menor é {menor}')
