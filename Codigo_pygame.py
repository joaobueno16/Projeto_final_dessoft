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

WIDTH = 380 # Largura da tela
HEIGHT = 600 # Altura da tela
FPS = 60 # F

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)




class Player(pygame.sprite.Sprite):

    def __init__(self, player_img):
        #construtor e coletar imagem 
        pygame.sprite.Sprite.__init__(self)    
        self.image = player_img 
        self.image = pygame.transform.scale(player_img, (45, 45))   
        self.image.set_colorkey(BLACK)   
        self.rect = self.image.get_rect()
            
        #posicoes
        self.rect.y = HEIGHT/2
        self.rect.x = (WIDTH/2)-30
        #raio
       

        self.speedx = 0 

        self.speedy = 0
       
    def update(self):
        self.rect.y += self.speedy 
        if self.rect.y <= 0:
            self.rect.y = 0
            self.speedy = 0 
        if self.speedy > 2:
            self.speedy = 2
        self.rect.x += self.speedx 
        if self.rect.x <= 0:
            self.rect.x = 0
            self.speedx = 0
        if self.speedy > 2:
            self.speedy = 2
        if self.speedx > 2:
            self.speedx = 2
            


class Tela_de_fundo(pygame.sprite.Sprite): 

   def __init__(self,base,x,y):

       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.transform.scale(base,(1,150))
       self.image.set_colorkey(BLACK)
       self.rect = self.image.get_rect()

       # posicao 
       self.rect.x = x
       self.rect.y = y

       #velocidade
       self.speedx = 0
       self.speedy = -4.5 

   def update(self):
       self.rect.y += self.speedy 
       
class Carros_aleatorios(pygame.sprite.Sprite):

   def __init__(self, Carros_aleatorios,x):

       pygame.sprite.Sprite.__init__(self)

       #define a largura aleatoria do cano
       aleatorio = random.randint(100,350)

       self.image = pygame.transform.scale(Carros_aleatorios, (80, 600))       
       self.image.set_colorkey(BLACK)
       self.rect = self.image.get_rect()

       #poscicoes 
       self.rect.top =  aleatorio
       self.rect.x = x

       self.speedx = 0
       self.speedy = -4.5



   #def update(self):
   def update(self):
       self.rect.y += self.speedy 
       if self.speedy > -4.5:
           self.speedy = -4.5

      
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
       