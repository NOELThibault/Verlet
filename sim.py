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

# Main loop
run = True
while run :
    # Window management
    for event in pg.event.get() :
        if event.type == pg.QUIT :
            run = False
        if event.type == pg.KEYDOWN :
            if event.key == pg.K_ESCAPE :
                run = False
            if event.key == pg.K_SPACE :
                particles.append( Particle() )
                print( f"New number of particles : { len( particles ) }" )

    screen.fill( BLACK )
    pg.draw.circle( screen, GREY, MID_SCREEN, SIMULATION_AREA )

    # Time handling
    deltaTime = clock.tick() / 1000 # deltaTime in seconds for computations
    # Don't show FPS every frame to get clearer numbers
    sumFPS += clock.get_fps()
    if frameCount % FPS_COMPUTATION_THRESHOLD == 0 :
        fps = int( sumFPS / FPS_COMPUTATION_THRESHOLD ) # Average of FPS measured after last print  
        print( f"FPS : { fps }" )
        sumFPS = 0

    # Particle handling
    subDeltaTime = deltaTime / SIMULATION_SUBSTEPS
    for i in range( SIMULATION_SUBSTEPS ) :
        for particle in particles :
            particle.update( subDeltaTime )
            for other in particles :
                particle.collide( other )
            particle.draw( screen )

    pg.display.flip()
    frameCount += 1

# Cleanup
pg.quit()
