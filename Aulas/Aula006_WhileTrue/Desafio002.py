# DESAFIO 02
# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre
# quantos números foram digitados e qual foi a soma entre eles (desconsiderando o 999).

while True:
    numbers = int(input('=====Digite um numero: '))
    somaNum = ['999']
    print('')
    for i in range(numbers,somaNum):
    if numbers == somaNum:
            print('Parábens voce venceu ! ')
            print(f'Soma de todos os numeros jogados {somaNum-999}')
    else:
        print('Você errou, tente mais uma vez !')
    
    resposta = input('Deseja parar de jogar? (s/n):')
    if resposta.lower() == 's':
        print('Obrigado pelo game! .')
    break