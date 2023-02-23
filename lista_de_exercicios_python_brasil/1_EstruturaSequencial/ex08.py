#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor = float(input('Digite o valor que você ganha por horas trabalhadas: '))
hora = float(input('Digite o número de horas que você trabalhou: '))
salario = valor * hora
print('O valor total do seu salario por horas trabalhadas é: ',salario, 'R$')