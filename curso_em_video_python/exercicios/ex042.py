# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

reta1 = int(input('Digite o comprimento da reta 1: '))  # 16
reta2 = int(input('Digite o comprimento da reta 2: '))  # 20
reta3 = int(input('Digite o comprimento da reta 3: '))  # 30

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print(f'Essas retas podem formar um triangulo!')
else:
    print(f'Essas retas não podem formar um triangulo!')

if reta1 == reta2 == reta3:
    print(f'O triangula é equilátero')
elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
    print(f'O triangula é isósceles')
else:
    print(f'O triangula é escaleno!')
