# (Utilizando pygame)
import pygame
from pygame.locals import *
from sys import exit
import random
import time

pygame.init()

#Declaração de variáveis
largura = 640
altura = 480
tituloJanela = "One game py"

#informações retângulo
pos_x_rect = 10
pos_y_rect = 20
width_rect = 100
heigth_rect = 40


#informações circle
pos_x_circle = 500
pos_y_circle = 200
raio_circle = 15
rgb_circle = (102,190,255)

#caixa de texto 
fonte = pygame.font.SysFont("Arial", 40, True, False)
pontos = 0
#texto de perdeu - reboot 
# usei a mesma fonte de cima


tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption(tituloJanela)
relogio = pygame.time.Clock()

while True:
    tela.fill((0,0,0))
    relogio.tick(30)
    msg = f"Pontos: {pontos}"   
    caixa_texto = fonte.render(msg,False, (255,255,255))   
    
    for event in pygame.event.get(): #monitora cliques no mouse e teclado
        if event.type == QUIT:
            pygame.quit()
            exit()
        # if event.type == KEYDOWN:
            # if event.key == K_a:
            #     pos_x_rect -= 50
            # if event.key == K_d:
            #     pos_x_rect += 50
            # if event.key == K_s:
            #     pos_y_rect += 50
            # if event.key == K_w:
            #     pos_y_rect -= 50
            
#Criando um retângulo
    retangulo = pygame.draw.rect(tela,(205,240,190), (pos_x_rect,pos_y_rect,width_rect,heigth_rect))
    if pygame.key.get_pressed()[K_a]:
        pos_x_rect -= 20
    elif pygame.key.get_pressed()[K_d]:
        pos_x_rect += 20
    elif pygame.key.get_pressed()[K_s]:
        pos_y_rect += 20
    elif pygame.key.get_pressed()[K_w]:
        pos_y_rect -= 20
        
#nao passar da tela    
    if pos_x_rect >= largura:
        pos_x_rect = 0
        
    elif pos_x_rect <= 0:
        pos_x_rect = largura
    
    
    if pos_y_rect >= altura:
        pos_y_rect = 0
        
    elif pos_y_rect <= 0:
        pos_y_rect = altura
    
    
#Criando um circulo
    circulo = pygame.draw.circle(tela,(rgb_circle),(pos_x_circle,pos_y_circle), raio_circle)
    if pygame.key.get_pressed()[K_LEFT]:
        pos_x_circle -= 20
    if pygame.key.get_pressed()[K_RIGHT]:
        pos_x_circle += 20
    if pygame.key.get_pressed()[K_DOWN]:
        pos_y_circle += 20
    if pygame.key.get_pressed()[K_UP]:
        pos_y_circle -= 20
    
    if pos_x_circle >= largura:
        pos_x_circle = 0
        
    elif pos_x_circle <= 0:
        pos_x_circle = largura
    
    
    if pos_y_circle >= altura:
        pos_y_circle = 0
        
    elif pos_y_circle <= 0:
        pos_y_circle = altura
    
#colisão .................
    if circulo.colliderect(retangulo):
        pos_x_rect = random.randint(20,altura)
        pos_y_rect = random.randint(20,largura)
        pontos += 1
        
    tela.blit(caixa_texto, (400,40)) #caixa de texto apareceu na tela (400,40 é a posição na TELA)
    pygame.display.update()
    
    
