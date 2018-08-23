from base import *
from random import randint

class Nature:
    def __init__(self,point,dimensions,shape,board):
        self.point = point
        self.dimensions = dimensions
        self.shape = shape
        self.board = board
        self.draw()

    def draw(self):
        self.board.update(self.point,self.shape,self.dimensions)


class Cloud(Nature):
    def __init__(self,board):
        shape = [ list('/\\'*6) , list('\\'+' '*10+'/') , list('/'+' '*10+'\\') , list('\\/'*6)]
        focus = Point(randint(0,7),randint(4,board.breadth - 14))
        Nature.__init__(self,focus,Dimension(4,12),shape,board)

class Mountain(Nature):
    def __init__(self,board):
        shape = []
        focus = Point(FLOOR+4,randint(5,board.breadth - 5))
        Nature.__init__(self,focus,Dimension(4,12),shape,board)

class Bush(Nature):
    def __init__(self,board):
        shape = [list('/\\' * 6) ,list('|' + ' ' * 10 + '|') ,list('|'+ '_' * 10 + '|')]
        focus = Point(FLOOR-3,randint(2,board.breadth - 14))
        Nature.__init__(self,focus,Dimension(3,12),shape,board)



if __name__ == '__main__':
    mountain = """
       /\\
      /  \\
     /    \\
    /______\\
    """
