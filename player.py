class Player:

    def __init__(self, logo: str, world: list, stroke: str):
        self.logo = logo
        self.world = world
        self.stroke = stroke

    def teleport(self, x, y):
        for _y in range(len(self.world)):
            for _x in range(len(self.world[x])):
                if self.world[_y][_x] == self.logo:
                    self.world[_y][_x] = self.stroke

        try:
            self.world[x][y] = self.logo
            self.world = self.world
        except IndexError:
            raise IndexError('You reached the maximum or minimum size of the world.')