# Faça um programa que leia a idade de um jovem e informe, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

idade = int(input('Digite sua idade: '))
idade_meses = idade * 12
#idade_meses_para_alistamento = 216
tempo = idade_meses - 216
tempo_positivo = 216 - idade_meses
anos_positivo = 18 - idade
anos = idade - 18


if idade < 18:
    print(
        f'Você tem {idade} anos, faltam {anos_positivo} anos ({tempo_positivo} meses) para você se alistar.')

elif idade == 18:
    print(f'Você tem {idade} anos, é a hora exata para você se alistar.')

elif idade > 18:
    print(
        f'Você tem {idade} anos, você passou {anos} anos ({tempo} meses) do prazo para se alistar.')


# FAZER DEPOIS Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
