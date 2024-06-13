# Aprendendo a usar 'if e 'else' 
# Bloco de codigo
   
nota = float(input("Digite sua Media: ")) 
   
if nota>=5: #F
   print(f"Voce foi Aprovado, Parabens !")
        
else: 
   print(f"Retido, infelizmente não foi dessa vez.")
print ("Fim")

# DESAFIO 002
 
Velo = float(input("Quando Km/h voce passou no radar? ")) 

if Velo >80:
    acima = Velo-80
    multa = acima*7
    print(f'Ramelou, vai levar multa pra casa no valor de R${multa}. Boa Sorte!')
    print('fim')
else: 
   print("Ufaa! Voce nao foi multado, continue assim!")
 
 
# DESAFIO 003
    
dkm = float(input('Qual foi a distancia percorrida em Km/h:'))
if dkm <=200:
    print(f'o percurso percorrico fica no total de R$ {dkm*0.50}')
else: 
    print(f'ao passar de 200(Km/h) o percurso percorrico fica no total de R$ {dkm*0.45}')


# DESAFIO 004

import random

print("JOGO DO ADIVINHE O NUMERO")
numUser = int(input("Digite um número entre de 0 a 5: "))
numCompute = random.randint(0,5)
print(f'Número escolhido pelo Computador:{numCompute}')
if numUser==numCompute:
    print('Amassou cria, derrotou a MAQUINA !')
else:
    print('A maquina DERROTOU você!!')


# DESAFIO 005 (MAIS FACÍL)

# Media escola
# Aprovado se  media maior ou igual a 7
# faltas até 10


media = float(input('Qual foi o valor da média'))
if media>6:
    print('Você foi Aprovado, parabens! ')
else: 
    if media<3:
        print('Infelizmente não tem mais jeito, você foi Reprovado.')
    else:
        print('Ainda tem chance! Você está de Recuperação')



# DESAFIO 005 (MAIS DIFICÍL)

media = float(input('Qual foi o valor da média '))
if media>6:
    print('Você foi Aprovado, parabens! ')
elif media<3:
    print('Infelizmente não tem mais jeito, você foi Reprovado.')
else:    
    print('Ainda tem chance! Você está de Recuperação')
