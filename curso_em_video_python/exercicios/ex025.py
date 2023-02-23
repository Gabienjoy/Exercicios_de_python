# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Digite seu nome completo: ')).strip()
silva = 'silva' in nome.lower()

print(f'Seu nome tem silva? {silva}')

#print('Seu nome tem silva? {}'.format('silva' in nome.lower()))
