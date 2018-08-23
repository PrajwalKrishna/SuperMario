'''Constants defined'''
LENGTH = 30
BREADTH = 500
FRAME_BREADTH = 100
FLOOR = 25
MAX_JUMP = 14


identifier = {}
#identifier['board'] = '\033[2;40m' + ' ' + '\033[49;22m'
identifier['board'] = ' '
identifier['coin'] = '\033[1;93m' + '$' + '\033[39;22m'
identifier['pipe'] = '\033[0;42;32m'+'*' + '\033[22;49;39m'
identifier['mario'] = '\033[44;35mM\033[49;39m'
identifier['pakistan'] = '\033[41;31m@\033[49;39m'
identifier['brick'] = '\033[2;43;33m#\033[22;49;39m'
identifier['china'] = '\033[41;95mB\033[49;39m'
identifier['cloudSpace'] = '\033[1;96m+\033[22;39m'
identifier['cloudSlash'] = '\033[1;96m/\033[22;39m'
identifier['cloudBackSlash'] = '\033[1;96m\\\033[22;39m'
identifier['valley'] = '\033[39m!\033[39m'
identifier['bushSpace'] = '\033[1;92m+\033[22;39m'
identifier['bushSlash'] = '\033[1;92m/\033[22;39m'
identifier['bushBackSlash'] = '\033[1;92m\\\033[22;39m'
identifier['bushPipe'] = '\033[1;92m|\033[22;39m'
identifier['spring'] = '\033[1;91m%\033[22;39m'

IMP_CHAR = [identifier['pipe'],identifier['mario'],identifier['pakistan']]
badChar = [identifier['pipe'],identifier['brick'],identifier['pakistan'],identifier['china']]
deadChar = [identifier['pakistan'],identifier['china']]
marioChar = identifier['mario']
springChar = identifier['spring']

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Dimension:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
