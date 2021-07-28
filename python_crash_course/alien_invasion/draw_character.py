import pygame

import util


class DrawCharacter:

    def __init__(self, image, screen):
        util.resize_image(image)
        self.screen = screen

        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.center = self.screen_rect.center

    def draw_character(self):
        self.screen.blit(self.image, self.rect)
