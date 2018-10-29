#!/usr/bin/python
# -*- coding: utf-8 -*-
'''Test all functions related to self class'''
from random import randint
from status import Status


class TestStatus(Status):

    '''Class for testing self functions'''

    def test_init(self):
        '''Check constuction'''
        assert self._life == 3
        assert self._life == 3
        assert self._level == 1
        assert self._coins == 0
        assert self._score == 0
        assert self._time == 0
        assert self._kills == 0


    def test_add_coin(self):
        '''Function to test add_coin'''
        while True:
            coins = self._coins
            score = self._score
            life = self._life
            self.add_coin()
            if coins < 49:
                assert self._coins == coins + 1 and self._life \
                    == life
            else:
                assert self._coins == 0 and self._life == life + 1
                break
            assert self._score == score + 250


    def test_add_score(self, point):
        '''Function to test add_score'''
        score = self._score
        self.add_score(point)
        assert self._score == score + point
        score = self._score
        self.add_score(point)
        assert self._score == score + point


    def test_add_kill(self):
        '''Function to test add_score'''
        kill = self._kills
        self.add_kill()
        assert self._kills == kill + 1


    def test_level_up(self):
        '''Function to test level up'''
        level = self._level
        self.level_up()
        assert self._level == level + 1


STATUS = TestStatus()
STATUS.test_init()
STATUS.test_add_coin()
STATUS.test_add_score(100 * randint(1, 9))
STATUS.test_add_score(randint(50, 500))
STATUS.test_add_kill()
#STATUS.test_level_up()
