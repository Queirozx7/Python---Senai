# DESAFIO 03
# Faça um programa que tenha uma função chamada maior(), que receba três parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


def maior():
    max(lista)
    print(f"o maior valor é {max(lista)} ! ")
    
lista = list()    

for i in range(0,3):
    num = int(input(f"Digite o {i+1} valor: "))
    lista.append(num)

print(f'Entre os valores {lista}... ')
print('')
maior()


# """" max() """" pega o maior valor de uma variavel ou lista/tuplas