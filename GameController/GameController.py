from View.Game_View import Game_View
from Snake.Snake import Snake
from Food.Food import Food
from Config import GameConfig , AssetsConfig
import time
import pygame

class GameController:
    def __init__(self):
        self.snake = Snake()
        self.food = Food(self.snake)
        self.game_view = Game_View(self.snake,self.food)
        self.score = 0

    def move_one_step(self):
        self.snake.move()
        self.game_view.redraw(self.snake, self.food)

    def event_handler(self, events, running):
        for event in events:
            if(event.type == pygame.QUIT):
                running = False

            elif(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_LEFT):
                    self.snake.setMoveDirection("left")
                elif(event.key == pygame.K_RIGHT):
                    self.snake.setMoveDirection("right")
                elif (event.key == pygame.K_DOWN):
                    self.snake.setMoveDirection("down")
                elif (event.key == pygame.K_UP):
                    self.snake.setMoveDirection("up")

        return running

    def refresh_and_check_status(self):
        if(self.snake.coordinates[0] == self.food.coordinate):
            self.score += 1
            self.food.switch_coordinate(self.snake)
            self.snake.grow()
            print("score: " + str(self.score))
            return False

        elif(self.snake.coordinates[0] in (self.game_view.screen.walls.coordinates + self.snake.coordinates[1:])):
            return True

    def endGame(self):
        print("game End")

    def wait(self):
        time.sleep(1/GameConfig.FPS)