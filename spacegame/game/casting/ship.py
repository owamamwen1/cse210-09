from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.gamecontants import *
import pygame

import time

class Ship(Actor):

    def __init__(self, pos = Point(0, 0), image = ACTOR_IMAGE, health = 100, vector_vel = 3, shoot_rate = .5):
        """
        """
        super().__init__()
        self._position = pos
        self._image = pygame.image.load(image)
        self._health = health
        self._vector_vel = vector_vel
        self._shoot_rate = shoot_rate
        self._t = time.perf_counter()

    def add_to_health(self, points):
        """
        """
        if (self._health + points <= 0):
            self._health = 0
        else:
            self._health += points

    def set_health(self, points):
        """
        """
        self._health = points

    def get_health(self):
        """
        """
        return self._health

    def is_recharged(self):
        """
        """
        t_now = time.perf_counter()
        diff = t_now - self._t
        return diff > self._shoot_rate

    def uncharge(self):
        """
        """
        self._t = time.perf_counter()

    def set_vector_vel(self, vel):
        """
        """
        self._vector_vel = vel

    def get_vector_vel(self):
        """
        """
        return self._vector_vel

    def set_shoot_rate(self, rate):
        """
        """
        self._shoot_rate = rate

    def get_shoot_rate(self):
        """
        """
        return self._shoot_rate
