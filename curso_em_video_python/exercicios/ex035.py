# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

reta1 = int(input('Digite o comprimento da reta 1: '))  # 16
reta2 = int(input('Digite o comprimento da reta 2: '))  # 20
reta3 = int(input('Digite o comprimento da reta 3: '))  # 30

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print(f'Essas retas podem formar um triangulo!')
else:
    print(f'Essas retas não podem formar um triangulo!')
