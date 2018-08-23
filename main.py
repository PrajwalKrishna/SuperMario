from background import *
from enemy import *
from board import *
from obstacles import *
from mario import *
from user import *
from hurdles import *

def makeBackground(board):
    for i in range(randint(4,7)):
        cloud = Cloud(board)
        cloud.draw()
    for i in range(randint(3,6)):
        bush = Bush(board)
        bush.draw()
        
class Level:
    '''Making of level'''
    def __init__(self,screens):
        self.screens = screens
