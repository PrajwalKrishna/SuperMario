'''Defines behaviour of enemies of Mario'''
from people import People
from base import Point, Dimension, IDENTIFIER

class SlaveEnemy(People):
    '''Small and weak Villans'''

    def __init__(self, x, y, board):
        ch = IDENTIFIER['SlaveEnemy']
        shape = [[ch, ch], [ch, ch]]
        board.all_enemies.append(self)
        People.__init__(self, Point(x, y), 1, shape, Dimension(2, 2), board)


class BossEnemy(People):
    '''Weak and smart enemy'''

    def __init__(self, x, y, board):
        ch = IDENTIFIER['BossEnemy']
        shape = [[ch, ch, ch], [ch, ch, ch], [ch, ch, ch]]
        board.all_enemies.append(self)
        People.__init__(self, Point(x, y), 1, shape, Dimension(3, 3), board)

    def self_move(self, unit):
        if 20 > self.point.y - self.board.mario.point.y > 0:
            if not self.move_left(2 * unit):
                self.move_right(2 * unit)
        elif 20 > self.board.mario.point.y - self.point.y > 0:
            if not self.move_right(2 * unit):
                self.move_left(2 * unit)
        else:
            People.self_move(self, 2 * unit)
