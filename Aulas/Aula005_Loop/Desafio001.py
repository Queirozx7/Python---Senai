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

