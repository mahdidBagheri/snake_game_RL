import pygame


class Screen:
    def __init__(self, screen_width ,screen_hight):
        self.screen = pygame.display.set_mode((screen_width,screen_hight))