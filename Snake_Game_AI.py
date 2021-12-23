from View.Game_View import Game_View
from AI.AIGameController import AIGameController

import pygame

if (__name__ == "__main__"):
    # Game init
    game_controller = AIGameController()

    # Game Loop
    running = True
    while running:

        game_controller.move_one_step()
        isEnd = game_controller.refresh_and_check_status()
        if (isEnd):
            running = False

        game_controller.wait()