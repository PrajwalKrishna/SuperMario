'''This creates and base board'''
from os import system
from base import *
from time import time

class Board:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
        self.life = 3
        self.level = 1
        self._coins = 0
        self._score = 0
        self.time = 0
        self.mario = None
        self._kills = 0
        self.beginTime = time()*10
        matrix = []
        for i in range(0,length):
            matrix.append(['.']*breadth)
            self.matrix = matrix
        for i in range(0,breadth):
            self.matrix[FLOOR][i]='-'

    def mario(self,mario):
        self.mario = mario

    def addCoin(self):
        self._coins += 1
        self._score += 1000
        if self._coins == 100:
            self._coins = 0
            self.life += 1

    def updateTime(self):
        pre = self.time
        self.time = int(time()*10 - self.beginTime)
        self._score += (self.time - pre)*10

    def addScore(self,point):
        self._score += point

    def addKill(self):
        self._kills += 1
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
        print('Level = ',self.level,"\tScore = ",self._score,'\t Coins = ',self._coins,'\t Lives = ',self.life,'\t Time = ',self.time,'\t Kills = ',self._kills)
        for i in self.matrix:
            for j in i[offset:offset + FRAME_BREADTH]:
                print(j,end ='')
            print('')
            #print(''.join(i[offset:offset + FRAME_BREADTH]))


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
