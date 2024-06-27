# DESAFIO 07

# Crie um programa que cria uma matriz de dimensão 3x3 e
# preencha com valores lidos pelo teclado.

# No final mostre a Matriz na tela, com a formatação correta.

#Versão 1
# matriz = [[0,0,0],[0,0,0],[0,0,0]]

# c = 0

# for i in matriz[0]:
#     numero = int(input(f"Digite um valor para [0, {c}]: "))

#     matriz[0][c] = numero
   
#     c +=1

# for i in matriz[1]:
#     if c == 3:
#         c = 0
#     numero = int(input(f"Digite um valor para [1, {c}]: "))
#     matriz[1][c] = numero  
#     c +=1

# for i in matriz[2]:
#     if c == 3:
#         c = 0
#     numero = int(input(f"Digite um valor para [2, {c}]: "))
#     matriz[2][c] = numero  
#     c +=1

# print(matriz[0])
# print(matriz[1])
# print(matriz[2])



#-------------------------------

#Versão 2

matriz = [[0,0,0],[0,0,0],[0,0,0]]
c = 0

for i in range (0,3): #i=1

    for j in matriz[i]: #
        if c == 3:
            c = 0
        numero = int(input(f"Digite um valor para [{i}, {c}]: "))

        matriz[i][c] = numero # matriz[1][0]  
       
        c +=1

print(matriz[0])
print(matriz[1])
print(matriz[2])