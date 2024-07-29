#### JOGO DA COBRINHA ####

import pygame
from pygame.locals import *
from sys import exit
from random import randint
import time

pygame.init()

### Função REBOOT game 
larguratxt = 320
alturatxt = 240
def reboot_game():
    global pontos,x_Snake,y_Snake, lista_cabeca_Snake, lista_Snake, x_Maca, y_Maca, lost , velocidade, key_s, key_a, key_w, key_d
    x_Snake = largura/2
    y_Snake = largura/2
    lista_cabeca_Snake = []
    lista_Snake, x_Maca = []
    x_Maca = randint(40,600)
    y_Maca = randint(40,440)
    lost = False
    velocidade = 5
    key_s = key_a = key_w = False
    key_d = True

#Declaração de variáveis
largura = 640
altura = 480
tituloJanela = "Snake Game"

#informações Snake
x_Snake = largura/2 #"meio" da tela
y_Snake = altura/2 #"meio" da tela
width_Snake = height_Snake = 20
lista_Snake = list()

#Informações Maça
x_Maca = randint(40,600)
y_Maca = randint(40,440)
width_Maca = height_Maca = 20 #### 1º largura 2ºaltura

# informações pontuação
fonte = pygame.font.SysFont('MS Sans Serif', 25, True, False)
pontos = 0

#informações movimento
velocidade = 10
movimentoX = velocidade                              ## lado
movimentoY = 0                     ##cima + e baixo -

key_a = key_w = key_s = False
key_d = True
#informações 


tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption(tituloJanela) ### Colocar titulo na janela 

relogio = pygame.time.Clock()

while True:
    relogio.tick(20)  # padrao 60 - super rapido
    tela.fill((54,54,54))
    msg = f'Pontos: {pontos}'
    caixaTexto = fonte.render(msg, True, (220,220,220))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
            
        if event.type == KEYDOWN: ## QUANDO TECLA FOR CLICADA (INFORMAR QUAL A TECLA DEPOIS)
            if event.key == K_a and not(key_d):
                movimentoX = -velocidade
                movimentoY = 0
                key_w = key_s = key_d = False
                key_a = True      
                
            if event.key == K_d and not(key_a):
                movimentoX = velocidade
                movimentoY = 0
                key_a = key_s = key_w = False
                key_d = True
                
            if event.key == K_s and not(key_w):
                movimentoY = velocidade
                movimentoX = 0
                
                key_a = key_w = key_d = False
                key_s = True      
                          
            if event.key == K_w and not(key_s):
                movimentoY = - velocidade
                movimentoX = 0        
                key_a = key_s = key_d = False
                key_w = True
            
    x_Snake += movimentoX
    y_Snake += movimentoY
    
#Recebimento de teclas (comentado por só ativar se clicar)
    # if pygame.key.get_pressed() [K_LEFT]:
    #     x_Snake -= 10
    # elif pygame.key.get_pressed() [K_RIGHT]:
    #     x_Snake += 10
    # elif pygame.key.get_pressed() [K_UP]:
    #     y_Snake -= 10    
    # elif pygame.key.get_pressed() [K_DOWN]:
    #     y_Snake += 10
        
### Snake NÃO passar da tela     
    if x_Snake >= largura:
        x_Snake = 0
        
    elif x_Snake <= 0:
        x_Snake = largura
    
    if y_Snake >= altura:
        y_Snake = 0
        
    elif y_Snake <= 0:
        y_Snake = altura

### MAÇA E COBRA (retangulos - onde é exibido - cor - posição X e Y - largura e altura )    
    snake = pygame.draw.rect(tela,(0,255,255),(x_Snake, y_Snake , width_Snake, height_Snake))   
    maca  = pygame.draw.rect(tela,(255,69,0),(x_Maca,y_Maca,width_Maca,height_Maca))
    
### Colisão com a Maça:s
    if snake.colliderect(maca):
        x_Maca = randint(40,600)
        y_Maca = randint(40,480)
        pontos += 1  


    if len(lista_Snake) > pontos:
        del lista_Snake[0]
        
    lista_cabeca_Snake = list()
    lista_cabeca_Snake.append(x_Snake)
    lista_cabeca_Snake.append(y_Snake)
    
    
    lista_Snake.append(lista_cabeca_Snake)
    for XeY in lista_Snake:
        pygame.draw.rect(tela, (60,179,113), (XeY[0], XeY[1], width_Snake, height_Snake))
    
### Sistema de GAME OVER
    if lista_Snake.count(lista_cabeca_Snake) > 1:
        lost = True
        while lost:
            tela.fill((0,0,0))
            reboot = f'Parabéns voçê fez um total de {pontos} pontos. \nPara jogar novamente pressione a tecla R no seu teclado'
            textoreboot = fonte.render(reboot,True, (255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    lost = False
                    reboot_game()
            tela.blit(reboot,(320,240)) 
        pygame.display.update()
    
    tela.blit(caixaTexto, (500,40))
    tela.blit(reboot, (320,240))
    pygame.display.update()


    