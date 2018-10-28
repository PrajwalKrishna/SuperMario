'''Defining background barriers'''
from random import randint
from base import FLOOR, Point, Dimension, IDENTIFIER


class Nature:
    '''Parent class of all background barriers'''
    def __init__(self, point, dimensions, shape, board):
        self.point = point
        self.dimensions = dimensions
        self.shape = shape
        self.board = board
        self.draw()

    def draw(self):
        '''How to render on board'''
        self.board.update(self.point, self.shape, self.dimensions)


class Cloud(Nature):
    '''Makes clouds'''
    def __init__(self, board):
        slash = IDENTIFIER['cloudSlash']
        backslash = IDENTIFIER['cloudBackSlash']
        space = IDENTIFIER['cloudSpace']
        temp = [space]*10
        shape = [[slash, backslash] * 6, [backslash, *temp, slash],
                 [slash, *temp, backslash], [backslash, slash]*6]
        focus = Point(randint(0, 7), randint(4, board.breadth - 14))
        Nature.__init__(self, focus, Dimension(4, 12), shape, board)


class Mountain(Nature):
    '''Makes mountain'''
    def __init__(self, board):
        shape = []
        focus = Point(FLOOR+4, randint(5, board.breadth - 5))
        Nature.__init__(self, focus, Dimension(4, 12), shape, board)


class Bush(Nature):
    '''Makes bushes'''
    def __init__(self, board):
        slash = IDENTIFIER['bushSlash']
        backslash = IDENTIFIER['bushBackSlash']
        space = IDENTIFIER['bushSpace']
        pipe = IDENTIFIER['bushPipe']
        temp = [space]*10
        shape = [[slash, backslash] * 6, [pipe, *temp, pipe], [pipe, *temp, pipe]]
        focus = Point(FLOOR-3, randint(2, board.breadth - 14))
        Nature.__init__(self, focus, Dimension(3, 12), shape, board)
