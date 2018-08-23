from obstacles import *
from enemy import *
from coins import *
class Hurdle:
    '''A group of obstacles'''
    def __init__(self,start,width,obstacles,enemies,board):
        self.start = start
        self.width = width
        self.obstacles = obstacles
        self.enemies = enemies
        self.board = board

    def load(self):
        for i in self.obstacles:
            i.draw()
        for i in self.enemies:
            i.update()

    def motion(self):
        for i in self.enemies:
            i.selfMove(1)

class ThreePipes(Hurdle):
    '''Creating three pipe hurdle'''
    def __init__(self,start,board):
        width = 21
        obstacles = []
        obstacles.append(Pipe(start,6,board))
        obstacles.append(Pipe(start + 8,10,board))
        obstacles.append(Pipe(start + 16,14,board))
        Hurdle.__init__(self,start,width,obstacles,[],board)
        self.load()

class TwoPipes(Hurdle):
    ''' 2 enemies between two pipes'''
    def __init__(self,start,board):
        width = 36
        obstacles = []
        obstacles.append(Pipe(start,6,board))
        obstacles.append(Pipe(start + 30,6,board))
        enemy = []
        enemy.append(Pakistan(FLOOR - 2,start + 9,board))
        enemy.append(Pakistan(FLOOR - 2,start + 13,board))
        Hurdle.__init__(self,start,width,obstacles,enemy,board)
        self.load()

class BrickJungle(Hurdle):
    '''Some arrangement of bricks'''
    def __init__(self,start,board):
        width = 56
        obstacles = []
        obstacles.append(Brick(Point(19,start),Dimension(2,5),board))
        obstacles.append(Brick(Point(15,start + 8),Dimension(2,5),board))
        obstacles.append(Brick(Point(11,start + 16),Dimension(2,5),board))
        obstacles.append(Brick(Point(5,start + 21),Dimension(2,11),board))
        obstacles.append(Brick(Point(11,start + 32),Dimension(2,5),board))
        obstacles.append(Brick(Point(15,start + 40),Dimension(2,5),board))
        obstacles.append(Brick(Point(19,start + 48),Dimension(2,5),board))

        coinRow(Point(4,start+21),Dimension(1,11),board)
        Hurdle.__init__(self,start,width,obstacles,[],board)
        self.load()
