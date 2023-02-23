#Faça um programa que peça uma nota, entre zero e dez. 
#Mostre uma mensagem caso o valor seja inválido 
#Continue pedindo até que o usuário informe um valor válido.

nota= int(input('Nota: '))
while not (nota >= 0 and nota <= 10):
    print('Inválido')
    nota= int(input('Nota: '))
print('Nota válida!')



