import sys

import pygame

from CODE.Constantes import SCREEN_HEIGHT, SCREEN_WIDTH, MENU_OPTION
from CODE.Level import Level
from CODE.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(SCREEN_HEIGHT, SCREEN_WIDTH))

    def run(self):
        while True:
            menu = Menu(self.screen)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.screen, 'Level1', menu_return)
                level_return = level.run()
            else:
                pygame.quit()
                sys.exit()
