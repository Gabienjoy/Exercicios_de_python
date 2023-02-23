# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = (input('Digite seu nome completo: ')
        ).strip()  # strip elimina os espaços
# diminuindo o tamanho da string pela quantidade de espaços

tamanho = (len(nome) - nome.count(' '))
tamanho_primeiro_nome = nome.find(' ')

print(f'Seu nome: {nome}')
print(f'Seu nome em letras minusculas: {nome.lower()}')
print(f'Seu nome em letras maiusculas: {nome.upper()}')
print(f'Seu nome tem ao todo: {tamanho} letras')
# procurei o primeiro espaço entre uma palavra e outra e o programa retonou a quantidade de letras do primeiro nome
print(f'Seu primeiro nome tem ao todo: {tamanho_primeiro_nome} letras')
