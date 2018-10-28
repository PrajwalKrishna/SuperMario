'''Constants defined'''
LENGTH = 30
BREADTH = 500
FRAME_BREADTH = 100
FLOOR = 25
MAX_JUMP = 14


IDENTIFIER = {}
IDENTIFIER['board'] = ' '
IDENTIFIER['coin'] = '\033[1;93m' + '$' + '\033[39;22m'
IDENTIFIER['pipe'] = '\033[0;42;32m'+'*' + '\033[22;49;39m'
IDENTIFIER['mario'] = '\033[44;35mM\033[49;39m'
IDENTIFIER['pakistan'] = '\033[41;31m@\033[49;39m'
IDENTIFIER['brick'] = '\033[2;43;33m#\033[22;49;39m'
IDENTIFIER['china'] = '\033[41;95mB\033[49;39m'
IDENTIFIER['cloudSpace'] = '\033[1;96m+\033[22;39m'
IDENTIFIER['cloudSlash'] = '\033[1;96m/\033[22;39m'
IDENTIFIER['cloudBackSlash'] = '\033[1;96m\\\033[22;39m'
IDENTIFIER['valley'] = '\033[39m!\033[39m'
IDENTIFIER['bushSpace'] = '\033[1;92m+\033[22;39m'
IDENTIFIER['bushSlash'] = '\033[1;92m/\033[22;39m'
IDENTIFIER['bushBackSlash'] = '\033[1;92m\\\033[22;39m'
IDENTIFIER['bushPipe'] = '\033[1;92m|\033[22;39m'
IDENTIFIER['spring'] = '\033[1;91m%\033[22;39m'

IMP_CHAR = [IDENTIFIER['pipe'], IDENTIFIER['mario'], IDENTIFIER['pakistan']]
BAD_CHAR = [IDENTIFIER['pipe'], IDENTIFIER['brick'],
            IDENTIFIER['pakistan'], IDENTIFIER['china']]
DEAD_CHAR = [IDENTIFIER['pakistan'], IDENTIFIER['china']]
MARIO_CHAR = IDENTIFIER['mario']
SPRING_CHAR = IDENTIFIER['spring']


class Point:
    '''Defines a co-ordinate'''
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Dimension:
    '''Defines dimensions of an object in 2D world'''
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
