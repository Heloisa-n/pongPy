import pygame
import config

class Barras(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        # barra:
            # tamanho:
        self.image = pygame.Surface((20, 130))
            #cor:
        self.image.fill((0, 0, 0)) #preto
        
            # colisão:
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        
        # 3. Vetor para movimento suave (opcional, mas recomendado)
        self.pos = pygame.Vector2(x, y)
     
    def fica_na_tela(self):
        if(self.rect.y < 50):
            self.rect.y = 50
            
        if(self.rect.y >= 265):
            self.rect.y = 265

class TextoNaTela(pygame.sprite.Sprite):
    def __init__(self,tamanhoFonte):
        super().__init__()
        pygame.font.init()
        self.fonte = pygame.font.SysFont("Arial", tamanhoFonte, bold=True)
        self.fonte_esc = pygame.font.SysFont("Arial", 13, bold=True)
        self.placar = 0
    
    def orientacao(self):
        texto = self.fonte.render(("Tecle ESPAÇO ou ENTER para começar."),True,(0,0,0))
        texto_pausa = self.fonte_esc.render(("Tecle ESC para PAUSAR."),True,(0,0,0))
        config.tela.blit(texto, (50, 250))
        config.tela.blit(texto_pausa, (120, 280))

    def pontuacao(self):
        texto = self.fonte.render(("Pontos: " + str(self.placar)),True,(0,0,0))
        config.tela.blit(texto, (130, 10))

textoPontos = TextoNaTela(30)
textoOrientacao = TextoNaTela(16)

barra_esquerda = Barras(10, 100)
barra_direita = Barras(config.tela_largura - 30, 100)

grupo_barra_esquerda = pygame.sprite.Group(barra_esquerda)
grupo_barra_direita = pygame.sprite.Group(barra_direita)

#funçoes:

def versusComputador(barraEsquerdaDireita,y_bola,barra_velocidade,x_bola,bola_velocidade_x,bola,lado):

    if abs(barraEsquerdaDireita.rect.centery - y_bola) > barra_velocidade:# desce a barra junto com a bola
        if barraEsquerdaDireita.rect.centery < y_bola: 
            barraEsquerdaDireita.rect.y += barra_velocidade
        else:
            barraEsquerdaDireita.rect.y -= barra_velocidade

        #colisôes:
    if barraEsquerdaDireita.rect.colliderect(bola):
        if lado == "esquerda":
            bola_velocidade_x = abs(bola_velocidade_x) + 0.1 # Vai para a direita
            x_bola = barraEsquerdaDireita.rect.right + 20 
        else: # Lado direita
            bola_velocidade_x = -abs(bola_velocidade_x) - 0.1 # Vai para a esquerda
            x_bola = barraEsquerdaDireita.rect.left - 20 

    return x_bola,bola_velocidade_x


