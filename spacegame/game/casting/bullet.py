from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.gamecontants import *
import pygame


class Bullet(Actor):
    """
    """
    def __init__(self, pos, direction):
        """
        """
        super().__init__()
        self.set_position(pos)
        self._dead = False
        self._previous_position = pos
        if (direction == 0):
            self.setImage(pygame.image.load(BULLET_IMAGE))
            self.set_velocity(Point(6,0))