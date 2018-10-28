'''Level maker'''
#from background import *
from random import randint
from user import getInput
from board import Board
from background import Cloud, Bush
from mario import Mario
from hurdles import HURDLES
from coins import COINS, USED_COINS
from castle import Castle
from base import IDENTIFIER, LENGTH, FLOOR


class Level:
    '''Making of level'''

    def __init__(self, breadth, status):
        if not status._level % 3:
            IDENTIFIER['board'] = '\033[1;96m~\033[22;39m'
        else:
            IDENTIFIER['board'] = ' '
        self.board = Board(LENGTH, breadth, status)
        self.status = status
        self.offset = 0
        self.breadth = breadth

        # Generate random background
        if status._level % 3:
            for _ in range(randint(breadth//20, breadth//16)):
                _ = Cloud(self.board)
        for _ in range(randint(breadth//15, breadth//10)):
            _ = Bush(self.board)
        self.display()

        self.generate_hurdles()
        self.display()

        self.mario = Mario(FLOOR - 3, 3, self.board)
        self.display()
        while True:
            self.scheduler()

    def scheduler(self):
        '''order of execution in each iteration'''
        self.mario.gravity(2)
        for i in USED_COINS:
            i.restore()
        for i in self.board.all_enemies:
            i.self_move(1)
        self.move_screen()
        self.user_response()
        for i in COINS:
            i.check()
        self.display()
        if self.breadth - self.mario.point.y < 20:
            self.board.status.level_up()

    def display(self):
        '''Render the board'''
        self.board.status.update_time()
        self.board.display(self.offset)

    def move_screen(self):
        '''Move screen logic'''
        if self.mario.point.y - self.offset > 50:
            self.offset += 15
        if self.mario.point.y - self.offset < 0:
            self.offset -= 15

    def user_response(self):
        '''Get user input and react accordingly'''
        ch = getInput()
        if ch == 'a':
            self.mario.move_left(1)
        elif ch == 'd':
            self.mario.move_right(1)
        elif ch == 'q':
            quit()
        elif ch == 'w':
            self.mario.jump(6)

    def generate_hurdles(self):
        '''Set hurdles for the level'''
        hurdles = HURDLES
        options = len(hurdles)
        x = 20
        while x < self.breadth - 35:
            option = randint(0, options-1)
            if hurdles[option][0] + x < self.breadth - 35:
                hurdles[option][1](x, self.board)
                x += hurdles[option][0]
                x += randint(10, 20)
            else:
                break

        _ = Castle(self.breadth - 33, self.board)
