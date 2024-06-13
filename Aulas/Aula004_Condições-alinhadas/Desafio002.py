# # ESCREVA UM PROGRAMA QUE LEIA DOIS NUMEROS INTEIROS E COMPARE-OS, MOSTRANDO NA TELA UMA MENSAGEM:
# O primeiro valor é maior
# o Segundo valor é maior
# Não existe valor maior, ambos são iguais.

num1 = int(input('Digite o PRIMEIRO valor: '))
num2 = int(input('Digite o SEGUNDO valor: '))

if num1>num2:
    print(f'O PRIMEIRO valor maior é {num1}')
if num2>num1:
    print(f'O SEGUNDO valor é maior {num2}')
else:
    print('Não existe valor maior, ambos são iguais! ')