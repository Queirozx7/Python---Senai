# DESAFIO 01
# Faça um programa que tenha uma função chamada área(), que
# receba as dimensões de um terreno retangular (largura e
# comprimento) e mostre a área do terreno.

print('-='*15)
print('CONTROLE DE TERRENO')
print('-='*15)


def area(l,c):
    # calc =  largura*comprimento 
    return largura*comprimento 

largura = float(input('Digite a largura(m) : '))
comprimento = float(input('Digite o comprimento(m): '))

print(f"A área de um terreno {largura}x{comprimento} é de {area(largura,comprimento)}²")