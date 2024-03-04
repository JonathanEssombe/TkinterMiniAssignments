import pygame
import time
import math

# Initializing images
GRASS = pygame.image.load('grass.jpg')
track = pygame.image.load('track.png')

TRACK_BORDER = pygame.image.load('track-border.png')
FINISH = pygame.image.load('finish.png')

RED_CAR = pygame.image.load('red-car.png')
GREEN_CAR = pygame.image.load('green-car.png')

# height and width from the track image we initialized
WIDTH, HEIGHT = track.get_width(), track.get_height()

# Initialize and interactive window
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Title of the window created
pygame.display.set_caption('Racing Game!')

# keep the program running unless it is closed
run = True

while run:
    for event in pygame.event.get():
        # Checks if user closes window
        if event.type == pygame.QUIT:
            run = False
            break

pygame.quit()
