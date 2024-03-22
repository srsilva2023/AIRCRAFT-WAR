#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from CODE.Background import Background
from CODE.Constantes import SCREEN_WIDTH, SCREEN_HEIGHT
from CODE.Enemy import Enemy
from CODE.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'level1bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'level1bg{i}', (0, 0)))
                    list_bg.append(Background(f'level1bg{i}', (SCREEN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, SCREEN_HEIGHT / 2 - 30))

            case 'Player2':
                return Player('Player2', (10, SCREEN_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (SCREEN_WIDTH + 10, random.randint(0 + 40, SCREEN_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (SCREEN_WIDTH + 10, random.randint(0 + 40, SCREEN_HEIGHT - 40)))
