from base import *
class Obstacle:
    '''All obstacles from Mario World'''
    def __init__(self,point,shape,dimensions,board):
        self.point = point
        self.shape = shape
        self.dimensions = dimensions
        self.board = board

    def draw(self):
        self.board.update(self.point,self.shape,self.dimensions)



class Pipe(Obstacle):
    '''Iconic pipes '''
    def __init__(self,y,height,board):
        focus = Point(FLOOR - height,y)
        dimensions = Dimension(height,5)
        shape = [list([identifier['pipe']] * 5)] * height
        Obstacle.__init__(self,focus,shape,dimensions,board)

class Brick(Obstacle):
    '''Bricks of all kind'''
    def __init__(self,point,dimensions,board):
        shape = [list([identifier['brick']] * dimensions.breadth)] * dimensions.length
        Obstacle.__init__(self,point,shape,dimensions,board)
        self.pre = self.board.current(self.point,self.shape,self.dimensions)
        self.health = 1

    def breakBrick(self):
        self.health -= 1
        if not self.health:
            pass

    def elasticBrick(self):
        self.health = 5

class Valley(Obstacle):
    def __init__(self,start,breadth,board):
        '''Pit or valley'''
        dimensions = Dimension(5,breadth)
        shape = [list([identifier['valley']] * dimensions.breadth)] * dimensions.length
        Obstacle.__init__(self,Point(FLOOR,start),shape,dimensions,board)
