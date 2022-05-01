import json
import numpy as np

# Import and initialize the pygame library
import pygame as pg

pg.init()

with open('data.json', 'r') as data:
    all_data = json.load(data)

# Screen width and height
SCREEN_WIDTH = all_data['screen_size'][0]
SCREEN_HEIGHT = all_data['screen_size'][1]

# Map width and height
MAP_WIDTH = all_data['map_size'][0]
MAP_HEIGHT = all_data['map_size'][1]

# Scale width and height
SCALE_WIDTH = (SCREEN_WIDTH * 0.9) / MAP_WIDTH
SCALE_HEIGHT = (SCREEN_HEIGHT * 0.9) / MAP_HEIGHT

# Set up the drawing window
screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Load iamges
img_r = pg.image.load('red.png').convert()
img_r = pg.transform.smoothscale(img_r, (SCALE_WIDTH, SCALE_HEIGHT))
img_b = pg.image.load('blue.png').convert()
img_b = pg.transform.smoothscale(img_b, (SCALE_WIDTH, SCALE_HEIGHT))
img_y = pg.image.load('yellow.png').convert()
img_y = pg.transform.smoothscale(img_y, (SCALE_WIDTH, SCALE_HEIGHT))
img_w = pg.image.load('white.png').convert()
img_w = pg.transform.smoothscale(img_w, (SCALE_WIDTH, SCALE_HEIGHT))
img_next = pg.image.load('next.png').convert()
img_next = pg.transform.smoothscale(img_next, (SCREEN_WIDTH * 0.1, SCREEN_HEIGHT * 0.1))

# The information of cube
ground = all_data['data']


# Get the index of pestrians
def getPedestrians(d_matrix):
    pedestrians = list()
    w, h = np.shape(d_matrix)
    for i in range(w):
        for j in range(h):
            if (d_matrix[i][j] == 1):
                pedestrians.append((i, j))
    return pedestrians

# Change the position of pedestrians
def movePedestrians(list, d_matrix):
    for (i, j) in list:
        d_matrix[i][j] = 1
    return d_matrix


# Run until the user asks to quit
running = True
while running:

    # Fill the backgroud with white
    screen.fill((255, 255, 255))

    # Draw the button
    screen.blit(img_next, (MAP_WIDTH * SCALE_WIDTH, MAP_HEIGHT * SCALE_HEIGHT))

    # Draw the map, 1 for pedestrain, 2 for obstacle, 3 for target, 0 for road
    for i in range(MAP_WIDTH):
        for j in range(MAP_HEIGHT):

            pos = (i * SCALE_WIDTH, j * SCALE_HEIGHT)

            if (ground[i][j] == 1):
                screen.blit(img_r, pos)
            elif (ground[i][j] == 2):
                screen.blit(img_y, pos)
            elif (ground[i][j] == 3):
                screen.blit(img_b, pos)
            else:
                screen.blit(img_w, pos)

    # Did the user click the window close button?
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            position = pg.mouse.get_pos()
            print(position)

    # Flip the display
    pg.display.flip()

# Done! Time to quit
pg.quit()
