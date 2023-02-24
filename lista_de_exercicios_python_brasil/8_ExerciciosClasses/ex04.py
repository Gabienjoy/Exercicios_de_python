# Classe Pessoa: Crie uma classe que modele uma pessoa:
# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer. 
# Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:

    def __init__(self,nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhercer(self, nova_idade):
        if self.idade < 21:
            self.idade = nova_idade
            self.altura = self.altura + 0.5
            return self.idade , self.altura
        else:
            self.idade = nova_idade
            return self.idade
        
    def engordar(self, peso_engordou):
        self.peso = peso_engordou
        return self.peso

    def emagrecer(self, peso_emagreceu):
        self.peso = peso_emagreceu
        return self.peso

    def crescer(self, altura_cresceu):
        self.altura = altura_cresceu
        return self.altura
