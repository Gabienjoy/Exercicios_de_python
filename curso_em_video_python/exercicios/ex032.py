# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from _datetime import date
ano = int(input('Digite um ano: '))

if ano == 0:
    ano = date.today().year

if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print(f'O ano de {ano} é bissexto')
else:
    print(f'O ano de {ano} não é bissexto')
