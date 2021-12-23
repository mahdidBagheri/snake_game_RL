import pygame
from Config import GameConfig, AssetsConfig
from Wall.Wall import Wall

class Screen:
    def __init__(self, snake, food):
        self.screen = pygame.display.set_mode((GameConfig.Screen_Width,GameConfig.Screen_Hight))
        self.background = pygame.image.load(AssetsConfig.backGroundAddress)
        self.walls = Wall()
        self.drawIcons(snake, food)

        pygame.display.update()

    def drawBackGround(self):
        self.screen.blit(self.background,(0,0))

    def drawIcons(self,snake, food):
        self.drawBackGround()
        self.drawSnake(snake)
        self.drawFood(food)
        self.drawWalls()

    def drawWalls(self):
        for wall_coor in self.walls.coordinates:
            self.screen.blit(self.walls.icon, wall_coor)

    def drawSnake(self, snake):
        for coor in snake.coordinates[1:]:
            self.screen.blit(snake.icon, coor)

        self.screen.blit(snake.head_icon, snake.coordinates[0])

    def drawFood(self, food):
        self.screen.blit(food.icon, food.coordinate)