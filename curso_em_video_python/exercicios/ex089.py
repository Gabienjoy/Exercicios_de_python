# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
ficha = []
while True:
    nome = str(input('Nome: '))    
    nota1 = float(input('Nota 1: '))    
    nota2 = float(input('Nota 2: '))
    media= (nota1 + nota2) / 2 
    ficha.append([[nome], [nota1], [nota2], [media]])
    resp= str(input('Deseja continuar?[s/n] '))
    if resp in 'Nn':
        break
print(ficha)

print(f"{'ID'}  {'Nome'}  {'Média'}")
for i, a in enumerate(ficha):
    print(f'{i}  {a[0]}  {a[3]}')
while True:
    op= int(input('Mostrar notas de qual aluno?(999 interrompe): '))
    if op == 999:
        break
    if op <= len(ficha) - 1:
        print(f'Notas de {ficha[op][0]} são {ficha[op][1]} e {ficha[op][2]}')
