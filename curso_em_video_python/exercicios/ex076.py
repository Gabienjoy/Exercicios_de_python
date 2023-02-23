# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

lista = ('Arroz', 5.99, 'Feijão', 6.85, 'Mel', 15.90, 'Farinha', 2.99, 'Aveia',
         2.50, 'Leite', 4.99, 'Ovos', 10.99, 'Refrigerante', 6.5, 'Chocolate', 4, 'Chá', 2)

print('*' * 40)
print(f'{"Produtos":^40}')
print('*' * 40)

for prod in range(0, len(lista)):
    if prod % 2 == 0:
        print(f'{lista[prod]:<30}', end='')
    else:
        print(f'R${lista[prod]:>8.2f}')
print('*' * 40)
