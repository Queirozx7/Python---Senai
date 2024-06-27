# DESAFIO 002
# Crie um programa que vai gerar CINCO NUMEROS ALEATÓRIOS e colocar em uma TUPLA.
# Depois o MENOR e o MAIOR valor que estão na TUPLA

import random

num_program = random.randint(0,6)

minha_lista = []
minha_tupla = minha_lista+num_program
print(minha_tupla)



#PROFESSOR FEZ (PRIMEIRA FORMA)

maior = 0
menor = 0

for i in range(1,6):
    num_program = random.randint(1,5)
    minha_lista.append(num_program)
    
print(minha_lista)

maior = max(minha_lista)
menor = min(minha_lista)
minha_tupla = tuple(minha_lista)

print(f'MAIOR = {maior}')
print(f'MENOR = {menor}')
print(minha_tupla)
