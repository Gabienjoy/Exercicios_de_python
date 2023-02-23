#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

usuario= input('Insira um nome de usuário: ')
senha= input('Insira uma senha: ')

while senha == usuario:
        print('Senha inválida')
        senha= (input('Insira uma senha: '))
print('Senha válida!')



