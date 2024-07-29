# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

# Condições Necessárias:

# a + b > c
# a + c > b
# b + c > a
# 
linha1 = float(input("escolha o tamanho de uma linha: "))
linha2 = float(input("escolha o tamanho de uma linha: "))
linha3 = float(input("escolha o tamanho de uma linha: "))
if (linha1 + linha2) > linha3 and (linha1 + linha3) > linha2 and (linha3 + linha2) > linha1:
    print("é possivel fazer um triangulo ⨹")
else:
    print("nao é possivel fazer um triangulo 🤔")