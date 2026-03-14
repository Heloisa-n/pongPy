import pygame
import config
import classes

pontos = "0"
barra_velocidade = 5

x_bola = config.tela_largura //2
y_bola = config.tela_altura //2
raio_bola = 20
bola_movendo = False
maquinaXMaquina =True

bola_velocidade = 2
bola_velocidade_x = bola_velocidade
bola_velocidade_y = bola_velocidade

while config.rodando:

    config.dt = config.clock.tick(60) / 1000
    teclas = pygame.key.get_pressed()
        #background:
    config.tela.fill("white")
    
    # EVENTOS:
        # SAIR PELO X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            config.rodando = False

    #SE A BOLA NÃO ESTIVER MOVENDO OU GAME OVER:
    if bola_movendo == False:
        #reset:
            #velocidade:
        bola_velocidade_x = 2
        bola_velocidade_y = 2
            #bola pro meio da tela:
        x_bola = config.tela_largura / 2
        y_bola = config.tela_altura / 2
            #pontuação:
        classes.textoPontos.placar = 0
            #Texto de orientação:
        classes.textoOrientacao.orientacao()
            #barras centralizadas
        classes.barra_esquerda.rect.topleft = (10, 100)
        classes.barra_direita.rect.topleft = (config.tela_largura - 30, 100)

    #PÔE NA TELA:
        #pontuação do jogo:
    if maquinaXMaquina == False:
        classes.textoPontos.pontuacao()
        #desenha a bola na tela:
    bola = pygame.draw.circle(config.tela, "red",(x_bola, y_bola), raio_bola ) # 20 é o raio da bola
        #barras:
    classes.grupo_barra_esquerda.draw(config.tela)
    classes.grupo_barra_direita.draw(config.tela)

    # BOLA:
        #"SE A BOLA ESTA SE MOVENDO, ENTÃO...:"
    if bola_movendo:
        x_bola += bola_velocidade_x
        y_bola += bola_velocidade_y

            #BORDAS:
                #COLISÃO COM A BORDA VERTICAIS (QUICA):
        if y_bola <= 60 or y_bola >= 380: # 20 + 50 raio da bola + área do texto
            
            bola_velocidade_y *= -1

                # COLISÃO COM A BORDA HORIZONTAL(PERDE):
        if x_bola <= 20 or x_bola >= 400:

            bola_movendo = False

            classes.barra_esquerda.rect.topleft = (10, 100)
            classes.barra_direita.rect.topleft = (config.tela_largura - 30, 100)
    
    # BARRA DO JOGADOR:    

    #BARRA DO COMPUADOR:
    if maquinaXMaquina:
        bola_movendo = True
        #texto de orientação:
        classes.textoOrientacao.orientacao()
            # Lógica da barra ESQUERDA: 
        if (x_bola <= 200 ): #0 a 200 = lado esquerdo
            x_bola, bola_velocidade_x = classes.versusComputador(classes.barra_esquerda,y_bola,barra_velocidade,x_bola,bola_velocidade_x,bola,"esquerda")
            # Lógica da barra DIREITA:
        if (x_bola >= 200):
            x_bola, bola_velocidade_x = classes.versusComputador(classes.barra_direita,y_bola,barra_velocidade,x_bola,bola_velocidade_x,bola,"direita")
            
    else:
        if (x_bola >= 200):
            x_bola, bola_velocidade_x = classes.versusComputador(classes.barra_direita,y_bola,barra_velocidade,x_bola,bola_velocidade_x,bola,"direita")
            #colisôes:
        if classes.barra_esquerda.rect.colliderect(bola):
        
            classes.textoPontos.placar += 1

            bola_velocidade_x = abs(bola_velocidade_x) + 0.1 #(positivo = direira)
            x_bola = classes.barra_esquerda.rect.right + 20 

        #TECLAS:
        if teclas[pygame.K_UP] or teclas[pygame.K_w]:
            classes.barra_esquerda.rect.y -= barra_velocidade
        if teclas[pygame.K_DOWN] or teclas[pygame.K_s]:
            classes.barra_esquerda.rect.y += barra_velocidade
        
    #TECLAS:
    if teclas[pygame.K_RETURN] or teclas[pygame.K_SPACE]:
        maquinaXMaquina= False
    if teclas[pygame.K_ESCAPE]:
        maquinaXMaquina = True
    
    classes.barra_esquerda.fica_na_tela()
    classes.barra_direita.fica_na_tela()

    pygame.display.flip()

pygame.quit()