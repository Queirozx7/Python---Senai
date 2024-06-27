# DESAFIO 01
# Escreva um programa que peça ao usuário para digitar dois
# números e divida o primeiro número pelo segundo. Certifique-se
# de lidar com a possibilidade de divisão por zero.

while True:
    try:
        num1 = int(input('Digite o 1º número (-1 para sair): '))
        num2 = int(input('Digite o 2º número (-1 para sair): '))
        resultado = num1 / num2
        
    except ZeroDivisionError:
        print('Não pode ser dividido por 0 (Zero)')

    if num1 or num2 < 0 :
        print('Voçê desejou sair...')
        break
    else:
        print(resultado)