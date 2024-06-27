# DESAFIO 02

# Crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista.
#
# Caso o número já exista lá dentro, ele não será adicionado.
#
# No final serão exibidos todos os valores únicos digitados, em ordem
# crescente.

valores =[]

while True:
    numero= int(input("Digite um número entre 0 e 10000:  (Digite -1 se quiser sair) "))
    print(" ")
   
    if numero in valores:
        print("Número já cadastrado. Tente outro!")
    else:    
        valores.append(numero)
        print(valores)
   
    if numero== -1:
        print(" ")
        print("Saindo...")
        break
print(" ")
print("------------------------- ")
print("Lista completa")
print(valores)
print("Ordem crescente:")
valores.sort()
print(valores)