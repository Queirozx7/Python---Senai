# DESAFIO 02
# Crie um programa onde 4 jogadores joguem um dado e tenham resultado aleatórios. Guarde esses resultados em um dicionário . No final, coloque esse dicionário em ordem,
# sabendo que o vencedor tirou o maior numero no dado.

# import random
# jogador = {}
# numAleatorio = list()

# for j in range(0,1):
#     jogador["Nome"] = input(f'Digite o nome do {j+1}º jogador: ')
#     input("pressione ENTER para jogar o dado: ")   
#     numAleatorio.append(jogador.copy())
#     dado = random.randint(1,6)
#     jogador["Valor"] = dado
#     print(f"O dado caiu na posição {dado}.")
#     print("Proximo jogador em: \n3... \n2... \n1...")
#     print("-="*15)
    



import random
jogador = [{"Nome" : "Dado:"},
           {"Nome" : "Dado"},
           {"Nome" : "Dado:"},
           {"Nome" : "Dado:"},
           {"Nome" : "Dado:"}]
# jogador = {} #dicionario vazio

print(' ')
print('-='*60)

for i, j in jogador:
    jogador[0] = input(f"Digite o nome do {i+1}° jogador: ")
    jogador[1] = random.randint(1,6)#numero  que o dado caiu
    print(f"O dado de {jogador[0]}, caiu no valor {jogador[1]}  ")
    jogador.append
    print("=-"*30)

print (f"O Jogador: {i}, vençeu por tirar o maior número no dado")



