class GameObject:

    def __init__(self, position, sprite):
        self._position = position
        self._sprite = sprite

    def setPosition(self, position):
        self._position = position

    def getPosition(self):
        return self._position

    def getSprite(self):
        return self._sprite

    def _intersectsY(self, other):
        other_position = other.getPosition()

        if self._position[1] >= other_position[1] and self._position[1] <= other_position[1]:
            return 1

        return 0

    def _intersectsX(self, other):
        other_position = other.getPosition()

        if self._position[0] >= other_position[0] and self._position[0] <= other_position[0]:
            return 1

        return 0

    def intersects(self, other):
        if self._intersectsY(other) and self._intersectsX(other):
            return 1
        return 0

    def collides_with(self, other):
        (x, y) = other.getPosition()
        if self._position[0] == x and self._position[1] == y:
            return 1
        return 0

    def move(self, offset):
        (x, y) = offset
        self._position = (self._position[0] + x, self._position[1] + y)

    def draw(self, target_surface):
        target_surface.blit(self._sprite, self._position)
