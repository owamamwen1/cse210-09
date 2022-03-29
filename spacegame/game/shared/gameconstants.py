import pathlib 
import pygame
from game.shared.color import Color
# import Path

FRAME_RATE = 50
MAX_X = 800
MAX_Y = 600
FONT_SIZE = 20
PLAYER_SIZE = 15
CENTER = "center"
COLS = 60
ROWS = 40
CAPTION = "Space Game"
WHITE = Color(255, 255, 255)

SHIP_X = 75
SHIP_Y = 75
SHIP_ROTATE = 270 #Ship rotation in degrees

SHIP_BULLET_X = 35
SHIP_BULLET_Y = 35


ENEMY_MAX_COUNT = 3

ENEMY_X = 80
ENEMY_Y = 80

ENEMY_VEL = 1  # Enemy velocity

ENEMY_BULLET_X = 35
ENEMY_BULLET_Y = 35

# IMAGE LOADERS
ACTOR_IMAGE = pygame.transform.rotate(
    pygame.transform.scale(
        pygame.image.load(pathlib.Path(__file__).parent.parent / "assets/images/actor.png"),
         (SHIP_X, SHIP_Y)), SHIP_ROTATE)

ENEMY_IMAGE = pygame.transform.scale(
    pygame.image.load(pathlib.Path(__file__).parent.parent / "assets/images/enemy.png"),
        (ENEMY_X, ENEMY_BULLET_Y))

BACKGROUND_IMAGE = pathlib.Path(__file__).parent.parent / "assets/images/background.png"
LOGO_IMAGE = pathlib.Path(__file__).parent.parent / "assets/images/logo.png"
BULLET_IMAGE = pygame.transform.scale(pygame.image.load(
    pathlib.Path(__file__).parent.parent / "assets/images/bullet.png"),
        (SHIP_BULLET_X, SHIP_BULLET_Y))

BULLET_ENEMY_IMAGE = pathlib.Path(__file__).parent.parent / "assets/images/bullet_enemy.png"

# Sounds for the game
ACTOR_SOUND = pathlib.Path(__file__).parent.parent / "assets/sounds/actor_shoot_sound.mp3"
BACKGROUND_SOUND = pathlib.Path(__file__).parent.parent / "assets/sounds/background_sound.mp3"
