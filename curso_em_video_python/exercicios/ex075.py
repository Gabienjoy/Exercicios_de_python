# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.

tupla = (int(input('insira um número:')), int(input('insira um número:')), int(
    input('insira um número:')), int(input('insira um número:')))

print(f'Valores digitados: {tupla}')
print(f'Quantas vezes apareceu o valor 9: {tupla.count(9)} vezes')
if 3 in tupla:
    print(
        f'Em que posição foi digitado o primeiro valor 3: Posição {tupla.index(3) +1} ')
else:
    print(f'O valor 3 não foi digitado.')
print(f'Quais foram os números pares: ')
for n in tupla:
    if n % 2 == 0 and n != 0:
        print(f'{n}')
