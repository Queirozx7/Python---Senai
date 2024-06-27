# DESAFIO 4

import random

print("JOGO DO ADIVINHE O NUMERO")
numUser = int(input("Digite um número entre de 0 a 5: "))
numCompute = random.randint(0,5)
print(f'Número escolhido pelo Computador:{numCompute}')
if numUser==numCompute:
    print('Amassou cria, derrotou a MAQUINA !')
else:
    print('Ta osso em... Perdeu!!')