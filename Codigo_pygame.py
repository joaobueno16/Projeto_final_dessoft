
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:51:07 2019
@author: joaoluizleaobueno
"""

import pygame
import random
from os import path

# diretorios de imagem e som
img_dir = path.join(path.dirname(__file__), 'img_dir')
snd_dir = path.join(path.dirname(__file__), 'snd_dir')

# Dados gerais do jogo.
WIDTH = 440  # Largura da tela
HEIGHT = 540  # Altura da tela
FPS = 30  # Frames por segundo

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pos_car_ini = [70, 190, 350]


class Player(pygame.sprite.Sprite):

    def __init__(self):
        # construtor da classe pai (Sprite)
        pygame.sprite.Sprite.__init__(self)

        # Carregando imagem de fundo
        player_img = pygame.image.load(path.join(img_dir, "Player.png")).convert()

        self.image = player_img
        # self.image.set_colorkey(BLACK)

        # Diminuindo o tamanho da imagem
        self.image = pygame.transform.scale(player_img, (1333 // 25, 2400 // 25))

        # Deixando transparente
        # self.image.set_colorkey(BLACK)

        # Detalhes do posicionamento
        self.rect = self.image.get_rect()

        # Centraliza no baixo da tela
        self.rect.centerx = int(WIDTH / 2)
        self.rect.bottom = HEIGHT - 40

        # Velocidade do carro
        self.speedx = 4
        self.speedy = 0

    # Metodo que atualiza a posição do carro
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Mantem dentro da tela
        if self.rect.right > WIDTH - 30:
            self.rect.right = WIDTH - 30
        if self.rect.left < 30:
            self.rect.left = 30
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0


# Classe Mob que representa os meteoros
class Mob(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self):
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Carregando a imagem de fundo.
        mob_img = pygame.image.load(path.join(img_dir, "carro_verde.png")).convert()

        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(mob_img, (1333 // 25, 2400 // 25))
        # self.image.set_colorkey(BLACK)
        self.rotate = pygame.transform.rotate(mob_img, -180)

        # Deixando transparente.
        # self.image.set_colorkey(BLACK)

        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Sorteia um lugar inicial em x
        self.rect.x = pos_car_ini[random.randint(0, 2)]
        # Sorteia um lugar inicial em y
        self.rect.y = random.randrange(-640, -70)
        # Sorteia uma velocidade inicial

        self.speedy = 15

    # Metodo que atualiza a posição dos carros aleatorios
    def update(self):
        self.rect.y += self.speedy

        # Se o carro passar do final da tela, volta para cima
        if self.rect.top > HEIGHT + 10:
            self.rect.x = pos_car_ini[random.randint(0, 2)]
            self.rect.y = random.randrange(-150, -30)
            
        

            # self.speedy = random.randrange(2, 9)
    #def collide(self , groupcollide):
        
            
            
        

class Pista(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        background = pygame.image.load(path.join(img_dir, 'pista.png')).convert()
        self.image = pygame.transform.scale(background, (WIDTH, HEIGHT))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

        # posicao
        self.rect.x = x
        self.rect.y = y

        # velocidade
        self.speedx = 0
        self.speedy = 30

    def update(self):
        self.rect.y += self.speedy

        # Se a pista sair de cima da tela, volta para cima
        if self.rect.y > HEIGHT:
            self.rect.y = 0 - HEIGHT + 30


class Telainicial(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        inicio_img = pygame.image.load(path.join(img_dir, "start.png")).convert()
        self.image = pygame.transform.scale(inicio_img, (440, 540))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

        # posicao
        self.rect.x = x
        self.rect.y = y

        self.speedy = 0

    def update(self):
        self.speedy += 0


# Carrega todos os assets uma vez só.
def load_assets(img_dir, snd_dir):
    assets = {}
    assets["musica_jogo"] = pygame.mixer.Sound(path.join(snd_dir, 'pew.wav'))
    return assets


# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Carrega todos os assets uma vez só e guarda em um dicionário
assets = load_assets(img_dir, snd_dir)
# Carrega os sons do jogo
pygame.mixer.music.load(path.join(snd_dir, '8_Bit_Universe_-_ACDC_Back_In_Black_8_bit_(dj4u.io).mp3'))
pygame.mixer.music.set_volume(0.4)
# music_sound = assets["musica_jogo"]

# Loop principal.
pygame.mixer.music.play(loops=-1)

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Carros")

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()

# Cria um grupo só da pista
pista = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

pista1 = Pista(0, 0)
all_sprites.add(pista1)
pista.add(pista1)

# Carrega o  segundo fundo do jogo
pista2 = Pista(0, 0 - HEIGHT)
all_sprites.add(pista2)
pista.add(pista2)

# Cria uma nave. O construtor será chamado automaticamente.
player = Player()

# Cria um grupo de todos os sprites e adiciona o player.
class_player = pygame.sprite.Group()
class_player.add(player)
all_sprites.add(player)

# Carrega o fundo do jogo

# background_rect=background.get_rect()

# Cria um grupo só dos carros aleatorios
mobs = pygame.sprite.Group()

# Cria 8 carros aleatorios e adiciona no grupo carros aleatorios
for i in range(5):
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)




# Comando para evitar travamentos.

try:
    
    

    running = True
    state = 2

    player.speedy = 0
    player.speedx = 0
    inicial = Telainicial(0, 0)
    telainicial = pygame.sprite.Group()
    telainicial.add(inicial)
    telainicial.draw(screen)
    telainicial.update()
    pygame.display.flip()
    m.speedy = 0

    clock.tick(FPS)

    while running:
        for amob in mobs:
                mobs.remove(amob)
                hit2=pygame.sprite.spritecollide(amob, mobs, False)
                mobs.add(amob)
                if len(hit2)>0:
                    amob.kill()
        if len(mobs)<6:

           novo_mob = Mob()        
           mobs.add(novo_mob)
           all_sprites.add(novo_mob)
                    
                    
                
                

        clock.tick(FPS)

        if state == 1:
            
            

            hit = pygame.sprite.groupcollide(mobs, class_player, False, False)
            if len(hit) != 0:
                pygame.quit()

            # Depois de processar os eventos.
            # Atualiza a acao de cada sprite.
            all_sprites.update()

            # A cada loop, redesenha o fundo e os sprites
            screen.fill(BLACK)
            # screen.blit(background, background_rect)
            all_sprites.draw(screen)

            # Depois de desenhar tudo, inverte o display.
            pygame.display.flip()

            # Processa os eventos (mouse, teclado, botão, etc).
            for event in pygame.event.get():

                # Verifica se foi fechado.
                if event.type == pygame.QUIT:
                    running = False
                    # Dependendo da tecla, altera a velocidade.
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.speedx = -8
                    if event.key == pygame.K_RIGHT:
                        player.speedx = 8
                    if event.key == pygame.K_UP:
                        player.speedy = -8
                    if event.key == pygame.K_DOWN:
                        player.speedy = 8

                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key == pygame.K_LEFT:
                        player.speedx = 0
                    if event.key == pygame.K_RIGHT:
                        player.speedx = 0
                    if event.key == pygame.K_UP:
                        player.speedy = 0
                    if event.key == pygame.K_DOWN:
                        player.speedy = 0

        if state == 2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    running = False
                if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        state = 1
                        del telainicial
finally:
    pygame.quit()
