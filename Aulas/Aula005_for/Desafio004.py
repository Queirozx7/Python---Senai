# DESAFIO 04
# Refaça o DESAFIO 09, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

# TABUADA (0,5)

num = int(input('Digite um Numero: '))
inicio = int(input('Digite um Numero de INICIO: '))
fim= int(input('Digite um Numero de FIM: '))
fim=fim+1

for i in range(inicio,fim):
     print(f'{num} X {i} = {num*i}')
    
print('===========================================')
print('===== Fim ! =====')
