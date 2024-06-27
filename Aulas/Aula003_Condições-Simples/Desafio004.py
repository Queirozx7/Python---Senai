# faça um programa que leia três numeros e mostre qual é o maior e o menor.

num1 = float(input('Qual é o primeiro numero? '))
num2 = float(input('Qual é o segundo numero? '))
num3 = float(input('Qual é o terceiro numero? '))

# #Versão 2.0
num1= int(input("Digite o PRIMEIRO numero: "))
num2= int(input("Digite o SEGUNDO numero: "))
num3= int(input("Digite o TERCEIRO numero: "))

#maior?
if num1>num2 and num1>num3:
    print(f"Primeiro é Maior = {num1}")
elif num2>num3:
    print(f"Segundo é Maior = {num2}")
else:
    print(f" Terceiro é Maior = {num3}")
#menor?    
if num1<num2 and num1<num3:
    print(f"Primeiro é Menor = {num1}")
elif num2<num3:
    print(f"Segundo é Menor = {num2}")
else:
    print(f" Terceiro é Menor = {num3}")