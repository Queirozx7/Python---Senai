# Faça co que seu programa seja uma calculadora, separando as operações matemáticas em funções.

### Versão (0.5) Somente tabuada
# def tabuada(numero,fim):
#     print(f'Tabuada do {numero}: ')
#      for i in range(1,fim+1):
#         resultado = numero * i 
#         print(f'{numero} x {i} = {resultado}')
        
        

# def dados():
#     print('Olá {nome}, seja bem vindo! ')

# nome = str(input('Digite o seu nome: '))
# numero = int(input('Digite o Numero que deseja multiplicar: '))
# fim = int(input('Digite o limite da tabuada: '))

# #chamando as funções 
# dados(nome)
# tabuada(numero,fim)






# Versão (1.0) Utilizando funções

# import math


# n1Soma  = 0
# n2Tabuada = 0 
# n3Divisão = 0
# n4Subutracao = 0


# def operações(ini,fim,num1,num2):
#     operacao = int(input('Digite qual operação deseja realizar \n 1 - Soma \n 2 - Tabuada \n 3 - Subtração \n 4 - Divisão \n Digite (1 a 4): '))
    
#     #soma
# def soma():
#     for i in range(ini,fim):
#         soma = num1 + num2
#         return soma
    
#     # #tabuada       
#     # elif operacao == 2:
#     #     for i in range(inicio,fim):
#     #         return num1*num2
            
            
#    

# #função
# soma()

# inicio = int(input('Digite em qual numero deseja que a conta começe: '))
# 







import time

def soma(n1,n2):
    for i in range(1,fim):
        print(f'a Soma dos valores {n1}, {n2}. Deu um total de: {n1+n2}')

def multiplicação(n1,n2,fim):
    for i in range(1,fim):
        print(f'a Multiplicação dos valores {n1}, {n2}. Deu um total de: {n1*n2}')
        

def subtração(n1,n2):
    for i in range(1,fim):
        print(f'a Subtração dos valores {n1}, {n2}. Deu um total de: {n1-n2}')

def divisão(n1,n2):
    for i in range(1,fim):
        print(f'a Divisão dos valores {n1}, {n2}. Deu um total de: {n1/n2}')




n1 = int(input('Digite o 1º numero: '))
n2 = int(input('Digite o 2º numero: '))
fim = int(input('Digite em qual numero deseja que a conta Termine: '))
operacao = int(input('Digite a oção desejada: \n1 - Soma \n2 - Multiplicação \n3 - Subtração \n4 - Divisão \nDigite o numero de acordo com a opção desejada: '))

    
op = {
    "4" : "divisao()",
    "3" : "subtração()",
    "2" : "multiplicação()",
    "1" : "soma()"
}

# fazer os if e relacionalos com as funções que seram usadas 