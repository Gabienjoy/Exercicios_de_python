# Classe Bola: Crie uma classe que modele uma bola:
# Atributos: Cor, circunferência, material
# Métodos: trocaCor e mostraCor

class Bola:

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor
        return cor

    def mostraCor(self):
        return f'A bola é da cor {self.cor}'


cor = input(str('Informe a cor desejada: '))

minha_bola= Bola(cor, material= 'plastico', circunferencia='redondo')

mudanca_de_cor = minha_bola.trocaCor(cor)

print(f"A cor da bola agora é: {mudanca_de_cor}")


