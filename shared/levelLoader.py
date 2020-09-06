import pygame
from shared.gameConstants import GameConstants
from source.sprite import Sprite


class LevelLoader:
    floor_sprite = pygame.image.load(GameConstants.SPRITE_FLOOR)
    floor_sprite = pygame.transform.scale(floor_sprite, (GameConstants.BLOCK_SIZE, GameConstants.BLOCK_SIZE))

    wall_sprite = pygame.image.load(GameConstants.SPRITE_BLOCK)
    wall_sprite = pygame.transform.scale(wall_sprite, (GameConstants.BLOCK_SIZE, GameConstants.BLOCK_SIZE))

    nest_sprite = pygame.image.load(GameConstants.SPRITE_NEST)
    nest_sprite = pygame.transform.scale(nest_sprite, (GameConstants.BLOCK_SIZE, GameConstants.BLOCK_SIZE))

    egg_sprite = pygame.image.load(GameConstants.SPRITE_EGG)
    egg_sprite = pygame.transform.scale(egg_sprite, (GameConstants.BLOCK_SIZE, GameConstants.BLOCK_SIZE))

    player_sprite = pygame.image.load(GameConstants.SPRITE_PLAYER)
    player_sprite = pygame.transform.scale(player_sprite, (GameConstants.BLOCK_SIZE, GameConstants.BLOCK_SIZE))

    @staticmethod
    def render(current_level):
        with open(f'..\\levels\\level{current_level}.txt', 'r') as ipt:
            data = ipt.read()

        lines = data.split('\n')
        width = len(lines[0])
        height = len(lines)
        x_offset = GameConstants.SCREEN_SIZE[0] / 2 - width * GameConstants.BLOCK_SIZE / 2
        y_offset = GameConstants.SCREEN_SIZE[1] / 2 - height * GameConstants.BLOCK_SIZE / 2

        floors, walls, nests, eggs = [], [], [], []
        player = None
        col, row = 0, 0
        size = GameConstants.BLOCK_SIZE

        for line in lines:
            for c in line:
                posn = (size * col + x_offset, size * row + y_offset)
                if c == "0":
                    floors.append(Sprite(posn, LevelLoader.floor_sprite))
                elif c == "1":
                    walls.append(Sprite(posn, LevelLoader.wall_sprite))
                elif c == "2":
                    nests.append(Sprite(posn, LevelLoader.nest_sprite))
                elif c == "3":
                    floors.append(Sprite(posn, LevelLoader.floor_sprite))
                    eggs.append(Sprite(posn, LevelLoader.egg_sprite))
                elif c == "4":
                    floors.append(Sprite(posn, LevelLoader.floor_sprite))
                    player = Sprite(posn, LevelLoader.player_sprite)
                elif c == "5":
                    nests.append(Sprite(posn, LevelLoader.nest_sprite))
                    eggs.append(Sprite(posn, LevelLoader.egg_sprite))
                elif c == "6":
                    nests.append(Sprite(posn, LevelLoader.nest_sprite))
                    player = Sprite(posn, LevelLoader.player_sprite)
                col += 1
            row += 1
            col = 0
        return floors, walls, nests, eggs, player