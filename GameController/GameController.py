from View.Game_View import Game_View
from Snake.Snake import Snake
from Food.Food import Food

class GameController:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.game_view = Game_View(self.snake,self.food)

    def move_one_step(self):
        pass

    def check_status(self):
        pass

    def endGame(self):
        pass
