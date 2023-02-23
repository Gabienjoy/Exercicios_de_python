# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros

preco = float(input('Digite o preço do produto: '))

print("""                       MODOS DE PAGAMENTO
            (1) à vista dinheiro/cheque: 10 % de desconto
            (2) à vista no cartão: 5 % de desconto
            (3) até 2x no cartão: preço formal
            (4) 3x ou mais no cartão: 20 % de juros""")


pagar = int(input('Como deseja realizar a forma de pagamento? '))

dinheiro_cheque = 1
cartao_vista = 2
cartao_2vz = 3
cartao_3vz = 4

if pagar == 1:
    valor1 = preco - (preco * 0.1)
    print(
        f'O valor do produto é R${preco}, no pagamento à vista no dinheiro/cheque o valor dele é R${valor1}!')
elif pagar == 2:
    valor2 = preco - (preco * 0.05)
    print(
        f'O valor do produto é R${preco}, no pagamento à vista no cartão o valor dele é R${valor2}!')
elif pagar == 3:
    print(
        f'O valor do produto é R${preco}, no pagamento em até 2x no cartão o valor dele é continua o mesmo! ')
elif pagar == 4:
    valor3 = preco * 0.2 + preco
    print(
        f'O valor do produto é R${preco}, no pagamento em 3x ou mais no cartão o valor dele é R${valor3}!')
