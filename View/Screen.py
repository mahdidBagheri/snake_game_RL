import pygame
from Config import GameConfig
from Snake.Snake import Snake
from Food.Food import Food

class Screen:
    def __init__(self):
        self.screen = pygame.display.set_mode((GameConfig.Screen_Width,GameConfig.Screen_Hight))
        self.snake = Snake()
        self.food = Food()
        self.drawIcons()

    def drawIcons(self):
        self.drawSnake()
        self.drawFood()

    def drawSnake(self):
        for coor in self.snake.coordinates:
            self.screen.blit(self.snake.icon, coor)

    def drawFood(self):
        self.screen.blit(self.food.icon, self.food.coordinate)