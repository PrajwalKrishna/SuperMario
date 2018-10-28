'''Defines all obstacles in marioworld'''
from base import FLOOR, Dimension, IDENTIFIER, Point


class Obstacle:
    '''All obstacles from Mario World'''

    def __init__(self, point, shape, dimensions, board):
        self.point = point
        self.shape = shape
        self.dimensions = dimensions
        self.board = board

    def draw(self):
        '''Function to put on board'''
        self.board.update(self.point, self.shape, self.dimensions)


class Pipe(Obstacle):
    '''Iconic pipes '''

    def __init__(self, y, height, board):
        focus = Point(FLOOR - height, y)
        dimensions = Dimension(height, 5)
        shape = [list([IDENTIFIER['pipe']] * 5)] * height
        Obstacle.__init__(self, focus, shape, dimensions, board)


class Brick(Obstacle):
    '''Bricks of all kind'''

    def __init__(self, point, dimensions, board):
        shape = [list([IDENTIFIER['brick']] * dimensions.breadth)
                 ] * dimensions.length
        Obstacle.__init__(self, point, shape, dimensions, board)
        self.pre = self.board.current(self.point, self.shape, self.dimensions)
        self.health = 1

    def break_brick(self):
        '''Brick which can be broken in 1 go'''
        self.health -= 1
        if not self.health:
            pass

    def elastic_brick(self):
        '''Bricks which behaves like spring and break later'''
        self.health = 5


class Valley(Obstacle):
    '''Pit or valley'''

    def __init__(self, start, breadth, board):
        dimensions = Dimension(5, breadth)
        shape = [list([IDENTIFIER['valley']] * dimensions.breadth)
                 ] * dimensions.length
        Obstacle.__init__(self, Point(FLOOR, start), shape, dimensions, board)
