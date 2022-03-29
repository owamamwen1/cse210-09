from game.shared.gamecontants import *
import pygame
from pygame import mixer


class DisplayService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state 
    on the screen. 
    """

    def __init__(self, caption, width, height, frame_rate):
        """Constructs a new DisplayService using the specified debug mode. ???

        Args:
            debug (bool): whether or not to draw in debug mode. ???
        """
        self._caption = caption
        self._width = width
        self._height = height
        self._iconlogo = pygame.image.load(LOGO_IMAGE)
        self._background = pygame.image.load(BACK_GROUND_IMAGE)
        # Here we calculate the frame duration in milliseconds dividing 1000 by the frame rate.
        self._frame_duration = int(1000 / frame_rate)

    # The background sound
    def background_sound(self):
        mixer.music.load(BACK_GROUND_SOUND)
        mixer.music.play(-1)

    def draw_actor(self, actor):
        """Draws the given actor's text on the screen.

        Args:
            actor (Actor): The actor to draw.
        """
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        self.screen.blit(actor.get_image(), (x, y))

    def draw_actors(self, actors):
        """Draws the text for the given list of actors on the screen.

        Args:
            actors (list): A list of actors to draw.
        """
        self.screen.fill((0, 0, 0))
        self.screen.blit(self._background, (0, 0))
        pygame.display.set_caption(CAPTION)
        pygame.display.set_icon(self._iconlogo)
        for actor in actors:
            self.draw_actor(actor)
        pygame.display.update()

    def get_height(self):
        """Gets the display screen's height.

        Returns:
            Grid: The display screen's height.
        """
        return self._height

    def get_width(self):
        """Gets the display screen's width.

        Returns:
            Grid: The display screen's width.
        """
        return self._width

    def get_frame_duration(self):
        """"""
        return self._frame_duration

    def open_window(self):
        """Opens a new window with the provided title.

        Args:
            title (string): The title of the window.
        """
        self.screen = pygame.display.set_mode((self._width, self._height))
        self.background_sound()
