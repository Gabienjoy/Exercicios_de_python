#Faça um programa que leia 5 números e informe a soma e a média dos números.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))
n5 = int(input('Digite um número: '))


s = 0

for c in n1, n2, n3, n4, n5:
    s = n1 + n2 + n3 + n4 + n5
    m = s/5
print('A soma dos númeos é:', s )
print('A soma dos númeos é:', m )
