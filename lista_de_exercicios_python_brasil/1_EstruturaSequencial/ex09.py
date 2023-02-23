#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

far = float(input('Informe a temperatura em Fahrenheit: '))
cel = 5 * ((far-32) / 9)

print('A temperatura informada em Celsius é: ', cel)
