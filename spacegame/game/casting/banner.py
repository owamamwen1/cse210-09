from game.casting.actor import Actor
import pygame

class Banner(Actor):


    def __init__(self, pos, text = 'Text', font_size = 32):

        pygame.font.init()
        self._position = pos
        self._font_size = font_size
        self._font = pygame.font.Font('freesansbold.ttf', font_size)
        self._text_image = self._font.render(text, True, (250,250,250))

    def set_text(self, text):
        self._text_image = self._font.render(text, True, (250,250,250))

    def set_image(self, image):
        self.set_text(image)

    def get_image(self):
        return self._text_image

    def set_font_size(self, size):
        self._font_size = size