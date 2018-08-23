from people import *

class Pakistan(People):
    '''Small and weak Villans'''
    def __init__(self,x,y,board):
        ch = identifier['pakistan']
        shape = [[ch,ch],[ch,ch]]
        board.allEnemies.append(self)
        People.__init__(self,Point(x,y),1,shape,Dimension(2,2),board)

class China(People):
    '''Weak and smart enemy'''
    def __init__(self,x,y,board):
        ch = identifier['china']
        shape = [[ch,ch,ch],[ch,ch,ch],[ch,ch,ch]]
        board.allEnemies.append(self)
        People.__init__(self,Point(x,y),1,shape,Dimension(3,3),board)

    def selfMove(self,unit):
        if 20 > self.point.y - self.board.mario.point.y > 0:
            if not self.move_left(2 * unit):
                self.move_right( 2 * unit)
        elif 20 > self.board.mario.point.y - self.point.y > 0:
            if not self.move_right(2 * unit):
                self.move_left(2 * unit)
        else:
            People.selfMove(self,2 * unit)
