'''Function to test coins'''
from randint import random
from board import Board
from coins import Coins, COINS, USED_COINS
from base import Point, Dimension, IDENTIFIER
from status import Status

class TestCoins(Coins):
    '''Class having functions to test Coins'''
    pre_coins = COINS
    def test_init(self, point, board):
        '''Tests constructor'''
        Coins.__init__(self, point, board)
        assert point == self.point
        assert self.shape == [[IDENTIFIER['coin']]]
        assert self.dimensions == Dimension(1,1)
        assert board == self.board
        assert self.pre == []
        assert len(COINS) == len(pre_coins) + 1


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
x = randint(0, 10)
y = randint(0, 10)
COIN = TestCoins(Point(x, y), BOARD)
#COIN.test_init(Point(1, 1),[['#', '#'], ['#', '#']],Dimension(2, 2), BOARD)
#COIN.test_draw()
