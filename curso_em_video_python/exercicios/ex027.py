# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
ult = (nome[len(nome)-1])

print(f'Seu primeiro nome é: {nome[0]}')
print(f'Seu último nome é: {ult}')