'''Board class testing'''
from board import Board
from status import Status
from base import Point, Dimension

class TestBoard(Board):
    '''Class for testing Board and functions'''
    def test_init(self, length, breadth, status):
        '''Tests the constructor functions of board'''
        Board.__init__(self, length, breadth, status)
        assert self.length == length
        assert self.breadth == breadth
        assert self.status == status
        assert not self.all_enemies
        assert not self.mario
        assert len(self.matrix) == length
        assert len(self.matrix[0]) == breadth

    def test_current(self, point, shape, dimensions):
        '''This function test current function'''
        shape = self.current(point, shape, dimensions)
        alt_shape = [['' for _ in range(dimensions.breadth)]
                 for _ in range(dimensions.length)]
        for i in range(point.x, dimensions.length + point.x):
            for j in range(point.y, dimensions.breadth + point.y):
                assert shape[i - point.x][j - point.y] == self.matrix[i][j]

    #def 

STATUS = Status()
BOARD = TestBoard(200, 100, STATUS)
BOARD.test_init(200, 100, STATUS)
BOARD.test_current(Point(2, 2), [], Dimension(5, 5) )
