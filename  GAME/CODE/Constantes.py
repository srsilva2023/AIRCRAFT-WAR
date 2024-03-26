import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 128)
COLOR_GREEN = (0, 128, 0)
COLOR_CYAN = (0, 128, 128)

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
                'Player1Shot': 2,
                'Player2': 3,
                'Player2Shot': 3,
                'Enemy1': 1,
                'Enemy1Shot': 2,
                'Enemy2': 1,
                'Enemy2Shot': 2,
                }

ENTITY_HEALTH = {'level1bg1': 999,
                 'level1bg2': 999,
                 'level1bg3': 999,
                 'level1bg4': 999,
                 'level1bg5': 999,
                 'level1bg6': 999,
                 'level1bg7': 999,
                 'Player1': 300,
                 'Player1Shot': 1,
                 'Player2': 300,
                 'Player2Shot': 1,
                 'Enemy1': 50,
                 'Enemy1Shot': 5,
                 'Enemy2': 60,
                 'Enemy2Shot': 1,
                 }
ENTITY_DAMAGE = {'level1bg1': 0,
                 'level1bg2': 0,
                 'level1bg3': 0,
                 'level1bg4': 0,
                 'level1bg5': 0,
                 'level1bg6': 0,
                 'level1bg7': 0,
                 'Player1': 0,
                 'Player1Shot': 0,
                 'Player2': 0,
                 'Player2Shot': 0,
                 'Enemy1': 100,
                 'Enemy1Shot': 0,
                 'Enemy2': 125,
                 'Enemy2Shot': 0,
                 }
ENTITY_SCORE = {'level1bg1': 0,
                'level1bg2': 0,
                'level1bg3': 0,
                'level1bg4': 0,
                'level1bg5': 0,
                'level1bg6': 0,
                'level1bg7': 0,
                'Player1': 1,
                'Player1Shot': 25,
                'Player2': 1,
                'Player2Shot': 20,
                'Enemy1': 1,
                'Enemy1Shot': 20,
                'Enemy2': 1,
                'Enemy2Shot': 15,
                }
ENTITY_SHOT_DELAY = {'Player1': 1,
                     'Player2': 1,
                     'Enemy1': 100,
                     'Enemy2': 200,
                     }

PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}

PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}

PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}

PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}

PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL,
                    'Player2': pygame.K_LCTRL}

EVENT_ENEMY = pygame.USEREVENT + 1
