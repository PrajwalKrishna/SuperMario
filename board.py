'''This creates and base board'''
from os import system
from base import IDENTIFIER, FLOOR, FRAME_BREADTH
from coins import COINDICT, COINS

class Board:
    '''Board class'''
    def __init__(self, length, breadth, status):
        self.length = length
        self.breadth = breadth
        self.mario = None
        self.all_enemies = []
        self.status = status
        matrix = []
        ch1 = IDENTIFIER['board']
        for _ in range(0, FLOOR):
            matrix.append([ch1] * breadth)
        ch2 = IDENTIFIER['brick']
        for _ in range(FLOOR, length):
            matrix.append([ch2] * breadth)
        self.matrix = matrix

    def current(self, point, shape, dimensions):
        '''Makes and handles current board'''
        shape = [["" for i in range(dimensions.breadth)]
                 for j in range(dimensions.length)]
        for i in range(0, dimensions.length):
            for j in range(0, dimensions.breadth):
                shape[i][j] = self.matrix[point.x + i][point.y + j]
        return shape

    def update(self,point,shape,dimensions):
            for i in range(0,dimensions.length):
                for j in range(0,dimensions.breadth):
                    if self.matrix[point.x + i][point.y + j] == IDENTIFIER['coin'] and shape[i][j] == IDENTIFIER['mario']:
                        try:
                            coinIndex = COINDICT[point.y + j][point.x + i]
                            COINS[coinIndex].check()
                        except Exception as e:
                            #This exists to capture any issues that can occur because the board doesn't update fast enough
                            pass
                    self.matrix[point.x + i][point.y + j] = shape[i][j]

    def display(self, offset):
        '''Renders boards frame by frame'''
        system('clear')
        self.status.print_status()
        for i in self.matrix:
            for j in i[offset:offset + FRAME_BREADTH]:
                print(j, end='')
            print('')
