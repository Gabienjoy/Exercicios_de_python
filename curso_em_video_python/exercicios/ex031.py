# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Digite a distancia da viagem: '))

if distancia <= 200:
    preço = 0.5 * distancia
    print(
        f'A viagem é de até 200Km, então o valor da passagem vai ser R${preço:.2f}!')
elif distancia > 200:
    preço = 0.45 * distancia
    print(
        f'A viagem ultrapassa 200Km, então o valor da passagem vai ser R${preço:.2f}!')
