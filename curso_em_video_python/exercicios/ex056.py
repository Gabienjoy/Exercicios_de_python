# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos
soma_idade = 0
maior_idade_homem = 0
nome_homem_mais_velho = 0
mulher_20_anos = 0

for pessoa in range(1, 5):
    print(f'--------- {pessoa}ª PESSOA---------')
    nome = str(input(f'Digite o nome: ')).strip().lower()
    idade = int(input(f'Digite a idade: '))
    sexo = str(input(f'Digite o sexo [M/F]: ')).strip().lower()
    soma_idade = soma_idade + idade
    if pessoa == 1 and sexo in 'Mn':
        maior_idade_homem = idade
        nome_homem_mais_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulher_20_anos = mulher_20_anos + 1


media_idade = soma_idade/4
print(f'A média do grupo é de:{media_idade} anos')
print(
    f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_homem_mais_velho}')
print(f'Ao todo são {mulher_20_anos} mulheres com menos de 20 anos')
print(soma_idade)
