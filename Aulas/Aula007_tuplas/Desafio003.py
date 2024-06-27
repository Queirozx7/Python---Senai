# DESAFIO 003

# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro Serie B de Futebol, na ordem de colocação. Depois mostre:

# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time do Santos.


serieB = ('AMÉRICA-MG','GOIÁS','MIRASSOL','AVAÍ','SANTOS','SPORT','CEARÁ','OPERÁRIO','CORITIBA',
          'VILA NOVA','NOVOROZONTINO','AMAZONAS','CHAPECOENSE','PONTE PRETA','CRB','PAYSANDU','BOTAFOGO','ITUANO','BRUSQUE','GUARANI')

cincoPri = serieB[:5]
quatroUlti = serieB[16:20]

print('================================================')
print(f'Os cincos primeiros são: {cincoPri}')
print('')

print('================================================')
print(f'Os 4 ultimos são: {quatroUlti}')
print('')

print('===============================================================================')
myLista = list(serieB)
ord_lista = sorted(serieB)
print(ord_lista)
print('')

print('===============================================================================')
colocação = ord_lista.index('SANTOS')
print(f'O time Santos está na {colocação+1} posição ! ')
print('')