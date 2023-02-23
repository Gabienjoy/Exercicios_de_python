# Classe Quadrado: Crie uma classe que modele um quadrado:
# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:

    def __init__(self, lado):
        self.lado = lado

    def muda_valor_do_lado(self, novo_lado):
        self.lado = novo_lado
        return f'O novo valor do lado é {self.lado}'

    def retorna_valor_do_lado(self):
        return f'O valor do lado é {self.lado}'

    def calcula_area(self):
        area = self.lado * self.lado
        return f'O valor da area é {area}'


primeiro_input = int(input('Informe o valor do lado: '))
meu_quadrado = Quadrado(primeiro_input)

while meu_quadrado.lado != 0:
    print(meu_quadrado.retorna_valor_do_lado())
    print(meu_quadrado.calcula_area())
    segundo_input= int(input('Informe o valor do novo lado: '))

    print(meu_quadrado.muda_valor_do_lado(segundo_input))
    
    






