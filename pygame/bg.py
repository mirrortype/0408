# -*- coding: utf-8 -*-
from ast import While
from shutil import which
import pygame
pygame.init()

screan_widch = 480
screan_height = 640
screan = pygame.display.set_mode((screan_widch, screan_height))

pygame.display.set_caption("똥피하기-코드플레이")

bg = pygame.image.load("pygame/source/bg.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screan.blit(bg, (0, 0))
    pygame.display.update()

pygame.quit()