import pygame
from shared.gameConstants import GameConstants
from shared.levelLoader import LevelLoader

# for x in range(161):
#     print(f'-------{x}')
#     with open(f'..\levels\level{x}.txt') as ipt:
#         text = ipt.read()
#     text = text.replace('7', ' ')
#     with open(f'..\levels\level{x}.txt', 'w') as opt:
#         opt.write(text)
#     print(text)
# exit()

TITLE = 'Python Push Box'
BACKGROUND = (100, 149, 237)
MAX_LEVEL = 160

pygame.font.init()

WIN = pygame.display.set_mode(GameConstants.SCREEN_SIZE)

screen = pygame.display.set_mode(GameConstants.SCREEN_SIZE, pygame.DOUBLEBUF, 32)

pygame.mouse.set_visible(False)


def collides_with_list(mover, sprites):
    for item in list(set(sprites) - set([mover])):
        if mover.collides_with(item):
            return item
    return None


def is_puzzle_solved(eggs, nests):
    counter = 0
    for egg in eggs:
        for nest in nests:
            if egg.getPosition() == nest.getPosition():
                counter += 1
    return counter == len(nests)


def save_current_state(undo_list, eggs, player):
    location = [player.getPosition()]
    for egg in eggs:
        location.append(egg.getPosition())
    undo_list.append(location)
    return undo_list


def draw_lists(win, lists):
    for list in lists:
        for item in list:
            item.draw(win)


def main():
    win = WIN
    undo_list = []
    current_level = 0
    (floors, walls, nests, eggs, player) = LevelLoader.render(current_level)
    pygame.display.set_caption(TITLE + f' - Level {current_level}')
    clock = pygame.time.Clock()
    clock_speed = 60
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                break
            if event.type == pygame.KEYDOWN:
                (x, y) = 0, 0
                if event.key == pygame.K_r:
                    # reset level
                    (floors, walls, nests, eggs, player) = LevelLoader.render(current_level)
                    print(len(eggs))
                    undo_list = []
                    continue
                elif event.key == pygame.K_PAGEUP:
                    # previous level
                    current_level = max(current_level - 1, 1)
                    (floors, walls, nests, eggs, player) = LevelLoader.render(current_level)
                    pygame.display.set_caption(TITLE + f' - Level {current_level}')
                    continue
                elif event.key == pygame.K_PAGEDOWN:
                    # next level
                    current_level = min(current_level + 1, MAX_LEVEL)
                    (floors, walls, nests, eggs, player) = LevelLoader.render(current_level)
                    pygame.display.set_caption(TITLE + f' - Level {current_level}')
                    continue
                elif event.key == pygame.K_u:
                    if len(undo_list) > 0:
                        location = undo_list.pop()
                        for egg in eggs:
                            pos = location.pop()
                            egg.setPosition(pos)
                        player.setPosition(location.pop())
                    continue

                elif event.key == pygame.K_LEFT:
                    x -= GameConstants.BLOCK_SIZE
                elif event.key == pygame.K_RIGHT:
                    x += GameConstants.BLOCK_SIZE
                elif event.key == pygame.K_UP:
                    y -= GameConstants.BLOCK_SIZE
                elif event.key == pygame.K_DOWN:
                    y += GameConstants.BLOCK_SIZE
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                else:
                    break

                has_moved = True

                undo_list = save_current_state(undo_list, eggs, player)

                player.move((x, y))

                egg = collides_with_list(player, eggs)

                if egg is not None:
                    egg.move((x, y))

                    if collides_with_list(egg, walls):
                        player.move((-x, -y))
                        egg.move((-x, -y))
                        has_moved = False
                    if collides_with_list(egg, eggs):
                        player.move((-x, -y))
                        egg.move((-x, -y))
                        has_moved = False

                if collides_with_list(player, walls):
                    player.move((-x, -y))
                    has_moved = False

                if not has_moved:
                    undo_list.pop()

                if is_puzzle_solved(eggs, nests):
                    current_level = min(current_level + 1, MAX_LEVEL)
                    (floors, walls, nests, eggs, player) = LevelLoader.render(current_level)
                    pygame.display.set_caption(TITLE + f' - Level {current_level}')
                    undo_list = []

        screen.fill(BACKGROUND)
        draw_lists(win, (floors, walls, nests, eggs))
        player.draw(win)
        pygame.display.flip()
        clock.tick(clock_speed)


if __name__ == '__main__':
    main()
