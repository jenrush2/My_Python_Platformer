import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join
pygame.init()

pygame.display.set_caption("Platformer")

WIDTH, HEIGHT, = 1000, 800
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

def get_background(name):
    #load background image from assets
    image = pygame.image.load(join("assets", "Background", name))
    #get the width and height of image, ignore x and y
    _, _, width, height = image.get_rect()
    tiles = []

    #loop through how many tiles we need in each direction
    #width of screen integer divided by the width of one tile to get how many tiles
    #then add 1 more tile to make sure there are no gaps
    #same for height of screen
    for i in range(WIDTH // width +1):
        for j in range (HEIGHT // height +1):
            #denote the position of the top left hand corner of the current tile
            #continually moves each tile based on the for loop
            position = (i * width, j * height)
            tiles.append(position)

    return tiles, image

def draw(window, background, bg_image):
    #loop through every tile and draw background image at that position
    for tile in background:
        window.blit(bg_image, tile)
    
    #every frame clear screen and redraw
    pygame.display.update()

def main(window):
    clock = pygame.time.Clock()
    
    background, bg_image = get_background("Purple.png")

    run = True
    
    while run:
        #regulate frame rate across devices
        clock.tick(FPS)

        #allow exiting the game by clicking the x on the top right
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        draw(window, background, bg_image)

    pygame.quit()
    quit()

#only call the main function and call the game if we run the file directly
if __name__ == "__main__":
    main(window)