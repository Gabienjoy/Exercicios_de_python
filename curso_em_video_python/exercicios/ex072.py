# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.


extenso = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',  'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',  'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove',  'Vinte'

while True:
    n = int(input('Digite um número de 0 até 20: '))

    if n == 0:
        print(extenso[0])
    if n == 1:
        print(extenso[1])
    if n == 2:
        print(extenso[2])
    if n == 3:
        print(extenso[3])
    if n == 4:
        print(extenso[4])
    if n == 5:
        print(extenso[5])
    if n == 6:
        print(extenso[6])
    if n == 7:
        print(extenso[7])
    if n == 8:
        print(extenso[8])
    if n == 9:
        print(extenso[9])
    if n == 10:
        print(extenso[10])
    if n == 11:
        print(extenso[11])
    if n == 12:
        print(extenso[12])
    if n == 13:
        print(extenso[13])
    if n == 14:
        print(extenso[14])
    if n == 15:
        print(extenso[15])
    if n == 16:
        print(extenso[16])
    if n == 17:
        print(extenso[17])
    if n == 18:
        print(extenso[18])
    if n == 19:
        print(extenso[19])
    if n == 20:
        print(extenso[20])

    resp = str(input('Deseja continuar? [s/n] '))
    if resp in 'Nn':
        break
print('Fim do programa')


'''
Resolução Guanabara
while True:
    n = int(input('Digite um número de 0 até 20: '))
    if 0 <= n <= 20:
        break
    print(f'Tente noamente. ', end='')
print(f'Número digitado: {extenso[n]}')'''


'''while n == c:
    n = int(input('Digite um número de 0 até 20: '))
    c += 1
    print(extenso[c])
    #resp = str(input('Deseja continuar? '))

for c in range(0,21):
    n = int(input('Digite um número de 0 até 20: '))
    if n == c:
        print(extenso[c])'''
