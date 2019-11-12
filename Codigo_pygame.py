#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:51:07 2019

@author: joaoluizleaobueno
"""

import pygame
import random
from os import path


#diretorios de imagem e som
img_dir = path.join(path.dirname(__file__), 'sprites')

#Dados gerais do jogo.
WIDTH = 440 # Largura da tela
HEIGHT = 540 # Altura da tela
FPS = 60 # Frames por segundo

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)




class Player(pygame.sprite.Sprite):

    def __init__(self):
        #construtor da classe pai (Sprite)
        pygame.sprite.Sprite.__init__(self)

        #Carregando imagem de fundo
        player_img = pygame.image.load(path.join(img_dir, "Player.png")).convert()  
        
        self.image = player_img

        #Diminuindo o tamanho da imagem 
        self.image = pygame.transform.scale(player_img, (1333//25, 2400//25))

        #Deixando transparente   
        self.image.set_colorkey(BLACK)

        #Detalhes do posicionamento   
        self.rect = self.image.get_rect()

        #Centraliza no baixo da tela
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 40

        #Variavel road_speed
        #self.road_speed = road_speed

        # Velocidade do carro
        self.speedx = 0
        #self.speedy = self.road_speed

    def update(self):
        self.rect.x += self.speedx
        self.rect.bottom += self.speedy
    
        
        #Deixa dentro da tela
        if self.rect.right > WIDTH - 55:
            self.rect.right = WIDTH - 55
            
        if self.rect.left < 55:
            self.rect.left = 55
            
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        
        if self.rect.top < 0:
            self.rect.top = 0


    # Metodo que atualiza a posição do carro
    def update(self):
        self.rect.x += self.speedx
        
        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Carros")

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()

# Carrega o fundo do jogo
background = pygame.image.load(path.join(img_dir, 'pista.png')).convert()
background_rect = background.get_rect()

#Cria o carro O construtor será chamado automaticamente.
player = Player()

# Cria um grupo de sprites e adiciona o carro.
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Classe Mob que representa os carros
class Mob(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        mob_img = pygame.image.load(path.join(img_dir, "carro_verde.png")).convert()
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(mob_img, (1333//25, 2400//25))
        
        # Deixando transparente.
        self.image.set_colorkey(BLACK)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        #Centraliza no baixo da tela 
        self.rect.centerx = random.randint(70 , WIDTH-70)
        
        self.rect.bottom = random.randint(-2000, -500)
        
        #self.road_speed = road_speed
        
    def update(self):
        #self.rect.bottom += self.road_speed + 3
        
        if self.rect.top >= HEIGHT:
            #Faz com que spawn longe da tela para controlar melhor a quantidade de spawn
            self.rect.bottom = random.randint(-2000, -500)
        '''
        # Sorteia um lugar inicial em x
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        # Sorteia um lugar inicial em y
        self.rect.y = random.randrange(-100, -40)
        # Sorteia uma velocidade inicial
        self.speedx = random.randrange(-3, 3)
        self.speedy = random.randrange(2, 9)
        '''
    # Metodo que atualiza a posição do carro
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        # Se o carro passar do final da tela, volta para cima
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedx = random.randrange(-3, 3)
            self.speedy = random.randrange(2, 9)



# Cria um grupo só dos meteoros
mobs = pygame.sprite.Group()

# Cria 8 meteoros e adiciona no grupo meteoros
for i in range(3):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
 
# Comando para evitar travamentos.
try:
    
    # Loop principal.
    running = True
    while running:
        
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                running = False
            
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    player.speedx = -8
                if event.key == pygame.K_RIGHT:
                    player.speedx = 8
                    
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    player.speedx = 0
                if event.key == pygame.K_RIGHT:
                    player.speedx = 0
                    
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite.
        #all_sprites.update()
            
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        
finally:
    pygame.quit()

            
'''   
def load_assets(img_dir):
   assets = {}
   assets["Player"] = pygame.image.load(path.join(img_dir, "Player.png")).convert_alpha()
   assets["Carro_aleatorio"] = pygame.image.load(path.join(img_dir, "carro_azul.png")).convert_alpha()
   assets['background1'] = pygame.image.load(path.join(img_dir, "Tela_de_fundo.png")).convert_alpha()
   

  
   return assets      
       
     
def game_screen(screen):


    assets = load_assets(img_dir)
    
    clock = pygame.time.Clock()
    
    #cria o background
    background = assets["background1"]
    background = pygame.transform.scale(background,(WIDTH,HEIGHT+20))
    background_rect = background.get_rect() 

    #criando grupos de sprites
    all_sprites = pygame.sprite.Group()
    classeplayer = pygame.sprite.Group()
    
    #cria o carro
    player = Player(assets["Player"])
    all_sprites.add(player)
    classeplayer.add(player)

    #cria os Carros_aleatorios
    carros_aleatorios = pygame.sprite.Group()
    
    
    #Canodecima1
    Carro_aleatorio1 = Carros_aleatorios(assets['Carro_aleatorio'], (WIDTH/2)+250)
    all_sprites.add(Carro_aleatorio1)
    carros_aleatorios.add(Carro_aleatorio1)
    #Canodebaixo1 
    Carro_aleatorio2 = Carros_aleatorios(assets['Carro_aleatorio'], (WIDTH/2)+250)
    all_sprites.add(Carro_aleatorio2)
    carros_aleatorios.add(Carro_aleatorio2)
    #Canodecima2
    Carro_aleatorio3 = Carros_aleatorios(assets['Carro_aleatorio'], (WIDTH/2)+550)
    all_sprites.add(Carro_aleatorio3)
    carros_aleatorios.add(Carro_aleatorio3)
    
    #estados
    PLAYING = 0
    DONE = 1
    INICIO = 2
    GAME_OVER = 3 
    state = INICIO
    
    
    telainicial = pygame.sprite.Group()
    
    
    while state != DONE:
       
       clock.tick(FPS)
         
       
    
# Inicialização do Pygame
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption("Benga_das_bengas")


try:
   game_screen(screen)
finally:
   pygame.quit()
'''
       
       