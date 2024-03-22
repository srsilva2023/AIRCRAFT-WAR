#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from CODE.Constantes import COLOR_WHITE, MENU_OPTION, EVENT_ENEMY
from CODE.Entity import Entity
from CODE.EntityFactory import EntityFactory


class Level:
    def __init__(self, screen, name: str, menu_option):
        self.screen: Surface = screen
        self.name = name
        self.mode = menu_option
        self.entity_list = list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, 4000)

    def run(self):
        pygame.mixer_music.load(f'./Sons/{self.name}.mp3')  # SOM BACKGROUND
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.02)
        clock = pygame.time.Clock()  # VELOCIDADE BACKGROUND
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.screen.blit(source=ent.surf, dest=ent.rect)
                self.level_text(14, f'FPS:{clock.get_fps(): .0f}', COLOR_WHITE, (10, 10))
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
            pygame.display.flip()
            pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucid Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.screen.blit(source=text_surf, dest=text_rect)
