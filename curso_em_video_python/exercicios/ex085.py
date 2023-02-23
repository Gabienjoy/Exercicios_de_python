# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
lista = [[],[]]
num= 0

for v in range(7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        if num % 2 == 1:
            lista[1].append(num)
  

print(f' Os valores digitados: {lista}')
lista[0].sort()
print(f' Os valores pares digitados: {lista[0]}')
lista[1].sort()
print(f' Os valores impares digitados: {lista[1]}')
