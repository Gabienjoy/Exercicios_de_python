#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# a.salário bruto.
# b.quanto pagou ao INSS.
# c.quanto pagou ao sindicato.
# d.o salário líquido.
# e.calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$

valor = float(input('Digite o valor que você ganha por horas trabalhadas: '))
hora = float(input('Digite o número de horas que você trabalhou neste mês: '))
salario_b = valor * hora
valor_inss = ((8/100) * salario_b)
valor_sind = ((5/100) * salario_b)
valor_ir = ((11/100) * salario_b)
salario_l = (salario_b - valor_inss - valor_ir - valor_sind)

print('O valor do seu salario bruto é: ',salario_b, 'R$')
print('O valor pago ao INSS é de: ',valor_inss, 'R$')
print('O valor pago ao sindicato é de: ',valor_sind, 'R$')
print('O valor do seu salario líquido é: ',salario_l, 'R$')
