'''Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';'''


nome = input('Digite um nome:')
if len(nome) > 3:
    pass
else:
    while not len(nome) > 3:
        print('Nome inválido!')
        nome = input('Digite um nome:')
print('Nome válido!')


idade = int(input('Digite a idade:'))
if idade >= 0 and idade <= 150:
        pass
else: 
    while not (idade >= 0 and idade <= 150): 
        print('Idade inválida')
        idade = int(input('Digite a idade:'))
print('Idade válida')



salario = float(input('Digite o salário:'))
if salario >0:
    pass
else:
    while not salario > 0:
        print('Salário inválido')
        salario = float(input('Digite um salário válido:'))
print('Salário Válido!')


sexo= input('Digite o sexo:') .lower()
if sexo == 'm' or sexo == 'f':
    pass
else:
    while not (sexo == 'm' or sexo == 'f'):
        print('Sexo inválido')
        sexo = input('Digite a sexo:')
print('Sexo Válido!')


estado_civil = input('Digite o estado civil:') .lower()
if estado_civil in "scvd":
    pass
else:
    while not (estado_civil in "scvd"):
        print('Estado civil inválido')
        estado_civil = input('Digite o estado civil:') .lower()
print('Estado civil Válido!')