# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o seu salario: '))

if salario > 1250:
    aumento = (0.1 * salario) + salario
    print(f'O seu salário com aumento de 10% é R${aumento:.2f}!')
elif salario <= 1250:
    aumento = (0.15 * salario) + salario
    print(f'O seu salário com aumento de 15% é R${aumento:.2f}!')
