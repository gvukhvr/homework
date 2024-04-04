# Imports
import pygame
import sys
from pygame.locals import *
import random
import time

# Initialzing 
pygame.init()

# Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 770
SPEED = 5
SCORE_ENEMY = 0
SCORE_COIN = 0

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = pygame.image.load('game-over.png')
game_over = pygame.transform.scale(game_over, (800, 770))

background = pygame.image.load('road.png')
background = pygame.transform.scale(background, (800, 770))
DISPLAYSURF = pygame.display.set_mode((800, 770))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Class for Enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.original_image = pygame.image.load("car1.png")
        self.image = pygame.transform.scale(self.original_image, (95, 230))  
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(150, SCREEN_WIDTH-160), 0)  

    # Method to move the enemy
    def move(self):
        global SCORE_ENEMY
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE_ENEMY += 1
            self.rect.top = 0
            self.rect.center = (random.randint(150, SCREEN_WIDTH - 160), 0)

# Class for Coin
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.original_image = pygame.image.load("coin1.png")
        self.image = pygame.transform.scale(self.original_image, (70, 70))  
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(150, SCREEN_WIDTH-160), 0)  

    # Method to move the coin
    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(150, SCREEN_WIDTH - 160), 0)


class Coin2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.original_image = pygame.image.load("coin2.png")
        self.image = pygame.transform.scale(self.original_image, (70, 70))  
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(150, SCREEN_WIDTH-160), 0)  

    # Method to move the coin
    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(150, SCREEN_WIDTH - 160), 0)



# Class for Player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.original_image = pygame.image.load("player11.png")
        self.image = pygame.transform.scale(self.original_image, (150, 170)) 
        self.rect = self.image.get_rect()
        self.rect.center = (350, 680)
        
    # Method to move the player
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 110:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH-110:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()
C2 = Coin2()

# Creating Sprites Groups
enemies_group = pygame.sprite.Group()
enemies_group.add(E1)
coins_group = pygame.sprite.Group()
coins_group.add(C1)
coins_group.add(C2)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(C2)

# Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game Loop
while True:
       
    # Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0,0))
    
    # Render and display scores
    score_enemy_text = font_small.render("Cars: " + str(SCORE_ENEMY), True, BLACK)
    score_coin_text = font_small.render("Coins: " + str(SCORE_COIN), True, BLACK)
    DISPLAYSURF.blit(score_enemy_text, (10, 10))
    DISPLAYSURF.blit(score_coin_text, (10, 30))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies_group):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
                    
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(game_over, (0,0))
           
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Check for collision between Player and Coins
    for coin in coins_group:
        if pygame.sprite.collide_rect(P1, coin):
            pygame.mixer.Sound('coin-sound.wav').play()
            if isinstance(coin, Coin2):
                SCORE_COIN += 2  # If it's the second type of coin, add 2 to the score
            else:
                SCORE_COIN += 1  # If it's the first type of coin, add 1 to the score
            coin.kill()  # Remove the collected coin

                
    pygame.display.update()
    FramePerSec.tick(FPS)
