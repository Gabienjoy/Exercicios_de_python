# Crie um programa que leia dois valores e mostre um menu na tela:[1] somar [2] multiplicar [3] maior [4] novos números [5] sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
op = 0
while op != 5:
    print('______________MENU_______________')
    print('|        [1] Somar              |')
    print('|        [2] Multiplicar        |')
    print('|        [3] Maior              |')
    print('|        [4] Novos números      |')
    print('|________[5] Sair do programa___|')

    op = int(input('Digite a opção que deseja executar: '))

    if op == 1:
        soma = n1 + n2
        print(f'A soma entre os dois valores é {soma}!')
    elif op == 2:
        mult = n1 * n2
        print(f'A multiplicação entre os dois valores é {mult}!')
    elif op == 3:
        if n1 > n2:
            print(f'O maior valor é {n1}')
        else:
            print(f'O maior valor é {n2}')
    elif op == 4:
        print('Digite novos valores abaixo!')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif op == 5:
        print('Programa encerrado. Obrigada pela visita!')
