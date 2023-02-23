# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print('GERADOR DE PA!')


n1 = int(input('Primeiro termo: '))
n2 = int(input('Razão: '))
termo = n1
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end=' ')
        termo = termo + n2
        cont += 1
    print('Pausa!')
    mais = int(input('Você deseja mostrar quantos termos a mais? '))

print('Fim da PA!')
