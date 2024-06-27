# DESAFIO 01
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

while True:

    nova = []
    maior=menor=0

    

    print("=-"*30)
    # O MAIOR DIGITADO + POSIÇÃO

    for i in range(0,5):
        fiveNum = int(input(f'Digite po {i+1}° Número: '))
        print(f'Voçê digitou os seguintes numeros: {nova}')
        #0, 1, 2, 3, 4, 5, 6    
        
    else:
        stop = input('Deseja parar? (s/n)')
        stop.upper()
        if stop == 'S':
                # break
            print('=============Tank You !==============')