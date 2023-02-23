# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER

ano = int(input('Digite o ano de nascimento do atleta: '))
idade = 2022 - ano

if idade <= 9:
    print(
        f' A idade do atleta é {idade} anos. Este se enquadra na categoria MIRIM')
elif idade >= 8 and idade < 14:
    print(
        f' A idade do atleta é {idade} anos. Este se enquadra na categoria INFANTIL')
elif idade >= 15 and idade < 19:
    print(
        f' A idade do atleta é {idade} anos. Este se enquadra na categoria JÚNIOR')
elif idade >= 20 and idade < 25:
    print(
        f' A idade do atleta é {idade} anos. Este se enquadra na categoria SÊNIOR')
elif idade >= 25:
    print(
        f' A idade do atleta é {idade} anos. Este se enquadra na categoria MASTER')
