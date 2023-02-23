# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

# pessoas = {'nome': 'Gabi', 'sexo': 'F', 'Idade': 25}
# del pessoas['sexo']
# pessoas['nome'] = 'Gabriel'
# pessoas['Peso'] = 75
# for k, v in pessoas.items():
#     print(f' {k}: {v}')

aluno = {}

aluno['Nome'] = str(input('Digite o nome do aluno: '))
aluno['Média'] = float(input(f'Digite a média de {aluno["Nome"]}: '))

if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
if aluno['Média'] < 7 and aluno['Média'] > 5:
    aluno['Situação'] = 'Recuperação'
if aluno['Média'] < 5:
    aluno['Situação'] = 'Reprovado'


for k, v in aluno.items():
    print(f'{k}: {v}')
