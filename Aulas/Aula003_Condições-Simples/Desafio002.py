# DESAFIO 2
 
Velo = float(input("Quando Km/h voce passou no radar? ")) 

if Velo >80:
    acima = Velo-80
    multa = acima*7
    print(f'Ramelou, vai levar multa pra casa no valor de R$ {multa}. Boa Sorte!')
    print('fim')
else: 
    print("Ufaa! Voce nao foi multado, continue assim!")