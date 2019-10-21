import pygame
import math
import sys
from random import choice
 
# Initialize the game engine
pygame.init()
 
# Define the colors and base position
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

CIRCLE_A = [512, 100]
CIRCLE_B = [100, 668]
CIRCLE_C = [924, 668]

START = [350, 500]

ALL_BALLS = []
ALL_BALLS.append(CIRCLE_A)
ALL_BALLS.append(CIRCLE_B)
ALL_BALLS.append(CIRCLE_C)
ALL_BALLS.append(START)

# Set the height and width of the screen
size = [1024, 768]
screen = pygame.display.set_mode(size)
 
def MOVE (coord):
    BASE = choice([CIRCLE_A, CIRCLE_B, CIRCLE_C])
    nx = int((BASE[0] + coord[0]) / 2)
    ny = int((BASE[1] + coord[1]) / 2)
    coord = [nx, ny]
    return (coord)

# Draw the Base
pygame.display.set_caption("Drawing the fractal")
screen.fill(BLACK)
for current in ALL_BALLS:
        pygame.draw.circle(screen, GREEN, current, 2)    

#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

while not done:

    clock.tick(100000)
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    pygame.draw.circle(screen, RED, START, 2)

    START = MOVE(START)

    pygame.display.flip()

pygame.quit()