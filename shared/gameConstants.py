import os


class GameConstants:
    BLOCK_SIZE = 30
    SCREEN_SIZE = (800, 600)

    SPRITE_BLOCK = os.path.join(r'..\assets', 'block.png')
    SPRITE_FLOOR = os.path.join(r'..\assets', 'floor.png')
    SPRITE_EGG = os.path.join(r'..\assets', 'egg.png')
    SPRITE_NEST = os.path.join(r'..\assets', 'nest.png')
    SPRITE_PLAYER = os.path.join(r'..\assets', 'player.png')
