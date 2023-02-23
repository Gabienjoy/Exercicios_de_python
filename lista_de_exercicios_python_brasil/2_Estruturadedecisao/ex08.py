#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto_1= float(input('Digite o valor do primeiro produto:'))
produto_2= float(input('Digite o valor do segundo produto:'))
produto_3= float(input('Digite o valor do terceiro produto:'))

#print('O produto mais barato é o de valor:', min(produto_1, produto_2, produto_3))

if produto_1 < produto_2 and produto_1 < produto_3:
    print('O produto 1, que custa R$', produto_1,", é a escolha mais barata")

elif produto_2 < produto_1 and produto_2 < produto_3:
    print('O produto 2, que custa R$', produto_2 ,", é a escolha mais barata")

else:
    print('O produto 3, que custa R$', produto_3 ,", é a escolha mais barata")