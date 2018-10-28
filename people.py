'''This modules defines behaviour of people both enemies and mario'''
from base import MARIO_CHAR, BAD_CHAR, Point


class People:
    '''All people from Mario World'''

    def __init__(self, point, speed, shape, dimensions, board):
        self.point = point
        self.speed = speed
        self.shape = shape
        self.dimensions = dimensions
        self.board = board
        self.pre = False
        self.pre_point = False
        self.direction = 'R'

    def update(self):
        '''Logic of update clearing of board and restoring'''
        if self.pre:
            self.board.update(self.pre_point, self.pre, self.dimensions)
        self.pre = self.board.current(self.point, self.shape, self.dimensions)
        self.pre_point = Point(self.point.x, self.point.y)
        self.board.update(self.point, self.shape, self.dimensions)

    def move_left(self, unit):
        '''Logic of moving left'''
        if self.point.y < unit:
            return False
        for j in range(self.dimensions.length):
            ch = self.board.matrix[self.point.x + j][self.point.y - unit]
            if ch == MARIO_CHAR:
                self.board.mario.die()
            for i in BAD_CHAR:
                if i == ch:
                    return False
        self.point.y -= unit
        self.update()
        return True

    def move_right(self, unit):
        '''Logic of moving right'''
        if self.point.y + self.dimensions.breadth + unit > self.board.breadth:
            return False
        for j in range(self.dimensions.length):
            ch = self.board.matrix[self.point.x +
                                   j][self.point.y + self.dimensions.breadth + unit - 1]
            if ch == MARIO_CHAR:
                if self.__class__.__name__ == 'China' and j == 0:
                    pass
                else:
                    self.board.mario.die()
            for i in BAD_CHAR:
                if i == ch:
                    return False
        self.point.y += unit
        self.update()
        return True

    def die(self):
        '''Defines how to die'''
        self.board.status.add_kill()
        self.board.update(self.pre_point, self.pre, self.dimensions)
        self.board.all_enemies.remove(self)
        if self.__class__.__name__ == 'Pakistan':
            self.board.status.add_score(10000)
        else:
            self.board.status.add_score(900000)

    def self_move(self, unit):
        '''Defines how does board makes them move automatically'''
        if self.direction == 'R':
            if not self.move_right(unit):
                self.direction = 'L'
        else:
            if not self.move_left(unit):
                self.direction = 'R'
