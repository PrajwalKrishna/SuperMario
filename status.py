'''Stores status of current game'''
from time import time
from level import Level


class Status:
    '''Store game Status'''

    def __init__(self):
        self._life = 3
        self._level = 1
        self._coins = 0
        self._score = 0
        self._time = 0
        self._kills = 0
        self._begin_time = time()

    def make_game(self):
        '''Starts a level'''
        _ = Level(self._level * 100, self)

    def add_coin(self):
        '''Increments coins'''
        self._coins += 1
        self._score += 250
        if self._coins == 50:
            self._coins = 0
            self._life += 1

    def update_time(self):
        '''Maintains timer'''
        pre = self._time
        self._time = int(time() - self._begin_time)
        self._score += (self._time - pre)

    def add_score(self, point):
        '''Increments score by passed points'''
        self._score += point

    def add_kill(self):
        '''Increments kills'''
        self._kills += 1

    def die(self):
        '''Restarts games on death of mario'''
        # Game over
        self.make_game()

    def level_up(self):
        '''Increments the level'''
        self._level += 1
        self.make_game()

    def print_status(self):
        '''Shows status on top of board'''
        print('Level = ', self._level, "\tScore = ", self._score, '\t Coins = ', self._coins,
              '\t Lives = ', self._life, '\t Time = ', self._time, '\t Kills = ', self._kills)
