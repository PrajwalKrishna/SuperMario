'''Test all functions related to status class'''
from status import Status

#class Status(Status):
#    '''Class for testing status functions'''

# def test_init():
#     '''Check constuction'''
#     STATUS = Status()
#     assert STATUS._life == 3
#     assert STATUS._life == 3
#     assert STATUS._level == 1
#     assert STATUS._coins == 0
#     assert STATUS._score == 0
#     assert STATUS._time == 0
#     assert STATUS._kills == 0


# def test_add_coin():
#     '''Function to test add_coin'''
#     STATUS = Status()
#     while True:
#         coins = STATUS._coins
#         score = STATUS._score
#         life = STATUS._life
#         STATUS.add_coin()
#         if coins < 49:
#             assert STATUS._coins == coins + 1 and STATUS._life == life
#         else:
#             assert STATUS._coins == 0 and STATUS._life == life + 1
#             break
        # assert STATUS._score == score + 250

def test_add_score():
    '''Function to test add_score'''
    point = 100
    STATUS = Status()
    score = STATUS._score
    STATUS.add_score(point)
    assert STATUS._score == score + point
    point = 300
    score = STATUS._score
    STATUS.add_score(point)
    assert STATUS._score == score + point
#
#
# def test_add_kill():
#     '''Function to test add_score'''
#     STATUS = Status()
#     kill = STATUS._kills
#     STATUS.add_kill()
#     assert STATUS._kills == kill + 1
#
# '''def test_level_up():
#     Function to test add_score
#     STATUS = Status()
#     level = STATUS._level
#     STATUS.level_up()
#     assert STATUS._level == level + 1
# '''
#
# #STATUS = Status()
# #STATUS.test_init()
# #STATUS.test_add_coin()
# #STATUS.test_add_score(100)
# #STATUS.test_add_score(200)
# #STATUS.test_add_kill()
# #STATUS.test_level_up()
