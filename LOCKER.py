# JUMPING STARTING VALUES:
JUMP = False
j_height_0 = 0
jump_i = 0

#==========================================================#
# JUMPING:
height = 0
if jump_i >= 50:
    jump_i += 1
    JUMP = False
if jump_i == 70:
    jump_i = 0
if keys[pg.K_SPACE] and JUMP == False and jump_i == 0:
    JUMP = True
if JUMP == True:
    j_height_1 = (-0.02*(jump_i**2) + jump_i) * 10
    delta = j_height_1 - j_height_0
    y -= delta
    j_height_0 = j_height_1
    jump_i += 1
#==========================================================#