#!/usr/bin/python
# -*- coding: utf-8 -*-
from CODE.Constantes import SCREEN_WIDTH, ENTITY_SPEED
from CODE.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = SCREEN_WIDTH
