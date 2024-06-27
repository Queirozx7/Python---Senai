# DESAFIO 05
# Faça um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Um listagem com as pessoas mais leves


nome =[]
peso=[]

while True:
    id_usuario= (input('Digite o nome da pessoa:')),int(input('Digite o peso da pessoa:'))
    inserir= int(input('Caso deseje sair digite 1, para adicionar mais pessoas digite qualquer numero: '))
    nome.append(id_usuario[0])
    peso.append(id_usuario[1])
    if inserir ==1:
        break
    else:
        continue
leves= []
pesados=[]
print(nome)
print(peso)
print(len(nome))
media_pesos = sum(peso)/len(peso)
print(round(media_pesos,2))

for i in range(len(nome)):
    if peso[i] > media_pesos:
        pesados.append((nome[i]))
    else:
        leves.append((nome[i]))

# Exibindo os resultados
print(f'Nomes das pessoas: {nome}')
print(f'Pesos das pessoas: {peso}')
print(f'Total de pessoas: {len(nome)}')

print(f'As pessoas leves da lista são: {leves}')
print(f'As pessoas pesadas da lista são: {pesados}')
