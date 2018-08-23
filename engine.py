from background import *
from enemy import *
from board import *
from obstacles import *
from mario import *
from user import *
from hurdles import *
from coins import *
import colorama

OFFSET = 0
board = Board(LENGTH,BREADTH)
board.display(OFFSET)

#system('aplay ./Sounds/clap.wav')
#system('ls')

for i in range(randint(4,7)):
    cloud = Cloud(board)
    cloud.draw()
for i in range(randint(3,6)):
    bush = Bush(board)
    bush.draw()

mario = Mario(FLOOR-3,5,board)
mario.update()
board.display(OFFSET)


enemy = Pakistan(FLOOR-2,26,board);
enemy.update()
board.display(OFFSET)

print(enemy.move_right(1))
print(enemy.move_right(2))
print(enemy.move_right(3))
print(enemy.move_left(6))
board.display(OFFSET)


threePipes = ThreePipes(70,board)
board.display(OFFSET)

twoPipes = TwoPipes(130,board)
board.display(OFFSET)

brickJungle = BrickJungle(10,board)
board.display(OFFSET)

while True:
    board.updateTime()
    for i in USED_COINS:
        i.restore()
    for i in allEnemies:
        i.selfMove(1)
    mario.gravity(2)
    if(mario.point.y - OFFSET > 50):
        OFFSET += 15
    if(mario.point.y - OFFSET < 0):
        OFFSET -= 18
    ch = getInput()
    if ch == 'a':
        mario.move_left(1)
        #mario.move_left(1)
    elif ch == 'd':
        mario.move_right(1)
        #mario.move_right(1)
    elif ch == 'q':
        quit()
    elif ch == 'w':
        mario.jump(6)
    for i in COINS:
        i.check()
    board.display(OFFSET)
