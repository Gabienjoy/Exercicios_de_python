# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('Sara', 'Gabrielle', 'Gabriel', 'Karoline', 'Otair', 'Monica')

for nome in palavras:
    print(f'\nNo nome {nome} existem as vogais: ', end='')
    for letra in nome:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
