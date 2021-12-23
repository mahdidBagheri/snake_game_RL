from View.Game_View import Game_View
from Snake.Snake import Snake
from Food.Food import Food
from Config import GameConfig , AssetsConfig, AIConfig
import time
import pygame

class AIGameController:
    def __init__(self):
        self.snake = Snake()
        self.food = Food(self.snake)
        self.game_view = Game_View(self.snake,self.food)
        self.score = 0
        self.frame_iteration = 0

    def move_one_step(self,move_dir):
        self.frame_iteration += 1
        self.apply_move(move_dir)
        self.snake.move()
        self.game_view.redraw(self.snake, self.food)
        self.refresh_and_check_status()

    def apply_move(self,move_dir):
        if(move_dir[0] == 1):
            return
        elif(move_dir[1] == 1):
            if(self.snake.move == "left"):
                self.snake.move_direction = "up"
            elif(self.snake.move == "up"):
                self.snake.move_direction = "right"
            elif(self.snake.move == "right"):
                self.snake.move_direction = "down"
            elif(self.snake.move == "down"):
                self.snake.move_direction = "left"
        elif(move_dir[2] == 1):
            if(self.snake.move == "left"):
                self.snake.move_direction = "down"
            elif(self.snake.move == "up"):
                self.snake.move_direction = "left"
            elif(self.snake.move == "right"):
                self.snake.move_direction = "up"
            elif(self.snake.move == "down"):
                self.snake.move_direction = "right"

    def refresh_and_check_status(self):

        if(self.snake.coordinates[0] == self.food.coordinate):
            self.score += 10
            reward = 10
            self.food.switch_coordinate(self.snake)
            self.snake.grow()
            print("score: " + str(self.score))

            return reward, False, self.score

        elif(self.snake.coordinates[0] in (self.game_view.screen.walls.coordinates + self.snake.coordinates[1:])):
            self.score -= 10
            reward = -10
            return reward, True, self.score

        else:
            self.score -= AIConfig.gamma
            reward = -AIConfig.gamma

            return reward, False, self.score


    def get_state(self):
        state = []
        state += self.snake.get_danger()
        state += self.snake.get_direction()
        state += get_food_direction()
        return state

    def get_food_direction(self):
        dir = [0,0,0,0]

        (x, y) = self.snake.coordinates[0]
        if( x < self.food.coordinate[0] ):
            dir[0] = 1
        if(x >= self.food.coordinate[0]):
            dir[1] = 1
        if(y < self.food.coordinate[0]):
            dir[2] = 1
        if(y >= self.food.coordinate[0]):
            dir[3] = 1
        return dir