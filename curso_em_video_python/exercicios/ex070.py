# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre: A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato.

produto_mais_barato = produto_mais_caro = 0
total = preco = mais_de_1000 = produtos = 0
maior_preco = menor_preco = 0


while True:
    print('*' * 30)
    print('     CARRINHO DE COMPRAS')
    print('*' * 30)
    nome = str(input('Digite o nome do produto: ')).strip().upper()
    preco = float(input('Digite o preço: R$'))
    print('*' * 30)
    continuar = str(
        input('Deseja cadastrar mais pessoas [S/N]? ')).strip().upper()[0]

    total += preco
    produtos += 1

    if preco >= 1000:
        mais_de_1000 += 1

    if produtos == 1:
        preco = maior_preco = menor_preco
        produto_mais_barato = produto_mais_caro = nome

        if preco > maior_preco:
            maior_preco = preco
            produto_mais_caro = nome

        if preco < menor_preco:
            menor_preco = preco
            produto_mais_barato = nome

    if continuar == 'N':
        break


print(f'O total gasto na compra é de R${total:.2f}')
print(f'A quantidade de produtos que custam mais de R$1000 é {mais_de_1000}')
print(
    f'O produto mais barato é {produto_mais_barato}, que custa R$ {menor_preco} e o produto mais caro é {produto_mais_caro}, que custa R${maior_preco}.')
# if de preço não ta funcionando
