
# basic pygame hello world

import pygame
from pygame.locals import *
import sys


pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Hello World!')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
