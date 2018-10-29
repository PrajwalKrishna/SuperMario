'''People class testing'''
from people import People
from base import Point, Dimension
from board import Board
from status import Status

class TestPeople(People):
    '''Class for testing People'''
    def test_init(self, point, speed, shape, dimensions, board):
        '''Checks constructor function of People'''
        People.__init__(self, point, speed, shape, dimensions, board)
        assert self.point == point
        assert self.speed == speed
        assert self.shape == shape
        assert self.dimensions == dimensions
        assert self.board == board
        return self

    def test_update(self):
        '''Test for checking update function of person'''
        temp_shape = self.pre
        temp_location = self.pre_point
        self.update()
        #Check if old shape is stored
        assert self.pre and self.pre_point
        #Check update function

    def test_move_left(self, unit):
        '''Test moving left'''
        assert self.point.y >= 0
        while True:
            if self.point.y >= unit:
                temp = self.point.y
                if self.move_left(unit):
                    assert self.point.y == temp - unit
            elif self.point.y >= 0:
                self.move_left(self.point.y)
                assert self.point.y == 0
                self.move_left(1)
                assert self.point.y == 0
                break
        assert self.point.y >= 0

    def test_move_right(self, unit):
        '''Test moving right'''
        max_right = self.board.breadth - self.dimensions.breadth + 1
        assert 0 <= self.point.y < max_right
        while True:
            if self.point.y < max_right - unit - 1:
                temp = self.point.y
                if self.move_right(unit):
                    assert self.point.y == temp + unit
            elif self.point.y < max_right:
                self.move_right(max_right - self.point.y - 1)
                assert self.point.y == max_right - 1
                self.move_right(1)
                assert self.point.y == max_right - 1
                break
        assert 0 <= self.point.y < max_right



BOARD = Board(100, 100, Status())
PEOPLE = TestPeople(Point(10, 10), 1, [['#', '#'], ['#', '#']], Dimension(2,2), BOARD)
PEOPLE.test_init(Point(10, 10), 1, [['#', '#'], ['#', '#']], Dimension(2,2), BOARD)
PEOPLE.test_move_left(4)
PEOPLE.test_move_right(7)
PEOPLE.test_update()
