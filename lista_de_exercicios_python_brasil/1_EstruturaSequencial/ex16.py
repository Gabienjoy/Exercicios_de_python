#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

from math import ceil

area = float(input('Digite o tamanho em metros² da area a ser pintada: '))
litro = area /3
lata = ceil (litro /18)
preco= lata * 80

print('A quantidade de latas a serem compradas é:', lata)
print('O valor total da compra vai ser de:', preco, 'R$')
