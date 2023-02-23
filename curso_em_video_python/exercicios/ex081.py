# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.

valor = []

while True:
    for c in range(0, 5):
        n = int(input('Digite um valor: '))
        if n > 0:
            valor.append(n)
    resp = str(input('Deseja inserir mais números?[S/N] '))
    if resp in 'Nn':
        break
print(f'Quantidade de números digitados na lista cadastrada: {len(valor)}')
print(f'Lista cadastrada: {valor}')
valor.sort(reverse=True)
print(f'Lista cadastrada em ordem decrescente: {valor}')
print(f'Vezes me que o valor 5 aparece na lista cadastrada: {valor.count(5)}')
