import pygame

from CODE.Constantes import SCREEN_HEIGHT, SCREEN_WIDTH
from CODE.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(SCREEN_HEIGHT, SCREEN_WIDTH))

    def run(self, ):
        while True:
            menu = Menu(self.screen)
            menu.run()
        pass
