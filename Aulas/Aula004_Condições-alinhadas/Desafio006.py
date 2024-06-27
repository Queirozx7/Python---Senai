# DESAFIO 06
# Crie um programa que faça o computador jogar Jokenpô com
# você.
print('')
print("===== Jogue Jokenpô comigo! =====")
import random

op_jogador = int(input("Digite sua escolha: \n1-Pedra \n2-papel \n3-Tesoura \nDigite sua escolha: "))
# op_jogador = op_jogador.upper()
# print(f"Você escolheu {op_jogador} !") #opção jogador

if op_jogador ==1:
    tx_jogador="PEDRA🧱"
if op_jogador ==2:
    tx_jogador="PAPEL🧻"
if op_jogador ==3:
    tx_jogador="TESOURA✂"
   
print(f"Você escolheu {tx_jogador} !")
opcoes = ["PEDRA🧱","PAPEL🧻","TESOURA✂"]
numero_randomico = random.choice(opcoes)

#print(opcoes)#random.choice(opcoes)
#print(opcoes[1])#PAPEL
 
op_computador = numero_randomico

#VITORIA
if ((tx_jogador=="PEDRA🧱" and op_computador=="TESOURA✂")or
    (tx_jogador=="TESOURA✂" and op_computador=="PAPEL🧻")or
    (tx_jogador=="PAPEL🧻" and op_computador=="PEDRA🧱")
):
    print("Ufa, voçê VENCEU ! 😁👍")

#DERROTA
elif ( 
    (tx_jogador=="PEDRA🧱" and op_computador=="PAPEL🧻")or
    (tx_jogador=="TESOURA✂" and op_computador=="PEDRA🧱")or
    (tx_jogador=="PAPEL🧻" and op_computador=="TESOURA✂")
): 
    print(" YOUR LOSER - MELHORE ! 🤣 ")
#EMPATE
else:
    print("Eita, parece que EMPATOU 👀")
        
print('')
print('FIM')