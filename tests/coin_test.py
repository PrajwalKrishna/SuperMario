'''Function to test coins'''
from random import randint
from board import Board
from coins import Coins, COINS, USED_COINS, coin_row
from base import Point, Dimension, IDENTIFIER
from status import Status
from copy import deepcopy

class TestCoins(Coins):
    '''Class having functions to test Coins'''
    def test_init(self, point, board):
        '''Tests constructor'''
        PRE_COINS = deepcopy(COINS)
        Coins.__init__(self, point, board)
        assert point == self.point
        assert self.shape == [[IDENTIFIER['coin']]]
        assert self.dimensions.length == 1
        assert self.dimensions.breadth == 1
        assert board == self.board
        assert len(COINS) == len(PRE_COINS) + 1


    def test_draw(self):
        '''Test draw function'''
        self.draw()
        point = self.point
        for i in range(0, self.dimensions.length):
            for j in range(0, self.dimensions.breadth):
                assert self.shape[i][j] == self.board.matrix[point.x + i][point.y + j]

    def test_remove_coin(self):
        '''Tests function which removes coin'''
        self.draw()
        self.pre = '$'
        PRE_USED_COINS = deepcopy(USED_COINS)
        PRE_COINS = deepcopy(COINS)
        assert self.board.matrix[self.point.x][self.point.y] == self.shape[0][0]
        self.remove_coin()
        assert self.board.matrix[self.point.x][self.point.y] != self.shape[0][0]
        assert self.board.matrix[self.point.x][self.point.y] == '$'
        assert len(PRE_USED_COINS) == len(USED_COINS) - 1
        assert len(PRE_COINS) == len(COINS) + 1


    def test_coin_row(self):
        '''This function tests coin row'''
        point = Point(randint(0, 10), randint(0, 10))
        dimensions = Dimension( randint(1, 9), randint(1, 9))
        COIN_ROW = coin_row(point, dimensions, self.board)
        for i in range(point.x, point.x + dimensions.length):
            for j in range(point.y, point.y + dimensions.breadth):
                assert self.board.matrix[i][j] == IDENTIFIER['coin']


BOARD = Board(100, 100, Status())
x = randint(0, 10)
y = randint(0, 10)
COIN = TestCoins(Point(1, 1), BOARD)
COIN.test_init(Point(x, y), BOARD)
COIN.test_draw()
COIN.test_remove_coin()
COIN.test_coin_row()
