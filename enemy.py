from people import *

class Pakistan(People):
    '''Small and weak Villans'''
    def __init__(self,x,y,board):
        ch = identifier['pakistan']
        shape = [[ch,ch],[ch,ch]]
        allEnemies.append(self)
        People.__init__(self,Point(x,y),1,shape,Dimension(2,2),board)

class China(People):
    '''Weak and smart enemy'''
    def __init__(self,x,y,board):
        ch = identifier['china']
