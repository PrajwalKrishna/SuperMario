'''Functions related to coins'''
from base import Point, Dimension, IDENTIFIER
COINS = []
USED_COINS = []


class Coins:
    ''' Coins from Mario World'''

    def __init__(self, point, board):
        self.point = point
        self.shape = [[IDENTIFIER['coin']]]
        self.dimensions = Dimension(1, 1)
        self.board = board
        self.pre = []
        COINS.append(self)
        self.draw()

    def draw(self):
        '''Function to render coin on board'''
        self.pre = self.board.current(self.point, self.shape, self.dimensions)
        self.board.update(self.point, self.shape, self.dimensions)

    def check(self):
        '''Logic to check presence of coin'''
        if self.board.matrix[self.point.x][self.point.y] == IDENTIFIER['mario']:
            self.board.status.add_coin()
            self.remove_coin()

    def restore(self):
        '''Function to restore coin after enemy'''
        ch = self.board.matrix[self.point.x][self.point.y]
        if ch != IDENTIFIER['coin']:
            return
        self.board.update(self.point, self.pre, self.dimensions)
        USED_COINS.remove(self)

    def remove_coin(self):
        '''Function to remove coin'''
        self.board.update(self.point, self.pre, self.dimensions)
        COINS.remove(self)
        USED_COINS.append(self)


def coin_row(point, dimensions, board):
    '''Function to generate a row of coins'''
    for i in range(dimensions.length):
        for j in range(dimensions.breadth):
            Coins(Point(point.x + i, point.y + j), board)
