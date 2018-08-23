'''This creates and base board'''
from os import system
from base import *

class Board:
    def __init__(self,length,breadth,status):
        self.length = length
        self.breadth = breadth
        self.mario = None
        self.allEnemies = []
        self.status = status
        matrix = []
        ch = identifier['board']
        for i in range(0,FLOOR):
            matrix.append([ch] * breadth)
        ch2 = identifier['brick']
        for j in range(FLOOR,length):
            matrix.append([ch2] * breadth)    
        self.matrix = matrix

    def current(self,point,shape,dimensions):
            shape = [["" for i in range(dimensions.breadth)]for j in range(dimensions.length)]
            for i in range(0,dimensions.length):
                for j in range(0,dimensions.breadth):
                    shape[i][j] = self.matrix[point.x + i][point.y +j]
            return shape

    def update(self,point,shape,dimensions):
            for i in range(0,dimensions.length):
                for j in range(0,dimensions.breadth):
                    self.matrix[point.x + i][point.y +j] = shape[i][j]

    def display(self,offset):
        system('clear')
        self.status.printStatus()
        for i in self.matrix:
            for j in i[offset:offset + FRAME_BREADTH]:
                print(j,end ='')
            print('')


if __name__ == '__main__':
    from random import randint
    from background import *
    board = Board(LENGTH,BREADTH)
    for i in range(randint(4,7)):
        cloud = Cloud(board)
        cloud.draw()
    for i in range(randint(3,6)):
        bush = Bush(board)
        bush.draw()
    board.display(0)
