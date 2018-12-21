import numpy as np
import matplotlib.pyplot as plt
import pygame as pg

pg.init()

win = pg.display.set_mode((2000, 2000))
pg.display.set_caption("Yaboi")

force1 = 1000
velx1 = 0
vely1 = 0
width1 = 30
height1 = 30
y1 = 235
x1 = 200
mass1 = width1 * height1
accel1 = force1 / mass1

force2 = 1000
velx2 = 0
vely2 = 0
width2 = 30
height2 = 30
y2 = 235
x2 = 235
mass2 = width2 * height2
accel2 = force2 / mass2

run = True
while run:
    pg.time.delay(50)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        velx1 -= accel1
    if keys[pg.K_RIGHT]:
        velx1 += accel1
    if keys[pg.K_UP]:
        vely1 -= accel1
    if keys[pg.K_DOWN]:
        vely1 += accel1
    
    if x1 <= 0 or x1 >= 500:
        velx1 = -1 * velx1
    
    if y1 <= 0 or y1 >= 500:
        vely1 = -vely1

    x1 += velx1
    y1 += vely1

    keys = pg.key.get_pressed()
    if keys[pg.K_a]:
        velx2 -= accel2
    if keys[pg.K_d]:
        velx2 += accel2
    if keys[pg.K_w]:
        vely2 -= accel2
    if keys[pg.K_s]:
        vely2 += accel2
        
    if x2 <= 0 or x2 >= 500:
        velx2 = -1 * velx2

    if y2 <= 0 or y2 >= 500:
        vely2 = -1 * vely2

    x2 += velx2
    y2 += vely2


    win.fill((0, 0, 0))
    pg.draw.rect(win, (255, 0, 0), (x1, y1, width1, height1))
    pg.draw.rect(win, (255, 0, 0), (x2, y2, width2, height2))
    pg.display.update()
pg.quit()
