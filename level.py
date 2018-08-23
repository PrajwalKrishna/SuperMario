from background import *
from enemy import *
from board import *
from obstacles import *
from mario import *
from user import *
from hurdles import *
from coins import *
import colorama
from castle import *

class Level:
    '''Making of level'''
    def __init__(self,breadth,status):
        if(not status._level % 3):
            identifier['board'] = '\033[1;96m~\033[22;39m'
        else:
            identifier['board'] = ' '
        self.board = Board(LENGTH,breadth,status)
        self.status = status
        self.offset = 0
        self.breadth = breadth

        #Generate random background
        if(status._level % 3):
            for i in range(randint(breadth//20,breadth//16)):
                cloud = Cloud(self.board)
        for i in range(randint(breadth//15,breadth//10)):
            bush = Bush(self.board)
        self.display()

        self.generateHurdles()
        self.display()

        self.mario = Mario(FLOOR - 3,3,self.board)
        self.display()
        while True:
            self.scheduler()

    def scheduler(self):
        self.mario.gravity(2)
        for i in USED_COINS:
            i.restore()
        for i in self.board.allEnemies:
            i.selfMove(1)
        self.moveScreen()
        self.userResponse()
        for i in COINS:
            i.check()
        self.display()
        if self.breadth - self.mario.point.y < 10:
            self.board.status.levelUp()

    def display(self):
        self.board.status.updateTime()
        self.board.display(self.offset)

    def moveScreen(self):
        if(self.mario.point.y - self.offset > 50):
            self.offset += 15
        if(self.mario.point.y - self.offset < 0):
            self.offset -= 15

    def userResponse(self):
        ch = getInput()
        if ch == 'a':
            self.mario.move_left(1)
        elif ch == 'd':
            self.mario.move_right(1)
        elif ch == 'q':
            quit()
        elif ch == 'w':
            self.mario.jump(6)

    def generateHurdles(self):
        hurdles = HURDLES
        options = len(hurdles)
        x = 20
        while( x < self.breadth - 35 ):
            option = randint(0,options-1)
            if hurdles[option][0] + x < self.breadth - 35:
                hurdles[option][1](x,self.board)
                x += hurdles[option][0]
                x += randint(10,20)
            else:
                break

        castle = Castle(self.breadth - 33,self.board)        
