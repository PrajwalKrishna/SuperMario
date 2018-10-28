'''Functions related to coins'''
from base import Point, Dimension, IDENTIFIER
COINS = {}
USED_COINS = []
COINDICT = {}
totalcoin = 0

class Coins:
    ''' Coins from Mario World'''

    def __init__(self, point, board):
        self.point = point
        self.shape = [[IDENTIFIER['coin']]]
        self.dimensions = Dimension(1, 1)
        self.board = board
        self.pre = []
        self.id = totalcoin
        self.store_coin(self.point)
        self.draw()

    def store_coin(self, point):
        COINS[totalcoin] = self
        if point.y in COINDICT.keys():
            tmpDict = COINDICT[point.y]
        else:
            tmpDict = {}
        tmpDict[point.x] = totalcoin
        COINDICT[point.y] = tmpDict


    def draw(self):
        '''Function to render coin on board'''
        self.pre = self.board.current(self.point, self.shape, self.dimensions)
        self.board.update(self.point, self.shape, self.dimensions)

    def check(self):
        '''Logic to check presence of coin'''
        self.board.status.add_coin()
        self.removeCoin()

    def restore(self):
        '''Function to restore coin after enemy'''
        ch =  self.board.matrix[self.point.x][self.point.y]
        if ch != IDENTIFIER['coin']:
                return
        else:
            self.board.update(self.point,self.pre,self.dimensions)
            USED_COINS.remove(self)

    def removeCoin(self):
        '''Function to remove coin'''
        self.board.update(self.point,self.pre,self.dimensions)
        USED_COINS.append(self)
        del COINS[self.id]
        COINDICT[self.point.y].pop(self.point.x)
        if len(COINDICT[self.point.y]) == 0:
            del COINDICT[self.point.y]


def coin_row(point, dimensions, board):
    '''Function to generate a row of coins'''
    for i in range(dimensions.length):
        for j in range(dimensions.breadth):
            Coins(Point(point.x + i,point.y + j),board)
            global totalcoin 
            totalcoin += 1
