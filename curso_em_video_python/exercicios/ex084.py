# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) Uma listagem com as pessoas mais pesadas.C) Uma listagem com as pessoas mais leves.

pessoas = []
pessoas_pesadas = []
pessoas_leves = []
pessoas_cadastradas = 0
peso_pesadas = 60
peso_leves = 60
nome_pesadas = 0
nome_leves = 0

while True:
    for c in range(0, 3):
        nome = str(input('Digite o nome: '))
        peso = float(input('Digite o peso: '))
        pessoas.append(nome)
        pessoas.append(peso)
        if pessoas_cadastradas == 1:
            peso = peso_pesadas = peso_leves
            nome_leves = nome_pesadas = nome
        if peso > peso_pesadas:
            #peso = peso_pesadas
            nome_pesadas = nome
            pessoas_pesadas.append(nome)
            pessoas_pesadas.append(peso)
        if peso < peso_leves:
            #peso = peso_leves
            nome_leves = nome
            pessoas_leves.append(nome)
            pessoas_leves.append(peso)
    pessoas_cadastradas += 3
    resp = str(input('Deseja adicionar mais pessoas?[S/N] '))
    if resp in 'Nn':
        break
print(f'A lista de pessoas cadastradas: {pessoas}')
print(f'A quantidade depessoas cadastradas na lista: {pessoas_cadastradas}')
print(f'A listagem de pessoas mais leves: {pessoas_leves}')
print(f'A listagem de pessoas mais pesadas: {pessoas_pesadas}')
