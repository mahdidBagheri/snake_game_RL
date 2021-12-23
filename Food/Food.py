from Config import AssetsConfig, GameConfig
import pygame
import random

class Food:
    def __init__(self):
        scale = GameConfig.scale
        self.icon = pygame.image.load(AssetsConfig.FoodBlockAddress)
        self.coordinate = (random.randint(0,GameConfig.Game_Width-1)*scale,random.randint(0,GameConfig.Game_Hight-1)*scale)


