# -*- coding: utf-8 -*-
from ast import While
from ctypes import sizeof
from shutil import which
import pygame
pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("똥피하기-코드플레이")

bg = pygame.image.load("pygame/source/bg.png")

character = pygame.image.load("pygame/source/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xPos = (screen_width / 2) - (character_width / 2)
character_yPos = screen_height - character_height

to_x = 0
to_y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                to_x -= 1
            elif event.key == pygame.K_d:
                to_x += 1
            elif event.key == pygame.K_w:
                to_y -= 1
            elif event.key == pygame.K_s:
                to_y += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                to_x = 0
            elif event.key == pygame.K_w or event.key ==pygame.K_s:
                to_y = 0
            
    character_xPos += to_x
    character_yPos += to_y

    if character_xPos < 0:
        character_xPos = 0
    elif character_xPos > screen_width - character_width:
        character_xPos = screen_width - character_width
        
    if character_yPos < 0:
        character_yPos = 0
    elif character_yPos > screen_height - character_height:
        character_yPos = screen_height - character_height

    screen.blit(bg, (0, 0))
    screen.blit(character, (character_xPos, character_yPos))

    pygame.display.update()

pygame.quit()