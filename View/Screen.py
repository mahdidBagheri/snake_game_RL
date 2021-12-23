import pygame
from Config import GameConfig, AssetsConfig


class Screen:
    def __init__(self, snake, food):
        self.screen = pygame.display.set_mode((GameConfig.Screen_Width,GameConfig.Screen_Hight))
        self.background = pygame.image.load(AssetsConfig.backGroundAddress)
        self.drawBackGround()
        self.drawIcons(snake, food)
        pygame.display.update()

    def drawBackGround(self):
        self.screen.blit(self.background,(0,0))

    def drawIcons(self,snake, food):
        self.drawBackGround()
        self.drawSnake(snake)
        self.drawFood(food)
        #self.drawWalls()

    def drawSnake(self, snake):
        self.screen.blit(snake.head_icon, snake.coordinates[0])
        for coor in snake.coordinates[1:]:
            self.screen.blit(snake.icon, coor)

    def drawFood(self, food):
        self.screen.blit(food.icon, food.coordinate)