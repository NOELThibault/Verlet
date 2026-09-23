import pygame as pg
from utils import * 
from particle import *

# Initialize simulation
pg.init()
pg.display.set_caption( "Verlet" )
pg.display.set_mode( ( SCREEN_WIDTH, SCREEN_HEIGHT ) )
screen = pg.display.get_surface()

# Simulation variables
particles = [ Particle() ]
clock = pg.time.Clock()
deltaTime = 0
frameCount = 0
sumFPS = 0

for particle in particles :
    particle.addForce( pg.Vector2( 0, particle.mass * g ) ) # P = mg

# Main loop
run = True
while run :
    # Window management
    for event in pg.event.get() :
        if event.type == pg.QUIT :
            run = False

    screen.fill( BLACK )

    # Time handling
    deltaTime = clock.tick() / 1000 # deltaTime in seconds for computations
    # Don't show FPS every frame to get clearer numbers
    sumFPS += clock.get_fps()
    if frameCount % FPS_COMPUTATION_THRESHOLD == 0 :
        fps = int( sumFPS / FPS_COMPUTATION_THRESHOLD ) # Average of FPS measured after last print  
        print( f"FPS : { fps }" )
        sumFPS = 0

    # Particle handling
    for particle in particles :
        particle.update( deltaTime )
        particle.draw( screen )

    pg.display.flip()
    frameCount += 1

# Cleanup
pg.quit()
