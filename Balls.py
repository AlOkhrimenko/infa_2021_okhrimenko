import pygame.freetype
from pygame.draw import *
from random import randint

"""
Catch the ball <3 
The program reads the player's name, after which the game window opens. On the playing field is created
from 3 to 10 balls in random places with a random radius and speed, and from 3 to 7 squares
in random places with a random side and speed. The task is to click on the ball or square.
If the ball is hit, 1 point is given, if the square is hit, 5 is given, but the square is permanently
acquires a random speed. If the ball hits the wall 10 times, it disappears,
if the square hits the wall 6 times, it disappears. The game ends when all the balls and
the squares will disappear. You can exit the game by pressing the ESCAPE key. The player's account with his name is recorded
to the scoreboard.txt file in the same directory as the game file. If there is no such file, it is automatically created.
"""

#player's nickname 
print("Print your name: ")
name = str(input())
pygame.init()

FPS = 60
screen = pygame.display.set_mode((1400, 700))

#COLORS
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    """
    The function calculates random ball coordinates, radius, axis velocities and color
    :return: returns a list of the above values
    """
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    Vx = randint(-20, 20)
    Vy = randint(-20, 20)
    color = COLORS[randint(0, 5)]
    return [x, y, r, Vx, Vy, color, 0, 0]

def new_kube():
    """
    The function calculates the random coordinates of the square, the length of the side, the speed along the axes and the color
    :param V: speed multiplier (random)
    :return: returns a list of the above values
    """
    x = randint(100, 700)
    y = randint(100, 500)
    a = randint(40, 60)
    Vx = randint(-15, 15)
    Vy = randint(-15, 15)
    color = COLORS[randint(0, 5)]
    return [x, y, a, Vx+V, Vy+V, color, 0, 0]


pygame.display.update()
clock = pygame.time.Clock()
score = 0
finished = False
f1 = pygame.freetype.Font(None, 36)

#Calculating the number of balls and squares
V = randint(-10,10)
n = randint(3, 8)
m = randint(3, 11)
A = [new_ball() for i in range(1, m)]
B = [new_kube() for k in range(1, n)]

#Initial drawing of shapes
for el in A:
    circle(screen, el[5], (el[0], el[1]), el[2])
for el in B:
    rect(screen, el[5], (el[0]-el[2], el[1]-el[2], 2*el[2], 2*el[2]))

#Main loop
while not finished:
    clock.tick(FPS)
    click_x = 0
    click_y = 0
    for event in pygame.event.get():
        V = randint(-8,8)
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #Reading mouse coordinates
            click_x = event.pos[0]
            click_y = event.pos[1]
        elif event.type == pygame.KEYDOWN:
            #Exit by button ESCAPE
            if event.key == pygame.K_ESCAPE:
                finished = True
    for el in A:
        #Ball hit test and scoring
        if (el[0]-click_x)**2+(el[1]-click_y)**2 <= el[2]**2:
            el[6] = 1
            score += 1
        if el[7] >= 10:
            el[6] = 1
        el[0] += el[3]
        el[1] += el[4]
        #Drawing a new ball and counting the number of hits against the wall
        if el[6] == 0:
            if el[0] >= 1400 - el[2]:
                el[3] = (-1)*el[3]
                el[7] += 1
                circle(screen, el[5], (1400 - el[2], el[1]), el[2])
            elif el[0] <= el[2]:
                el[3] = (-1)*el[3]
                el[7] += 1
                circle(screen, el[5], (el[2], el[1]), el[2])
            if el[1] >= 700 - el[2]:
                el[4] = (-1)*el[4]
                el[7] += 1
                circle(screen, el[5], (el[0], 700 - el[2]), el[2])
            elif el[1] <= el[2]:
                el[4] = (-1)*el[4]
                el[7] += 1
                circle(screen, el[5], (el[0], el[2]), el[2])
            else:
                circle(screen, el[5], (el[0], el[1]), el[2])
    #Creation of a new ball by killing an existing one, provided that the ball hit the wall no more than 9 times
    for i in range(0, m-1):
        if A[i][6] == 1 and A[i][7] < 10:
            A[i] = new_ball()
    for el in B:
        #Square hit test and scoring
        if (el[0]-click_x)**2+(el[1]-click_y)**2 <= el[2]**2:
            el[6] = 1
            score += 5
            #V += 1
        if el[7] >= 6:
            el[6] = 1
        el[0] += el[3]
        el[1] += el[4]
        #Drawing a square and counting the number of hits against the wall
        if el[6] == 0:
            if el[0] >= 1400 - el[2]:
                el[3] = (-1)*el[3]
                el[7] += 1
                rect(screen, el[5], (1400 - 2*el[2], el[1]-el[2], 2*el[2], 2*el[2]))
            elif el[0] <= el[2]:
                el[3] = (-1)*el[3]
                el[7] += 1
                rect(screen, el[5], (0, el[1]-el[2], 2*el[2], 2*el[2]))
            if el[1] >= 700 - el[2]:
                el[4] = (-1)*el[4]
                el[7] += 1
                rect(screen, el[5], (el[0]-el[2], 700 - 2*el[2], 2*el[2], 2*el[2]))
            elif el[1] <= el[2]:
                el[4] = (-1)*el[4]
                el[7] += 1
                rect(screen, el[5], (el[0]-el[2], 0, 2*el[2], 2*el[2]))
            else:
                rect(screen, el[5], (el[0]-el[2], el[1]-el[2], 2*el[2], 2*el[2]))
    #Creation of a new square when killing an existing one, provided that the square hit the wall no more than 5 times
    for i in range(0, n-1):
        if B[i][6] == 1 and B[i][7] < 6:
            B[i] = new_kube()
    #Account withdrawal
    text1 = f1.render_to(screen, (20, 20), f'Your score: {score}', (180, 0, 0))
    pygame.display.update()
    screen.fill(BLACK)
#Recording the player's nickname and account to the file
f = open('scoreboard.txt', 'a')
f.write('Player: ' + name + ' scored ' + str(score) + ' points \n')
f.close()

pygame.quit()
