#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from CODE.Constantes import COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, SCREEN_HEIGHT, COLOR_YELLOW


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.surf = pygame.image.load('./Imagens/background.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./Sons/nave.mp3')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.02)
        menu_option = 0
        while True:
            # DESENHAR NA TELA

            self.screen.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, 'AIRCRAFT', COLOR_ORANGE, (SCREEN_HEIGHT // 2, 70))
            self.menu_text(50, 'WAR', COLOR_ORANGE, (SCREEN_HEIGHT // 2, 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, (SCREEN_HEIGHT // 2, 200 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, (SCREEN_HEIGHT // 2, 200 + 30 * i))
            pygame.display.flip()

            # VERIFICAR EVENTOS

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION(menu_option)

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucid Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color). convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surf, dest=text_rect)
