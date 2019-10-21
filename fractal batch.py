import pygame
import math
import sys
from random import choice
 
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
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
 
pygame.display.set_caption("Drawing the fractal")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

def MOVE (coord):
    BASE = choice([CIRCLE_A, CIRCLE_B, CIRCLE_C])
    nx = int((BASE[0] + coord[0]) / 2)
    ny = int((BASE[1] + coord[1]) / 2)
    coord = [nx, ny]
    return (coord)
 
while not done:
 
    # Run the loop 10k times per second.
    clock.tick(10000)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop    
     
    # Clear the screen and set the screen background
    screen.fill(BLACK)
 
    # Draw the field
    for current in ALL_BALLS:
        pygame.draw.circle(screen, RED, current, 2)    

    # Create next step field
    START = MOVE(START)
    ALL_BALLS.append(START)
    
    # update the screen
    pygame.display.flip()

pygame.quit()