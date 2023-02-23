# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é oseu salário? '))
anos = int(input('Em quantos anos você pretende terminar de pagar a casa? '))

prestacao = valor_casa / (anos * 12)

if prestacao > salario * 0.30:
    print(
        f'O valor da prestação será de R${prestacao:.2f} para ser pago em {anos} anos. Seu empréstimo foi negado, pois a parcela ultrapassa 30% do seu salário!')
else:
    print(
        f'O valor da prestação será de R${prestacao:.2f} para ser pago em {anos} anos. Seu empréstimo será concedido!')
