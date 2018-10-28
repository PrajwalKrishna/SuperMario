'''Spring and related functions'''
from obstacles import Obstacle
from base import IDENTIFIER, Point, FLOOR, Dimension


class Spring(Obstacle):
    '''Spring from mario World '''

    def __init__(self, y, height, board):
        focus = Point(FLOOR - height, y)
        dimensions = Dimension(height, 7)
        pipe = IDENTIFIER['pipe']
        spring = IDENTIFIER['spring']
        shape = [[pipe, pipe, spring, spring, spring, pipe, pipe]] * height
        Obstacle.__init__(self, focus, shape, dimensions, board)
