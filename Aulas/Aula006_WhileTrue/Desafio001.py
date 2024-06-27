# DESAFIO 01
# Faça um jogo, onde o computador vai “pensar” em um número entre 0 a 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
while True:

    print("JOGO DO ADIVINHE O NUMERO")
    numUser = int(input("Digite um número entre de 0 a 10: "))
    qnt_tentativa = numUser
    numCompute = random.randint(0,10)


    for i in range(qnt_tentativa==numCompute):
        if numUser==numCompute:
            print(f'Número escolhido pelo Computador:{numCompute}')
        print('Amassou cria, derrotou a MAQUINA !')  
    else:
        print('Ta osso em... Perdeu!!')
        print(f'Número escolhido pelo Computador:{numCompute}')
    print(f'Foi necessário palpites para você vencer !')

    print('')
    resposta = input('Deseja jogar novamente? (s/n):')
    if resposta.lower() == 's':
            print('Obrigado pelo game! .')
    break