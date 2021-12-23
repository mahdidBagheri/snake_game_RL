from Config import AssetsConfig, GameConfig
import pygame
import random
from Utils.Utils import Utils

class Food:
    def __init__(self, snake):

        self.icon = pygame.image.load(AssetsConfig.FoodBlockAddress)
        self.coordinate = self.random_coordinate(snake)

    def switch_coordinate(self, snake):
        self.coordinate = self.random_coordinate(snake)

    def random_coordinate(self, snake):
        unallowedOpt = Utils.border_coordinates(self)
        unallowedOpt = unallowedOpt + snake.coordinates
        scale = GameConfig.scale

        rnd = (random.randint(0, GameConfig.Game_Width - 1) * scale, random.randint(0, GameConfig.Game_Hight - 1) * scale)
        while (rnd in unallowedOpt):
            rnd = (random.randint(0, GameConfig.Game_Width - 1) * scale, random.randint(0, GameConfig.Game_Hight - 1) * scale)

        return rnd