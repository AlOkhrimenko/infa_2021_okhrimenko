import pygame
import pygame.freetype
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 600))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball1():
    """
    Print new ball in random position
    """
    global x, y, r
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    
def new_ball2():
    """
    Print new ball in random position
    """
    global a, b, l, Vx, Vy, color
    a = randint(100,700)
    b = randint(100,500)
    l = randint(30,50)
    Vx = randint(-10,10)
    Vy = randint(-10,10)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (a, b), l)
    

def click(event):
    print(x, y, r)

    
def click(event):
    print(a, b, l)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
score = 0
kill = 0 


new_ball2()
while not finished:
    clock.tick(FPS)
    if kill == 1:
        new_ball2()
        kill = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:        
            x1 = event.pos[0]
            y1 = event.pos[1]
            if  (x1 - a)**2 + (y1 - b)**2 - l**2 <= 0 :
                #(x1 - x)**2 + (y1 - y)**2 - r**2 <= 0 or
                score+=1
                kill = 1
    if kill == 1:
        continue
    f1 = pygame.freetype.Font(None, 36)
    text1 = f1.render_to(screen,(100,50) 
                         , f'Your score:{score}'
                         , (255, 165, 50))
    a += Vx
    b += Vy
    if a >= 800 - l:
        Vx = -Vx
        circle(screen, color, (800 - l, b) , l )
    elif a <= l:
        Vx = -Vx
        circle(screen, color, (l, b) , l )
    elif b >= 600 - l:
        Vy = -Vy
        circle(screen, color, (a, 600 - b) , l )
    elif b <= l:
        Vy = -Vy
        circle(screen, color, (a, l) , l )
    else:
        circle(screen, color, (a, b) , l )
    

   

   
    pygame.display.update()
    screen.fill(BLACK)

    
    
pygame.quit()