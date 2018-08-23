from base import *
from random import randint

class Nature:
    def __init__(self,point,dimensions,shape,board):
        self.point = point
        self.dimensions = dimensions
        self.shape = shape
        self.board = board
        self.draw()

    def draw(self):
        self.board.update(self.point,self.shape,self.dimensions)


class Cloud(Nature):
    def __init__(self,board):
        ch1 = identifier['cloudSlash']
        ch2 = identifier['cloudBackSlash']
        ch3 = identifier['cloudSpace']
        temp = [ch3]*10
        shape = [ [ch1,ch2] * 6 , [ch2,*temp,ch1] , [ch1,*temp,ch2] , [ch2,ch1]*6]
        focus = Point(randint(0,7),randint(4,board.breadth - 14))
        Nature.__init__(self,focus,Dimension(4,12),shape,board)

class Mountain(Nature):
    def __init__(self,board):
        shape = []
        focus = Point(FLOOR+4,randint(5,board.breadth - 5))
        Nature.__init__(self,focus,Dimension(4,12),shape,board)

class Bush(Nature):
    def __init__(self,board):
        ch1 = identifier['bushSlash']
        ch2 = identifier['bushBackSlash']
        ch3 = identifier['bushSpace']
        ch4 = identifier['bushPipe']
        temp = [ch3]*10
        shape = [ [ch1,ch2] * 6 ,[ch4,*temp,ch4] ,[ch4,*temp,ch4]]
        focus = Point(FLOOR-3,randint(2,board.breadth - 14))
        Nature.__init__(self,focus,Dimension(3,12),shape,board)



if __name__ == '__main__':
    mountain = """
       /\\
      /  \\
     /    \\
    /______\\
    """
    ch1 = identifier['cloudSlash']
    ch2 = identifier['cloudBackSlash']
    ch3 = identifier['cloudSpace']

    cloud = [[ch1,ch2]*6]
    temp = [ch3]*10
    cloud.append([ch2,*temp,ch1])
    for i in cloud:
        for j in i:
            print(len(j))
            print(j,end = '')
        print('')
    print(cloud[0][0])
