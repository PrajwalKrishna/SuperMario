from base import *
COINS = []
USED_COINS = []
class Coins:
    ''' Coins from Mario World'''
    def __init__(self,point,board):
        self.point = point
        self.shape = [[identifier['coin']]]
        self.dimensions = Dimension(1,1)
        self.board = board
        self.pre = []
        COINS.append(self)
        self.draw()

    def draw(self):
        self.pre = self.board.current(self.point,self.shape,self.dimensions)
        self.board.update(self.point,self.shape,self.dimensions)

    def check(self):
        if self.board.matrix[self.point.x][self.point.y] == identifier['mario']:
            self.board.addCoin()
            self.removeCoin()

    def restore(self):
        ch =  self.board.matrix[self.point.x][self.point.y]
        if ch != identifier['coin']:
                return
        else:
            self.board.update(self.point,self.pre,self.dimensions)
            USED_COINS.remove(self)

    def removeCoin(self):
        self.board.update(self.point,self.pre,self.dimensions)
        COINS.remove(self)
        USED_COINS.append(self)

def coinRow(point,dimensions,board):
    for i in range(dimensions.length):
        for j in range(dimensions.breadth):
            Coins(Point(point.x + i,point.y + j),board)

if __name__ == "__main__":
    from board import *
    board = Board(26,26)
    board.display(0)
    coin = Coins(Point(1,2),board)
    board.display(0)
    print(board.matrix[1][2])
    print(identifier['coin'])
    print(coin.shape[0][0])
