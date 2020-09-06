from shared.gameObject import GameObject


class Sprite(GameObject):

    def __init__(self, position, sprite):
        super().__init__(position, sprite)

        self._position = position
        self._sprite = sprite
