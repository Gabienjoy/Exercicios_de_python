#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a.o produto do dobro do primeiro com metade do segundo .
#b.a soma do triplo do primeiro com o terceiro.
#c.o terceiro elevado ao cubo.

n1= int(input('Digite um número inteiro: '))
n2= int(input('Digite mais um número inteiro: '))
n3= float(input('Digite um número real: '))

a= ((n1*2) * (n2/2))
b= ((n1*3)+n3)
c= (n3**3)

print('O produto do dobro do primeiro com metade do segundo é: ', a)
print('A soma do triplo do primeiro com o terceiro é: ', b)
print('O terceiro elevado ao cubo: ', c)




