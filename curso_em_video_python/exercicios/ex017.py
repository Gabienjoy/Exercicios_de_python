# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import pow, sqrt, hypot

oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento de cateto adjacente: '))

#hipo = sqrt(pow(oposto, 2) + pow(adjacente, 2))
hipo = hypot(oposto, adjacente)

print(f'O valor da hipotenusa é: {hipo:.2f}')
