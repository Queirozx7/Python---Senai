# def  função_local():
#     variavel_local = 10
#     print(variavel_local)
    
# função_local()
# # print(variavel_local)


# #### transformando variavel me global

# variavel_global = 5

# def funcao_locate():
# #     global variavel_global #GLOBAL para informar que quero uma variavel de fora {variavel que desejo}
# #     variavel_global += 10 #py nao aceita usar na mesma linha que foi chamado a variavel GLOBAL  
# # print(funcao_locate())

# def tabuada(numero,fim):
#     print(f'Tabuada do {numero}: ')
#     for i in range(1,fim+1):
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





# def somar(a,b):
#     resultado = a+b
#     return resultado
#     #ou
#     #direto """"return a+b"""""

# result = somar(5,2) # =7
# print(f'A soma foi de {result}')
# print(f'A soma foi de' somar(5,6)) # faz a soma direta sem precisar de uma variavél 




# criando uma funcao com o empacotamento de dados
# def contador (*num ):
#     print(num)
    
# #chamando a função com os parametros

# contador(1,2,3)
# contador(1,3)
# contador(1,5,6,7)
