from View import Screen

class Game_View:
    def __init__(self, snake, food):
        self.screen = Screen.Screen(snake, food)

    def refresh(self):
        pygame.display.update()
