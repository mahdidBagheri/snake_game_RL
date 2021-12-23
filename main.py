from View.Game_View import Game_View
from GameController.GameController import GameController

if(__name__ == "__main__"):
    #Game init
    game_controller = GameController()

    #Game Loop
    while True:
        game_controller.move_one_step()
        isEnd = game_controller.check_status()
        if(isEnd):
            game_controller.endGame()
            break