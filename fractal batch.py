import pygame
import math
import sys
from random import choice
 
# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
black = (  0,   0,   0)
white = (255, 255, 255)
blue =  (  0,   0, 255)
green = (  0, 255,   0)
red =   (255,   0,   0)

base_a = [512, 100]
base_b = [100, 668]
base_c = [924, 668]
start = [350, 500]

all_base = []
all_base.append(base_a)
all_base.append(base_b)
all_base.append(base_c)
all_base.append(start)

step = 2

# Set the height and width of the screen
size = [1024, 768]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Drawing the fractal")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

def move (coord):
    base = choice([base_a, base_b, base_c])
    
    maxx = max(base[0], coord[0])
    minx = min(base[0], coord[0])
    dx = (maxx - minx) / step

    maxy = max(base[1], coord[1])
    miny = min(base[1], coord[1])
    dy = (maxy - miny) / step

    if coord[0] >= base[0]:
        nx = int(coord[0] - dx)
    else:
        nx = int(coord[0] + dx)
    
    if coord[1] >= base[1]:
        ny = int(coord[1] - dy)
    else:
        ny = int(coord[1] + dy)
    
    coord = [nx, ny]
    return (coord)

while not done:
 
    # Run the loop 10k times per second.
    clock.tick(10000)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop    
     
    # Clear the screen and set the screen background
    screen.fill(black)
 
    # Draw the field
    for current in all_base:
        pygame.draw.circle(screen, red, current, 2)    

    # Create next step field
    start = move(start)
    all_base.append(start)
    
    # update the screen
    pygame.display.flip()

pygame.quit()