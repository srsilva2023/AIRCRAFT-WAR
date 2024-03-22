import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 128)

SCREEN_HEIGHT = 576
SCREEN_WIDTH = 324

MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'EXIT')

ENTITY_SPEED = {'level1bg1': 0,
                'level1bg2': 1,
                'level1bg3': 2,
                'level1bg4': 3,
                'level1bg5': 4,
                'level1bg6': 5,
                'level1bg7': 6,
                'Player1': 3,
                'Player2': 3,
                'Enemy1': 2,
                'Enemy2': 1,
                }

PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}

PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}

PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}

PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}

EVENT_ENEMY = pygame.USEREVENT + 1
