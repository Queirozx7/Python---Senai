# DESAFIO 05
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar desconsidere-o.

while True:
     print('Some somente de números PARES')
     soma = 0
     cont = 0
     for i in range(1,7):
          numeros = int(input(f'Digite o {i}º Valor: '))
          if numeros % 2 == 0: 
               soma += numeros
               cont += 1
     print(f'Você informou {cont} números PARES e a soma foi de: {soma}')
     print('')
     loop = input('Deseja parar? (s/n)')
     if loop.lower() == 's':
          print('=====Obrigado por jogar 😁👍=====')
          break