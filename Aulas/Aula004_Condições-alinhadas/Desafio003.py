# DESAFIO 03
# Crie um programa que leia duas notas entre 0 a 10 de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida.
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 a 6.9: RECUPERAÇÃO
# Média igual ou superior a 7.0: APROVADO


print ('***SIMULE SUA NOTA***')
resultado_1 = float(input('Qual a sua nota 1? '))
resultado_2 =float(input('Qual a sua nota 2? '))

media = (resultado_1 + resultado_2)/2

if media<5:
    print('Você foi reprovado!')
elif media<6.9 or media<=5:
    print('Esta de recuperacao!')
else:
    print('Aprovado!!!')
