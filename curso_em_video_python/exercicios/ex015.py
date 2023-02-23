# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Qual Km percorrido pelo carro? '))
dia = float(input('Por quantos dias você alugou o carro? '))

aluguel_dia = dia * 60
aluguel_km = km * 0.15
aluguel_total = aluguel_dia + aluguel_km

print(f'O valor total do aluguel do carro é R${aluguel_total:.2f}')
