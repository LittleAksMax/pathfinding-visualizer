import pygame


class Window(object):
    def __init__(self, width, height, caption):
        self.width = width
        self.height = height
        self.caption = caption
        self.display = pygame.display
        self.window = self.display.set_mode((self.width, self.height))
        self.display.set_caption(self.caption)
