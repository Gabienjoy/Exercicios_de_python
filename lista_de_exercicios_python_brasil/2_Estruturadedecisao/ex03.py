#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

letra= input('Digite o sexo: ')

if letra == 'm' or  letra == 'M':
    print('Masculino')

elif letra== 'F' or letra == 'f':
    print('Feminino')

else:

    print ('Sexo inválido!')
    print('O sexo digitado foi,', letra)

