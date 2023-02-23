# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase qualquer: ')
            ).strip().lower()  # strip elimina os espaços

palavras = frase.split()
# separa a frase em palavras


junto = ''.join(palavras)
# junta as palavras sem espaço ou com algum elemento que estiver dentro do '' EX: '*'

#print(f'A frase: {frase}, a palavras {palavras} e tudo junto {junto}')

inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]

if inverso == junto:
    print(f'A frase: {frase} é um Palindromo')
else:
    print(f'A frase: {frase} não é um Palindromo')

print(junto, inverso)
