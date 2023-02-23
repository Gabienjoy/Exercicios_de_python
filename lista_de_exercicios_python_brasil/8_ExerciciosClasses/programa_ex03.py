# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe 
# as medidades de um local. Depois, deve criar um objeto com as medidas e calcular
# a quantidade de pisos e de rodapés necessárias para o local.

from ex03 import Retangulo 

comprimento = float(input("Informe o comprimento do retangulo em metros: "))
largura = float(input("Informe a largura do retangulo em metros: "))

meu_objeto = Retangulo(comprimento, largura)


quantidade_pisos = meu_objeto.calcula_area()
quantidade_rodapes = meu_objeto.calcula_perimetro()

print(f"Quantidade de pisos necessários: {quantidade_pisos}")
print(f"Quantidade de rodapés necessários: {quantidade_rodapes}")