'''Test for testing background functions'''
from random import randint
from base import Point, Dimension

class TestPoint(Point):
    '''Class having functions to test Point'''
    def test_init(self, x, y):
        '''Tests constructor'''
        Point.__init__(self, x, y)
        assert x == self.x
        assert y == self.y


class TestDimension(Dimension):
    '''Class having functions to test Dimension'''
    def test_init(self, length, breadth):
        '''Tests constructor'''
        Dimension.__init__(self, length, breadth)
        assert length == self.length
        assert breadth == self.breadth

x = randint(1, 1000)
y = randint(1, 1000)
POINT = TestPoint(x, y)
POINT.test_init(x, y)
DIMENSION = TestDimension(x, y)
DIMENSION.test_init(x, y)
