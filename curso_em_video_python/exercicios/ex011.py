largura = float(input('Digite a largura da sua parede: '))
altura = float(input('Digite a altura da sua parede: '))

# 1 lata de tinta pinta 2 metros
area = largura*altura
litros_necessarios = area/2

print(
    f"Sua parede tem {area} m²\nE você precisa de {litros_necessarios} latas de tinta para pinta-la")
