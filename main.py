from View.Game_View import Game_View
from GameController.GameController import GameController
import pygame

if(__name__ == "__main__"):
    #Game init
    game_controller = GameController()

    #Game Loop
    running = True
    while running:
        running = game_controller.event_handler(pygame.event.get(),running)
        game_controller.move_one_step()
        isEnd = game_controller.refresh_and_check_status()
        if(isEnd):
            game_controller.endGame()
            running = False


        game_controller.wait()