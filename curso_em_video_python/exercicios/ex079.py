# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valor = []

while True:
    n = int(input('Digite um valor: '))
    if n not in valor:
        valor.append(n)
    else:
        print('Valor já se encontra na lista. Tente novamente.')
    resp = str(input('Deseja inserir mais números?[S/N] '))
    if resp in 'Nn':
        break

print(f'Lista cadastrada: {valor}')
print(f'Lista em ordem crescente: {sorted(valor)}')
