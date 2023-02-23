#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

pais_a= int(input('Informe o número da população: '))
pais_b= int(input('Informe o número da população: '))
tx_pais_a = float(input('Informe a taxa da população: '))
tx_pais_b = float(input('Informe a taxa da população: '))

ano = 0
while not (pais_a >= pais_b):
    pais_a = round(pais_a * tx_pais_a + pais_a)
    pais_b = round(pais_b * tx_pais_b + pais_b)
    ano = ano + 1

print(f'''
A população do País A de {pais_a} habitantes
ultrapassou o País B de {pais_b} habitantes
após {ano} anos.
''')