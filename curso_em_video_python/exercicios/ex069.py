# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos.


pessoas_mais_de_18_anos = 0
homens_cadastrados = 0
mulheres_com_menos_de_20_anos = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [F/M]: ')).strip().upper()[0]

    continuar = str(
        input('Deseja cadastrar mais pessoas [S/N]? ')).strip().upper()[0]

    if idade >= 18:
        pessoas_mais_de_18_anos += 1

    if sexo == 'M':
        homens_cadastrados += 1

    if idade < 20 and sexo == 'F':
        mulheres_com_menos_de_20_anos += 1

    if continuar in 'Nn':
        break

print(f' Foram cadastrados {pessoas_mais_de_18_anos} pessoas com mais de 18 anos, {homens_cadastrados} homens e {mulheres_com_menos_de_20_anos} mulheres com menos de 20 anos.')
print('Fim do programa.')
