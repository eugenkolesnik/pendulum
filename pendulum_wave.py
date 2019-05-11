import pygame
import math
import sys

pygame.init()

res_x = 1024
res_y = 768
ball_colour = 255, 0, 0
backgrount_colour = 0, 0, 0
ball_number = 35

screen = pygame.display.set_mode((res_x, res_y))
middle_x = int(res_x/2)

while True:
    for degree in range(3600):
        y = 10
        for n in range(ball_number):
            y += 22
            alfa = degree*(n+1)/10
            
            r = int((1 + math.sin(math.radians(alfa)))*255/2)
            g = 255 - int((1 + math.sin(math.radians(alfa)))*255/2)
            # b = int((1 + math.sin(math.radians(alfa)))*255/2)
            b = 100
            ball_colour = (r, g, b)
            
            x = int(middle_x + math.sin(math.radians(alfa))*150)
            pygame.draw.circle(screen, ball_colour, (x, y), 10)

            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

        pygame.display.update()
        pygame.time.wait(10)
        screen.fill(backgrount_colour)