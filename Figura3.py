import pygame
pygame.init()
tamanho = (800,600)
branco = (255,255,255)
preto = (0,0,0)
tela = pygame.display.set_mode(tamanho)

running = True
while running:  
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.escape:
            running = False

    tela.fill(branco)
    pygame.draw.line(tela, preto, (50,50), (700,50), 2)
    pygame.draw.line(tela, preto, (50,50), (400,500), 2)
    pygame.draw.line(tela, preto, (400,500), (700,50), 2)


    pygame.display.update()
pygame.quit()