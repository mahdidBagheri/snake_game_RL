from View import Screen
import pygame

class Game_View:
    def __init__(self, snake, food):
        self.screen = Screen.Screen(snake, food)


    def redraw(self, snake, food):

        self.screen.drawIcons(snake, food)
        pygame.display.update()
