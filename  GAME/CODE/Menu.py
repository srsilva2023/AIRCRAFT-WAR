#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from CODE.Constantes import SCREEN_WIDTH


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.surf = pygame.image.load('./Imagens/background.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./Sons/nave.mp3')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.02)
        while True:
            self.screen.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, 'AIRCRAFT WAR', (255, 128, 0), ((SCREEN_WIDTH / 2), 70))
            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucid Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.screen.blit(source=text_surf, dest=text_rect)

    pass
