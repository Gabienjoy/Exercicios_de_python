#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

from math import ceil, floor

area = float(input('Digite o tamanho em metros² da area a ser pintada: '))
litros_por_area= (area*1.1)/6

# 1 lata = 108 metros² 
# 1 galão = 21.6 metros

#1 questão
lata = 18
quant_latas = ceil(litros_por_area/lata)
valor= quant_latas* 80

print('A quantidade de latas é', quant_latas ,', e o valor é, R$', valor)

#2 questão
galao= 3.6
quant_galao= ceil(litros_por_area/galao)
valor_galao = quant_galao*25

print('A quantidade de galão é', quant_galao,', e o valor é R$', valor_galao)

#3 questão
quant_latas_3= floor(litros_por_area/lata)
falta_pintar= (litros_por_area/lata)- quant_latas_3
quant_galao2 = ceil(falta_pintar/galao)
valor_misturado_galao= quant_galao2*25
valor_misturado_lata= quant_latas_3*80
valor_total= valor_misturado_lata + valor_misturado_galao


print('A quantidade de latas a serem compradas é', quant_latas_3, ', e a quantidade de galões é', quant_galao2, 'O valor total é', valor_total)