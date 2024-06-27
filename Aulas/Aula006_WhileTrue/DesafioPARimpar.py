# JOGO PAR OU IMPAR

import random
import time

while True:

    num_jogador = int(input('Escolha um entre ZERO a DEZ (0 a 10): '))
    if num_jogador<0 or num_jogador>10:
        print('')
        print("Opção INVÁLIDA")
        print('Vamos recomeçar !')
        continue
    num_compute = random.randint(0,10)
    op_jogador = int(input('>>>Escolha entre \n1-IMPAR \n2-PAR \n Digite sua escolha (1 ou 2):  '))
    print('')
    if op_jogador<1 or op_jogador>2:
        print('')
        print("Opção INVÁLIDA")
        print('Vamos recomeçar !')
        continue

    print(f'Você escolheu: {op_jogador} ')
    print(f'Seu oponente escolheu: {num_compute} ')
    print(f'Você escolheu: {num_jogador} ')
    total = num_jogador + num_compute

    par = total%2==0 #retorna um VERDADEIRO ou FALSO
    # print(f"é par? {par}")
    vitoria = 0
    print("")
    print("Vamos ver quem GANHOU !")
    print("Loanding...")
    time.sleep(1)
    print("Loanding...")
    time.sleep(1)
    print("Loanding...")
    time.sleep(1)

    print('')
    
    if op_jogador==1:
        print(f"Você escolheu IMPAR ")
        if par:
            print("Voçê perdeu ! ")
            break
        else:
            print('Voçê Ganhou ! ')
            vitoria+=1
    elif op_jogador==2:
        print('Você escolheu PAR ')
        if par:
            print("Voçê GANHOU ! ")
            vitoria+=1
        else:
            print('Voçê PERDEU ! ')
            break
        
    else:
        print('Opção Inválida, tente novamente ! ')
print (f'Voçê ganhou {vitoria} vezes consecutivas parabéns ! ')
