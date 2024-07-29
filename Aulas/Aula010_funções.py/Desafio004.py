# Faça co que seu programa seja uma calculadora, separando as operações matemáticas em funções.

# Versão (1.0) Utilizando funções

import time

def soma(n1,n2):
    print('A soma dos valores é: ')
    for i in range(1,fim+1):
        print(f'{n1}+{n2} = {n1+n2}')
        # parar()

def multiplicação(n1,n2,fim):
    print('A multiplicação dos valores é: ')
    for i in range(1,fim+1):
        print(f'{n1}x{n2} = {n1*i}')
        # parar()
def chamadamulti(): # arrumar isso (contem erros)
    global n1
    global n2
    global fim
    n1 = int(input('Digite 1° número que deseja realizar a multiplicação: '))
    n2 = int(input(f'Digite 2º número que deseja realizar a multiplicação ({n1}x??): '))
    fim = int(input('Digite em que número termina multiplicação (0 a 1000): '))
    multiplicação(n1,n2)
        

def subtração(n1,n2):
    print('A subtração dos valores é: ')
    for i in range(1,fim+1):
        print(f'{n1}-{i} = {n1-n2}')
        # parar()

def divisão(n1,n2):
    print('A divisão dos valores é: ')
    for i in range(1,fim+1):
        print(f'{n1}/{i} = {n1/n2}')
        # parar()

print('-='*16)

while True:
    print('OLÁ MUNDO, ESSA É A CALCULADORA')
    print('-='*16)
    
    #coletagem de dados
    operacao = int(input('Digite a operação desejada: \n0 - PARA SAIR \n1 - Soma \n2 - Multiplicação \n3 - Subtração \n4 - Divisão  \nDigite o numero de acordo com a opção desejada: '))
    time.sleep(1)
   
    # 2
    # fim = int(input('Digite em qual numero deseja que a conta Termine: '))
    # time.sleep(1)
        
    # def parar():
    #     parar = str(input('Deseja ir novamente? (s/n)'))
    #     parar.upper()
    #     if parar == 'S':
    #         print('Iniciando...')
    #         time.sleep(1)
    #     else:
    #         parar == 'N'
    #         print('Voçê desejou sair !')
    #         time.sleep(1)
    #         operacao = 0

    
    # fazer os if e relacionalos com as funções que seram usadas 
    if operacao == 0:
        print('Voçê desejou sair...')
        time.sleep(1)
        break

    if operacao == 1:
        print('*lembre-se de colocar na ordem desejada*')
        soma(n1,n2)
        print('-='*16)

    elif operacao == 2:
        chamadamulti()
        print('*lembre-se de colocar na ordem desejada*')
        print('-='*16)

    elif operacao == 3:
        print('*lembre-se de colocar na ordem desejada*')
        subtração(n1,n2)
        print('-='*16)

    elif operacao == 4:
        print('*lembre-se de colocar na ordem desejada*')
        divisão(n1,n2)
        print('-='*16)

    else:
        operacao != 1, 2, 3, 4
        print('Opção inválida, tente novamente ! ')
        time.sleep(0,5)
        continue