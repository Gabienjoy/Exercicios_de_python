# Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo

while True:
    t = int(input('Digite um número que você deseja saber a tabuada: '))
    if t < 0:
        break
    for c in range(1, 11):
        m = t*c
        print(f'{t}x{c}:{m}')


print('Programa interrompido. O número digitado é negativo!')
