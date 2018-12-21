import numpy as np
import matplotlib.pyplot as plt
import pygame as pg
import math

#==========================================================#
# FUNCTIONS:

def drag(density, velocity, coefficient, area):
    return 1/2 * density * velocity**2 * coefficient * area

def accelaration(force, mass):
    return force/mass

def GM_product(M, r):
    return (6.67259*M)/(r**2)
#==========================================================#

#==========================================================#
# GENERAL VALUES:
swidth = 1600
sheight = 900

air_density = 1.225
#==========================================================#

pg.init()
window = pg.display.set_mode((swidth, sheight))
pg.display.set_caption('We dem boys')


# box1 values:
box1_width = 40
box1_height = 40
mass1 = box1_width * box1_height
force1 = 1000
accel1 = accelaration(force1, mass1)
velx1 = 0
vely1 = 0
x1 = 50
y1 = 50

# UPDATE:
run = True
while run:
    pg.time.delay(5)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()

    #==========================================================#
    # GENERAL MOVEMENT:
    if keys[pg.K_LEFT]:
        velx1 -= accel1
    if keys[pg.K_RIGHT]:
        velx1 += accel1
    if keys[pg.K_UP]:
        vely1 -= accel1
    if keys[pg.K_DOWN]:
        vely1 += accel1

    if x1 <= 0 or x1 >= swidth - box1_width:
        velx1 = -velx1
    
    if y1 <= 0 or y1 >= sheight - box1_height:
        vely1 = -vely1
    #==========================================================#

    #==========================================================#
    # DRAG:
    if velx1 > 0:
        velx1 -= accelaration(drag(air_density, velx1, 1.05, box1_width), mass1)
    elif velx1 < 0:
        velx1 += accelaration(drag(air_density, velx1, 1.05, box1_width), mass1)
    if vely1 > 0:
        vely1 -= accelaration(drag(air_density, vely1, 1.05, box1_width), mass1)
    elif vely1 < 0:
        vely1 += accelaration(drag(air_density, vely1, 1.05, box1_width), mass1)
    #==========================================================#

    #==========================================================#
    # GRAVITY:
    #if y1 < sheight - box1_height:
    #    vely1 += GM_product(10000, (sheight - y1))
    #==========================================================#

    print(y1)

    x1 += velx1
    if y1 < sheight - box1_height:
        y1 += vely1

    window.fill((0,0,0))
    pg.draw.rect(window, (255, 0, 0), (x1, y1, box1_width, box1_height))
    pg.display.update()
    

pg.quit()