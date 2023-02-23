#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

h= float(input('Informe sua altura:' ))

peso_h = round((72.7 * h) - 58, 2)
peso_m = round((62.1 * h) - 44.7, 2)

print('Se você for homem, seu peso ideal é: ', peso_h)
print('Se você for mulher, seu peso ideal é: ', peso_m)
