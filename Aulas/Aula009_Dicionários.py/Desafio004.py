# DESAFIO 04

# Crie um programa que gerencie o aproveitamento de um
# jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de
# gols feitos em cada partida. No final, tudo isso será guardado
# em um dicionário, incluindo o total de gols feitos durante o
# campeonato.


#versão 0,5 (Lucas Queiroz)
nome_jogador = str(input('Digite seu nome: '))
qnt_partidas = int(input('Quantas partidas jogou: '))
total_gols = 0
meu_dicionario = {
    'Nome' : nome_jogador,
    'Partidas' : qnt_partidas,
    'Gols' : total_gols 
}


for qnt_partidas in range(meu_dicionario['Partidas']):
    gols = int(input(f'Quantos gols o jogador {nome_jogador} fez na {qnt_partidas+1}º partida: '))
    total_gols += gols
meu_dicionario['Gols'] = total_gols
print('-='*30)
print(meu_dicionario)
print('-='*30)
print(f'O jogador {meu_dicionario["Nome"]}, jogou {meu_dicionario["Partidas"]} partidas e marcou {meu_dicionario["Gols"]} no total. ')



# Versão 1.0 (Professor fez)


listaGols = []

jogador = {
    'Nome do Jogador' : str(input("Nome do Jorgador: "))
}

quantidadePartidas = int(input(f"Quantas partidas {jogador['Nome do Jogador']} jogou: "))

for i in range (0, quantidadePartidas):
    quantidadeGols = int(input(f"Digite a quantidade de gols feitos ma partida {i+1}: "))
    listaGols.append(quantidadeGols)

jogador['gols'] = listaGols
jogador['total'] = sum(listaGols)

for k,v in jogador.items():
    print(f"O campo {k} , tem o valor {v}")

print(f"O jogador {jogador['Nome do Jogador']} jogou {len(jogador['gols'])} partidas")

for i, v in enumerate(jogador['gols']):
    print(f"Na partida {i+1}, fez {v} gols")    
print(f"Tendo um total de {jogador['total']}")