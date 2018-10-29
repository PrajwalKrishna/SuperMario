'''Test for testing background functions'''
from board import Board
from background import Nature
from base import Point, Dimension
from status import Status

class TestNature(Nature):
    '''Class having functions to test Nature'''
    def test_init(self, point, dimensions, shape, board):
        '''Tests constructor'''
        Nature.__init__(self, point, dimensions, shape, board)
        assert point == self.point
        assert shape == self.shape
        assert dimensions == self.dimensions
        assert board == self.board

    def test_draw(self):
        '''Test draw function'''
        from random import randint
        dimensions = Dimension(randint(1, 9),randint(1, 9))
        shape = []
        self.dimensions = dimensions
        for _ in range(0, dimensions.length):
            temp = []
            for _ in range(0, dimensions.breadth):
                temp.append(randint(0, 9))
            shape.append(temp)
        self.shape = shape
        self.draw()
        point = self.point
        for i in range(0, self.dimensions.length):
            for j in range(0, self.dimensions.breadth):
                assert self.shape[i][j] == self.board.matrix[point.x + i][point.y + j]



BOARD = Board(100, 100, Status())
BACKGROUND = TestNature(Point(1, 1), Dimension(2, 2), [['#', '#'], ['#', '#']], BOARD)
BACKGROUND.test_init(Point(1, 1), Dimension(2, 2), [['#', '#'], ['#', '#']], BOARD)
BACKGROUND.test_draw()
