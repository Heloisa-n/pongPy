import pygame
import sys
import os

def caminhodoIcone(caminho):

    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, caminho)

# AGORA SIM: Carrega o ícone de forma "blindada"
icone_janela = pygame.image.load(caminhodoIcone("bola.ico"))

pygame.init()
# configurações:
    #tela:
tela = pygame.display.set_mode((400, 400))
    #Icone:
caminho_final = caminhodoIcone("bola.ico")
icone_janela = pygame.image.load(caminho_final)
pygame.display.set_icon(icone_janela)
    #título:
pygame.display.set_caption("PongPy")
    #geral:
tela_largura = tela.get_width()
tela_altura = tela.get_height()
clock = pygame.time.Clock()
rodando = True
dt = 0

