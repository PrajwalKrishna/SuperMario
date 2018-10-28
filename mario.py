'''Mario Development Program'''
from people import People
from base import BAD_CHAR, MARIO_CHAR, FLOOR, SPRING_CHAR, MAX_JUMP, DEAD_CHAR, Point, Dimension


class Mario(People):
    '''Class defining mario'''
    def __init__(self, x, y, board):
        shape = [[MARIO_CHAR] * 3] * 3
        People.__init__(self, Point(x, y), 1, shape, Dimension(3, 3), board)
        self.state = 0
        self.air = 0
        self.board.mario = self
        self.update()

    def grow(self):
        '''On eating of weeds'''
        self.shape = [[MARIO_CHAR]*4]*4
        self.dimensions = Dimension(4, 4)
        self.state = 1

    def depricate(self):
        '''On getting kicked'''
        self.shape = [[MARIO_CHAR]*3]*3
        self.dimensions = Dimension(3, 3)
        self.state = 0

    def shooter(self):
        '''Mario on 3 rd stage'''
        self.shape = [[MARIO_CHAR]*4]*4
        self.dimensions = Dimension(4, 4)
        self.state = 2

    def die(self):
        self.board.status._life -= 1
        self.board.update(self.pre_point, self.pre, self.dimensions)
        self.board.status.die()

    def jump(self, unit):
        '''Under Development'''
        if self.air + unit > MAX_JUMP:
            return False
        if self.point.x - unit < 0:
            unit = self.point.x
        while unit:
            for j in range(self.dimensions.breadth):
                ch = self.board.matrix[self.point.x - unit][self.point.y + j]
                for i in BAD_CHAR:
                    if i == ch:
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

    def gravity(self, unit):
        '''Simulate gravity'''
        if self.point.x > FLOOR - 1:
            self.die()
            return
        for i in range(self.point.y, self.point.y + self.dimensions.breadth):
            arr = self.board.matrix[self.point.x + self.dimensions.length]
            if arr[i] == SPRING_CHAR:
                self.jump(MAX_JUMP)
                return
            for j in BAD_CHAR:
                if arr[i] == j:
                    # logic to check for killing enemy
                    if j in DEAD_CHAR:
                        ememies_list = self.board.all_enemies
                        for k in ememies_list:
                            if k.point.x <= self.point.x + self.dimensions.length < k.point.x + k.dimensions.length:
                                if k.point.y <= i < k.point.y + k.dimensions.breadth:
                                    k.die()
                                    return
                    else:
                        self.air = 0
                        return
        self.point.x += unit
        self.update()
