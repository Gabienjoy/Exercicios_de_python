#: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista1 = []
lista2 = []
lista3 = []

while True:
    for c in range(0, 5):
        n = int(input('Digite um valor: '))
        if n > 0:
            lista1.append(n)
        if n % 2 == 0:
            lista2.append(n)
        if n % 2 == 1:
            lista3.append(n)
    resp = str(input('Deseja inserir mais números?[S/N] '))
    if resp in 'Nn':
        break
    
print(f'Lista cadastrada: {lista1}')
print(f'Números pares da lista cadastrada: {lista2}')
print(f'Números impares da lista cadastrada: {lista3}')
