import pygame
import pathlib


class Body(pygame.sprite.Sprite):

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(pathlib.Path(__file__).parent / 'gear.jpg')
        self.gameDisplay = pygame.display.set_mode((500, 500))
        self.gameDisplay.blit(self.image, (10, 10))
        self.image = pygame.Surface([30, 20])
        self.image.fill((50, 200, 250))
        self.rect = self.image.get_rect()

        self.rect.center = pos

    def car(self, x, y):
        self.gameDisplay.blit(self.image, (x, y))
