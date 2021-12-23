from Config import AssetsConfig, GameConfig
import pygame
import random

class Food:
    def __init__(self):
        self.icon = pygame.image.load(AssetsConfig.FoodBlockAddress)
        self.coordinate = (random.randint(0,GameConfig.Game_Width),random.randint(0,GameConfig.Game_Hight))


