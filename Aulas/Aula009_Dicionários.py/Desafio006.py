# DESAFIO 06
# Crie um programa onde o usuário possa digitar sete valores
# numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e impares. No final mostre os
# valores pares e impares e ordem crescente.

valores = [[],[]]

for val in range (7):
    val= int(input(f'Digite o {val+1}° numero: '))

    if val%2 ==0:
        valores[0].append(val)
    else:
        valores[1].append(val)

valores.sort()
valores[0].sort()
valores[1].sort()
print(f' Esses são os impares{valores[1]}')
print(f'Esses são os pares {valores[0]}')
print(f'EM ordem crescente {valores}')
