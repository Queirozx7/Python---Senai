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
    
    
    
#=========================INICIANDO LOOP================================

# TABUADA (0,5)

# num = int(input('Digite um Numero: '))
# inicio = int(input('Digite um Numero de INICIO: '))
# fim= int(input('Digite um Numero de FIM: '))
# fim=fim+1

# for i in range(inicio,fim):
#     print(f'{num} X {i} = {num*i}')
    
# print('')
# print('===== Fim ! =====')

# DESAFIO 001 (SLIDE)

#Somando números do intervalo informado limitando o maior numero 
inicio = int(input('Informe o primeiro número: '))
fim = int(input('Informe o número final: '))
salto = int(input('Informe o salto: '))
texto = "Cálculo: "
soma = 0
for numero in range(inicio , fim , salto):
    soma = soma + numero
    texto = texto + str(numero)
    if numero > 50:
        texto = texto + "n\ passou de 50"
        break
    if numero != fim-1:
        texto = texto + " + "
print(f'{texto}')
print(f'Soma: {soma}')


# FORMA EXPLICADA NA AULA (TELA)

