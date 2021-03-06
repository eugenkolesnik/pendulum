import pygame
import math
import sys
from random import choice
 
# Initialize the game engine
pygame.init()
 
# Define the colors and base position
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

step = 2

# Set the height and width of the screen
size = [1024, 768]
screen = pygame.display.set_mode(size)
 
def move (coord):
    base = choice([base_a, base_b, base_c])
    dx = (coord[0] - base[0]) / step
    dy = (coord[1] - base[1]) / step
    nx = int(coord[0] - dx)
    ny = int(coord[1] - dy)
    coord = [nx, ny]
    return (coord)

# Draw the base
pygame.display.set_caption("Drawing the fractal")
screen.fill(black)
for current in all_base:
        pygame.draw.circle(screen, red, current, 2)    

#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

while not done:

    clock.tick(100000)
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                 done=True

# Draw the field
    colour = choice([red, green, blue, white])
    pygame.draw.circle(screen, red, start, 2)

    start = move(start)

    pygame.display.flip()

pygame.quit()