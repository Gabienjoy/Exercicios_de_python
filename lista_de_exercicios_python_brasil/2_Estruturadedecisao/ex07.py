#Faça um Programa que leia três números e mostre o maior e o menor deles.

n1= float(input('Digite um número:'))
n2= float(input('Digite um número:'))
n3= float(input('Digite um número:'))

#Mostre o maior deles

#print('O maior número é:', max (n1, n2, n3))

if n1 > n2 and n1 > n3:
    print('O maior número é', n1)

elif n2 > n1 and n2 > n3:
    print('O maior número é', n2) 

else:
    print('O maior número é', n3) 

#Mostre o menor deles

#print('O maior número é:', min (n1, n2, n3))

if n1 < n2 and n1 < n3:
    print('O menor número é', n1)

elif n2 < n1 and n2 < n3:
    print('O menor número é', n2) 

else:
    print('O menor número é', n3)
