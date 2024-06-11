# # A confederação Nacional de Natação precisa de uma programa que leia o ano de nascimento de uma atleta e mostre sua categoria, de acordo com a idade.
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 24 anos: SÊNIOR
# Acima: MASTER

print(' Veja em qual categoria de ATLETA você está! ')
idade = int(input("Informe a idade do atleta: "))
# mirim = idade<=14
# infantil = idade>9 and idade<=14
# junior = idade>14 and idade<=19
# senior = idade>19 and idade<=24
# acima = idade>24 and idade==24

if idade>=1 and idade<=9:
    print(f'O atleta se encontra na categoria MIRIM')
    
if idade>9 and idade<=14:
        print(f'O atleta se encontra na categoria INFANTIL')
        
if idade>14 and idade<=19:
        print('O atleta se encontra na categoria JUNIOR')   
             
if  idade>19 and idade<=24:
    print(f'O atleta se encontra na categoria SÊNIOR')
        
if idade>24:
    print('O atleta se encontra na categoria MASTER')
        
elif idade<=0:
    print('o Atleta ainda não se encontra em NENHUMA categoria!')