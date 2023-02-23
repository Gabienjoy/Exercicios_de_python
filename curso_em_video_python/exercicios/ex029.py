# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Qual é a velocidade do carro? '))

multa = (vel - 80) * 7

if vel > 80:
    print(
        f'A velocidade ultrapassou o limite de 80Km/h! Você foi multado em R${multa:.2f}!')
else:
    print(f'Sua velocidade é {vel}! Boa viagem!')
