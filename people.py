from base import *
class People:
    '''All people from Mario World'''
    def __init__(self,point,speed,shape,dimensions,board):
        self.point = point
        self.speed = speed
        self.shape = shape
        self.dimensions = dimensions
        self.board = board
        self.pre=False
        self.prePoint =False
        self.direction = 'R'

    def update(self):
        if(self.pre):
            self.board.update(self.prePoint,self.pre,self.dimensions)
        self.pre = self.board.current(self.point,self.shape,self.dimensions)
        self.prePoint = Point(self.point.x,self.point.y)
        self.board.update(self.point,self.shape,self.dimensions)

    def move_left(self,unit):
        if(self.point.y < unit):
            return False
        for j in range(self.dimensions.length):
            ch = self.board.matrix[self.point.x + j][self.point.y - unit]
            if ch == marioChar:
                self.board.mario.die()
            for i in badChar:
                if i==ch:
                    return False
        self.point.y -= unit;
        self.update()
        return True


    def move_right(self,unit):
        if(self.point.y + self.dimensions.breadth + unit  > BREADTH):
            return False
        for j in range(self.dimensions.length):
            ch = self.board.matrix[self.point.x + j][self.point.y + self.dimensions.breadth + unit - 1]
            if ch == marioChar:
                self.board.mario.die()
            for i in badChar:
                if i==ch:
                    return False
        self.point.y += unit;
        self.update()
        return True

    def die(self):
        self.board.update(self.prePoint,self.pre,self.dimensions)
        allEnemies.remove(self)
        if(self.__class__.__name__ == 'Pakistan'):
            self.board.addScore(10000)
            self.board.addKill()

    def selfMove(self,unit):
        if(self.direction == 'R'):
            if not self.move_right(unit):
                self.direction = 'L'
        else:
            if not self.move_left(unit):
                self.direction = 'R'
