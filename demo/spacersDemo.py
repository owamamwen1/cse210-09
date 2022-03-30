import wave
from matplotlib import path
import pygame
import pathlib
import time
import random
pygame.font.init()
pygame.mixer.init()

# WINDOW
WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spacer DEMO")

# SHIP DIMENSIONS
SHIP_WIDTH, SHIP_HEIGHT = 90, 43
ENEMY_WIDTH, ENEMY_HEIGHT = 85, 85

# LOAD IMAGES
## Characters
HERO = pygame.transform.scale(pygame.transform.rotate(pygame.image.load(pathlib.Path(__file__).parent / 'hero.png'), -90), (SHIP_WIDTH, SHIP_HEIGHT))
ENEMY_1 = pygame.transform.scale(pygame.image.load(pathlib.Path(__file__).parent / 'enemy1.png'), (ENEMY_WIDTH, ENEMY_HEIGHT))
ENEMY_2 = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(pathlib.Path(__file__).parent / 'enemy2.png'), ((ENEMY_WIDTH, ENEMY_HEIGHT))), 90)
## Lasers
HERO_LASER = pygame.transform.scale(pygame.image.load(pathlib.Path(__file__).parent / 'heroLaser.png'),(SHIP_WIDTH * 0.8, SHIP_HEIGHT))
E1_LASER = pygame.transform.scale(pygame.image.load(pathlib.Path(__file__).parent / 'enemy1Laser.png'),(ENEMY_WIDTH , ENEMY_HEIGHT* 0.4))
E2_LASER = pygame.transform.scale(pygame.image.load(pathlib.Path(__file__).parent / 'enemy2Laser.png'),(ENEMY_WIDTH , ENEMY_HEIGHT* 0.6))
## BACKGROUND
BG = pygame.image.load(pathlib.Path(__file__).parent / 'background.png')

#AUDIO
HERO_AUDIO = pygame.mixer.Sound(pathlib.Path(__file__).parent / 'doublelaser.mp3')
E1_AUDIO = pygame.mixer.Sound(pathlib.Path(__file__).parent / 'vortex.mp3')
E2_AUDIO = pygame.mixer.Sound(pathlib.Path(__file__).parent / 'heavylaser.mp3')


# FONT
main_font = pygame.font.SysFont('impact', 40)
lost_font = pygame.font.SysFont('garamond', 140)

# COLORS
WHITE = 255, 255, 255

# GAME VARIABLES
FPS = 60
MAX_ENEMIES = 35
player_vel = 8
enemy_vel = 2
hero_laser_vel = 17
enemy_laser_vel = 3
health = 100

# CLASSES and Modules
class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.x += vel
    
    def on_screen(self, width):
        return self.x >= 0 and self.x <= WIDTH

    def hit(self, obj): 
        return collide(self, obj)

def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

class Ship():
    COOLDOWN = FPS / 2 
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down = 0 
        
    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def cooldown(self):
        if self.cool_down >= self.COOLDOWN:
            self.cool_down = 0
        elif self.cool_down > 0:
            self.cool_down += 1
    
    def fire(self):
        if self.cool_down == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down = 1
            self.audio.play()
    
    def move_laser(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.on_screen(WIDTH) == False:
                self.lasers.remove(laser)
            elif laser.hit(obj):
                obj.health -= 10
                self.lasers.remove(laser)

class Hero(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = HERO
        self.laser_img = HERO_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        self.lasers = []
        self.audio = HERO_AUDIO 

    def move_laser(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.on_screen(WIDTH) == False:
                self.lasers.remove(laser)
            else: 
                for obj in objs:
                    if laser.hit(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                              self.lasers.remove(laser)
    
class Enemy1(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = ENEMY_1
        self.laser_img = E1_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        self.audio = E1_AUDIO
    
    def move(self, vel):
        self.x -= vel

class Enemy2(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = ENEMY_2
        self.laser_img = E2_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        self.audio = E2_AUDIO


    def move(self, vel):
        self.x -= vel
    



#-------------------------------Main------------------------------------#
def main():
    run = True
    
    clock = pygame.time.Clock()
    hero = Hero(50,250)
    enemies = []
    wave_length = 1
    level = 0
    lives = 5
    lost= False

    while run:
        clock.tick(FPS)
        
        for enemy in enemies:
            if enemy.x < -50:
                enemies.remove(enemy)

        if lives <= 0:
            lost = True

        if len(enemies) == 0:
                level += 1
                
                for i in range(wave_length):

                    enemy1 = Enemy1(random.randrange(WIDTH+100, 1500), random.randrange(55, HEIGHT - ENEMY_HEIGHT))
                    enemy2 = Enemy2(random.randrange(WIDTH+100, 1500), random.randrange(55, HEIGHT - ENEMY_HEIGHT))
                    enemies.append(enemy1)
                    enemies.append(enemy2)

                if len(enemies) <= MAX_ENEMIES:
                    wave_length += 1
        
        def redraw_window():
            
            #draw background
            WIN.blit(BG, (0, 0))
            #draw labels
            
            level_label = main_font.render(f"Level: {level}", 1, WHITE)
            
            WIN.blit(level_label, (WIDTH//2 - level_label.get_width()//2, 10 ))
            
            #draw enemies
            for enemy in enemies:
                enemy.draw(WIN)
            
            #draw hero ship
            hero.draw(WIN)

            if lost:
                lost_banner = lost_font.render("GAME OVER", 1, WHITE)
                WIN.blit(lost_banner, WIDTH//2 - lost_banner.get_width()//2, HEIGHT//2)
                
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for enemy in enemies:
                        
            enemy.move(enemy_vel)
            enemy.move_laser(-enemy_laser_vel, hero)
            
            if random.randrange(0, FPS * 6 ) == 1:
                enemy.fire()
            elif collide(enemy, hero):
                hero.health -= 10
                enemies.remove(enemy)
                   

           

        hero.move_laser(hero_laser_vel, enemies)

        #key input for HERO
        keys = pygame.key.get_pressed()

        ##laser
        if keys[pygame.K_SPACE]:
            hero.fire()
        ## key pressed and restraints
        if keys[pygame.K_UP] and hero.y > 45: #move up
            hero.y -= player_vel
        if keys[pygame.K_DOWN] and hero.y + player_vel + 50 < HEIGHT : #move down
            hero.y += player_vel
        if keys[pygame.K_LEFT] and hero.x > 0: #move left
            hero.x -= player_vel//2
        if keys[pygame.K_RIGHT] and hero.x < WIDTH//3.5: #move right
            hero.x += player_vel//2    
        

        redraw_window()


main()

