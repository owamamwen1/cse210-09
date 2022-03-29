import pygame
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.gameconstants import *
pygame.mixer.init()


class Bullet(Actor):
    """
    """
    # The actor sound
    
    ACTOR_SOUND = pygame.mixer.Sound(ACTOR_SOUND)

    def __init__(self, pos, direction):
        """
        """
        super().__init__()
        self.set_position(pos)
        self._dead = False
        self._previous_position = pos
        if (direction == 0):
            self.set_image(BULLET_IMAGE)
            self.set_velocity(Point(20, 0))
            self.ACTOR_SOUND.play()
        if (direction == 1):
            self.set_image(pygame.image.load(BULLET_ENEMY_IMAGE))
            self.set_velocity(Point(-63, 0))
        