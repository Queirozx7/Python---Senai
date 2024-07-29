# DESAFIO 05
# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso
# de mostrar que tipo de triângulo será formado:

# Equilátero: Todos os lados iguais
# Isósceles: Dois lados iguais
# Escaleno: Todos os lados diferentes

print ('***************QUAL TIPO DE TRIANGULO?********************')
A= float(input('Digite o comprimento da aresta a: '))
B= float(input('Digite o comprimento da aresta b: '))
C= float(input('Digite o comprimento da aresta c: '))

if A+B>C and A+C>B and B+C>A:
    print('Pode ser triangulo!')
    if A == B == C:
        print('Triângulo Equilátero: todos os lados iguais')
    elif A == B or A == C or B == C:
        print('Triângulo Isósceles: dois lados iguais')
    else:
        print('Triângulo Escaleno: todos os lados diferentes')
else:
    print('Não é possível formar um triângulo!')
 


