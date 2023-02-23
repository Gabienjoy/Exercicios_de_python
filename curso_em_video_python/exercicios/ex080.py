# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []


for id in range(0, 5):
    n = int(input('Digite um valor: '))
    if id == 0 or id > lista[-1]:
        lista.append(n)
    else:
        posicao = 0
        while posicao < len(lista):
            if n <= lista[posicao]:
                lista.insert(posicao, n)
                break
            posicao += 1

print(f'Lista cadastrada: {lista}')

# SOLUÇÃO DO GUANABARA MAS NÃO FUNCIONA
