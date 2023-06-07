import pygame
import winsound
import random

pygame.init()
tamanho = (800,600)
branco = (255,255,255)
preto = (0,0,0)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
running = True
posicaoXBolinha = 0
posicaoYBolinha = 300
velocidadeBolinha = 1
direita = True
while running:  
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.escape:
            running = False

    tela.fill(branco)
    pygame.draw.circle(tela, preto, (posicaoXBolinha, posicaoYBolinha), 30)

    if posicaoXBolinha >=800:
        direita = False
        velocidadeBolinha = velocidadeBolinha +1
        posicaoYBolinha = ramdom.randint (0,600)
        winsound.Beep(500,300)
    elif posicaoXBolinha <=0:
        direita = True
        velocidadeBolinha = velocidadeBolinha +1
        winsound.Beep(500,300)
    if direita == True:
        posicaoXBolinha = posicaoXBolinha + velocidadeBolinha
    else:
        posicaoXBolinha = posicaoXBolinha - velocidadeBolinha
    
    posicaoXBolinha = posicaoXBolinha + 1
    pygame.draw.line(tela, preto, (30,30), (100,30), 5)


    pygame.display.update()
    clock.tick(60)
pygame.quit()