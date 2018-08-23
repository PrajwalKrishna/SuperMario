from obstacles import *
class Spring(Obstacle):
    '''Spring from mario World '''
    def __init__(self,y,height,board):
        focus = Point(FLOOR - height,y)
        dimensions = Dimension(height,7)
        a = identifier['pipe']
        b = identifier['spring']
        shape = [[a,a,b,b,b,a,a]] * height
        Obstacle.__init__(self,focus,shape,dimensions,board)
