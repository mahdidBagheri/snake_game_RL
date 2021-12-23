from Config import GameConfig , AssetsConfig
import pygame

class Snake:
    def __init__(self):
        self.icon = pygame.image.load(AssetsConfig.SnakeBlockAddress)
        self.direction = "left"
        self.coordinates = GameConfig.Snake_Initial_Coordinate

    def move_straight(self):
        pass