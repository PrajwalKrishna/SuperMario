from people import *
'''Mario Development Program'''
class Mario(People):
    def __init__(self,x,y,board):
        shape = [[marioChar] * 3] * 3
        People.__init__(self,Point(x,y),1,shape,Dimension(3,3),board)
        self.state = 0
        self.air = 0
        self.board.mario = self
        self.update()

    def grow(self):
        '''On eating of weeds'''
        self.shape = [[marioChar]*4]*4
        self.dimensions = Dimension(4,4)
        self.state = 1

    def depricate(self):
        '''On getting kicked'''
        self.shape = [[marioChar]*3]*3
        self.dimensions = Dimension(3,3)
        self.state = 0

    def shooter(self):
        self.shape = [[marioChar]*4]*4
        self.dimensions = Dimension(4,4)
        self.state = 2

    def die(self):
        self.board.status._life -= 1
        self.board.update(self.prePoint,self.pre,self.dimensions)
        self.board.status.die()

    def jump(self,unit):
        '''Under Development'''
        if(self.air + unit > MAX_JUMP):
            return False
        if(self.point.x - unit < 0):
            unit = self.point.x
        while unit:
            for j in range(self.dimensions.breadth):
                ch = self.board.matrix[self.point.x - unit][self.point.y + j]
                for i in badChar:
                    if i==ch:
                        unit -= 2
                        break
                else:
                    continue
                break
            else:
                break
        if not unit:
            return False
        self.point.x -= unit
        self.air += unit
        self.update()
        return True

    def gravity(self,unit):
        '''Simulate gravity'''
        if(self.point.x > FLOOR - 1):
            self.die()
            return
        for i in range(self.point.y,self.point.y + self.dimensions.breadth):
            arr = self.board.matrix[self.point.x + self.dimensions.length]
            if arr[i] == springChar:
                self.jump(MAX_JUMP)
                return
            for j in badChar:
                if arr[i] == j:
                    #logic to check for killing enemy
                    if j in deadChar:
                        enemiesList = self.board.allEnemies
                        for k in enemiesList:
                            if(k.point.x <= self.point.x + self.dimensions.length < k.point.x + k.dimensions.length):
                                if(k.point.y <= i < k.point.y + k.dimensions.breadth):
                                    k.die()
                                    return
                    else:
                        self.air = 0
                        return
        self.point.x += unit
        self.update()
