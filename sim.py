import pygame as pg
from utils import * 
from particle import *

# Initialize simulation
pg.init()
pg.display.set_caption( "Verlet" )
pg.display.set_mode( ( SCREEN_WIDTH, SCREEN_HEIGHT ) )
surface = pg.Surface( ( SCREEN_WIDTH, SCREEN_HEIGHT ) )

# Simulation variables
particles = [ Particle() ]
clock = pg.time.Clock()
deltaTime = clock.tick()
frameCount = 0
sumFPS = 0

# Main loop
run = True
while run :
    # Window management
    for event in pg.event.get() :
        if event.type == pg.QUIT :
            run = False

    surface.fill( BLACK )

    # Time handling
    deltaTime = clock.tick() / 1000.0 # deltaTime in seconds for computations
    sumFPS += clock.get_fps()
    if frameCount % FPS_COMPUTATION_THRESHOLD == 0 :
        fps = int( sumFPS / FPS_COMPUTATION_THRESHOLD )
        print( f"FPS : { fps }" )
        sumFPS = 0

    # Particle handling
    for particle in particles :
        particle.update( deltaTime )
        particle.draw( surface )

    pg.display.flip()
    frameCount += 1

# Cleanup
pg.quit()
