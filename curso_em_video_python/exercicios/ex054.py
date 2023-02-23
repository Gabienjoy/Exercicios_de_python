# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date  # importa a data atual
ano_atual = date.today().year  # omporta o ano atual

maior = 0
menor = 0

for pessoa in range(1, 8):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {pessoa}ª: '))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        maior = maior + 1
    else:
        menor = menor + 1

print(f'A quantidade de pessoas que atingiram a maior idade é: {maior}')
print(f'A quantidade de pessoas que não atingiram a maior idade é: {menor}')
