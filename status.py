from time import time
class Status:
    '''Store game Status'''
    def __init__(self):
        self._life = 3
        self._level = 1
        self._coins = 0
        self._score = 0
        self._time = 0
        self._kills = 0
        self._beginTime = time()*10

    def addCoin(self):
        self._coins += 1
        self._score += 1000
        if self._coins == 100:
            self._coins = 0
            self._life += 1

    def updateTime(self):
        pre = self._time
        self._time = int(time()*10 - self._beginTime)
        self._score += (self._time - pre)*10

    def addScore(self,point):
        self._score += point

    def addKill(self):
        self._kills += 1

    def die(self):
        pass

    def levelChange(self):
        pass

    def printStatus(self):
        print('Level = ',self._level,"\tScore = ",self._score,'\t Coins = ',self._coins,'\t Lives = ',self._life,'\t Time = ',self._time,'\t Kills = ',self._kills)
