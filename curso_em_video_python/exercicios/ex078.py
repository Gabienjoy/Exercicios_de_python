# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
valores = []
for num in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
a = max(valores)
b = min(valores)
print(f'A lista gerada: {valores}')
print(
    f'O maior valor digitado foi: {max(valores)} e sua posição é {valores.index(a)}')
print(
    f'O menor valor digitado foi: {min(valores)} e sua posição é {valores.index(b)}')
