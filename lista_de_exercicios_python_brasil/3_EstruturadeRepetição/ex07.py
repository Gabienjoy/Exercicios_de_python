#Faça um programa que leia 5 números e informe o maior número.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))
n5 = int(input('Digite um número: '))

maior= 0
for n in n1, n2, n3, n4, n5:
    if maior > n:
        maior = maior
    else:
        maior = n

print('O maior número entre eles é' , maior)
