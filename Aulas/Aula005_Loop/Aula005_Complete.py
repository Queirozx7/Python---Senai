# SINTAXE DO COMANDO (FOR)
# o comando FOR normalmente é ultilizado quandovoce quer repetir um bloco de código um numero fixo de vezes

#comando

# for contador in range(1,6): #sempre para 1 a menos 
#     print(contador)#1 
    
# #contador= contador +1
# #contador++    
# print("Fim")

# for contador in range(0,6,2):
#     print(contador)
# print("Fim")

#CONTA DE TABUADA
numero = int(input('Digite um número: '))
for i in range(0,11):
    #numero = int(input('Digite um número: '))
    print(f'{numero} X {i} = {numero*i}')

#CONTA DE SUBTRAÇÃO
menos = int(input('Digite um número para subtrair 10 vezes: '))
for i in range(0,11):
    #menos = int(input('Digite um número para subtrair 10 vezes: '))
    print(f'{menos} - {i} = {menos-i}')