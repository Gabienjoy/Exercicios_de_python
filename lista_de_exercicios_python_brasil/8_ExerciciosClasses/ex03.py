# Classe Retangulo: Crie uma classe que modele um retangulo:
# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe 
# as medidades de um local. Depois, deve criar um objeto com as medidas e calcular
# a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:

    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def muda_valor_dos_lados(self, novo_comprimento, nova_largura):
        self.comprimento = novo_comprimento
        self.largura = nova_largura

    def retorna_valor_dos_lados(self):
        return f'O valor do comprimento é {self.comprimento} e o valor da largura é {self.largura}'

    def calcula_area(self):
        area = self.comprimento * self.largura
        return area 

    def calcula_perimetro(self):
        perimetro = 2 * (self.comprimento + self.largura) 
        return perimetro 