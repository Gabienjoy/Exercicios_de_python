# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

a1 = input('Primeiro aluno(a):')
a2 = input('Segundo aluno(a): ')
a3 = input('Terceiro aluno(a): ')
a4 = input('Quarto aluno(a): ')
lista = [a1, a2, a3, a4]
escolhido = choice(lista)

print(f'O aluno(a) escolhido foi {escolhido}')
