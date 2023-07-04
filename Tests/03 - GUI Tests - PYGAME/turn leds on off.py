# GUI with 2 red LEDs, 2 green LEDs, 2 yellow LEDs and 2 blue LEDs. Also, 1 RGB LED.

import pygame
from pygame.locals import *
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('GUI')

# red LEDs
pygame.draw.circle(screen, "red", (100, 100), 40)
pygame.draw.circle(screen, "red", (100, 200), 40)

# green LEDs
pygame.draw.circle(screen, "green", (200, 100), 40)
pygame.draw.circle(screen, "green", (200, 200), 40)

# yellow LEDs
pygame.draw.circle(screen, "yellow", (300, 100), 40)
pygame.draw.circle(screen, "yellow", (300, 200), 40)

# blue LEDs
pygame.draw.circle(screen, "blue", (400, 100), 40)
pygame.draw.circle(screen, "blue", (400, 200), 40)

# RGB LED
pygame.draw.circle(screen, "red", (500, 100), 40)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        # if key is pressed, toggle the state of the LED: on or off
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                if pygame.draw.circle(screen, "red", (100, 100), 40):
                    pygame.draw.circle(screen, "gray", (100, 100), 40)
                else:
                    pygame.draw.circle(screen, "red", (100, 100), 40)
            
            if event.key == pygame.K_g:
                if pygame.draw.circle(screen, "green", (200, 100), 40):
                    pygame.draw.circle(screen, "gray", (200, 100), 40)
                else:
                    pygame.draw.circle(screen, "green", (200, 100), 40)
            
            if event.key == pygame.K_y:
                if pygame.draw.circle(screen, "yellow", (300, 100), 40):
                    pygame.draw.circle(screen, "gray", (300, 100), 40)
                else:
                    pygame.draw.circle(screen, "yellow", (300, 100), 40)

            if event.key == pygame.K_b:
                if pygame.draw.circle(screen, "blue", (400, 100), 40):
                    pygame.draw.circle(screen, "gray", (400, 100), 40)
                else:
                    pygame.draw.circle(screen, "blue", (400, 100), 40)

            if event.key == pygame.K_x:
                if pygame.draw.circle(screen, "red", (500, 100), 40):
                    pygame.draw.circle(screen, "gray", (500, 100), 40)
                else:
                    pygame.draw.circle(screen, "red", (500, 100), 40)
    pygame.display.update()
