'''Constants defined'''
LENGTH = 30
BREADTH = 500
FRAME_BREADTH = 100
FLOOR = 25
MAX_JUMP = 14


identifier = {}
identifier['coin'] = '\033[1;33m' + '$' + '\033[39;22m'
identifier['pipe'] = '\033[0;42;32m'+'*' + '\033[22;49;39m'
identifier['mario'] = '\033[46;33m&\033[49;39m'
identifier['pakistan'] = '\033[41;31m@\033[49;39m'
identifier['brick'] = '\033[0;33m#\033[49;39m'
identifier['china'] = '@'

IMP_CHAR = [identifier['pipe'],identifier['mario'],identifier['pakistan'],'_']
badChar = [identifier['pipe'],identifier['brick'],'-',identifier['pakistan']]
deadChar = [identifier['pakistan']]
marioChar = identifier['mario']

allEnemies = []

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Dimension:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
