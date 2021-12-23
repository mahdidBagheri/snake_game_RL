import Config.AssetsConfig
import Config.GameConfig
import pygame
import random

class Food:
    def __init__(self):
        self.icon = pygame.image.icon(AssetsConfig.FoodBlockAddress)
        self.coordinate((random.randint(GameConfig.Game_Width),random.randint(GameConfig.Game_Hight)))


