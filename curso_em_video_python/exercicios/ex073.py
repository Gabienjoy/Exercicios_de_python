# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em que posição está o time da Chapecoense.

times = 'Palmeiras', 'Internacional', 'Flamengo', 'Fluminense', 'Corinthians', 'Atletico-PR',  'Atletico-MG', 'América MG', 'Fortaleza', 'Botafogo', 'Santos', 'São Paulo', 'Bragantino', 'Goias', 'Coritiba', 'Ceará SC', 'Cuiabá', 'Atletico GO', 'Avai', 'Juventude'

print(f'Os 5 primeiros times foram {times[0:5]}\n')

print(f'Os últimos 4 colocados foram: {times[-4:]}\n')

print(f'Times em ordem alfabética: {sorted(times)}\n')

print(
    f'A posição está o time do Flamengo: {times.index("Flamengo") +1}ª Posição\n')
