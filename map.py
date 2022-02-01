import random

class Map:

    def __init__(self, x = 0, y = 0, r: bool = False, fill = None):
        # check for random world
        self.r = r
        if self.r:
            self.x = random.randint(1, 20)
            self.y = random.randint(1, 20)
        else:
            self.x = x
            self.y = y

        if fill == None:
            self.fill = '⬛'
        else:
            self.fill = fill

        # generate world
        world=[]
        for y in range(self.y):
            world.append([])
            for x in range(self.x):
                world[y].append(fill)
        self.world = world

    # print world
    def out(self):
        for y in range(len(self.world)):
            for x in range(len(self.world[y])):
                print(self.world[y][x], end = '')
                if x == len(self.world[y])-1:
                    print('\n')

    # modify map
    def add(self, column: int = None, content: list = None):
        if content != None:
            if content[0] <= len(self.world)-1:
                self.world[content[0]].append(content[1])
            self.world=self.world

        if column != None:
            for _ in range(column[0]):
                self.world.append(column[1])
            self.world=self.world