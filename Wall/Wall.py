from Config import GameConfig, AssetsConfig
import pygame
from Utils.Utils import Utils

class Wall:
    def __init__(self):
        self.icon = pygame.image.load(AssetsConfig.wallBlockAddress)
        self.coordinates = Utils.border_coordinates(self)
