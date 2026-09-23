import pygame as pg
from utils import *

_SIZE = 10

class Particle :

    def __init__( self ) :
        self.pos = pg.Vector2( SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 )
        self.prev_pos = self.pos
        self.acc = pg.Vector2( 0, 0 )
        self.mass = 0.001 # 1 gram

    def update( self, deltaTime ) :
        self.solveVerlet( deltaTime )
        self.constraints()

    def solveVerlet( self, deltaTime ) :
        temp = self.pos
        self.pos = 2 * self.pos - self.prev_pos + self.acc * deltaTime * deltaTime * SCALE
        self.prev_pos = temp

    def addForce( self, force ) :
        self.acc += force / self.mass

    def constraints( self ) :
        # Constraint the particle to the screen
        self.pos = pg.Vector2( max( self.pos[ 0 ], 0 ), max( self.pos[ 1 ], 0 ) )
        self.pos = pg.Vector2( min( self.pos[ 0 ], SCREEN_WIDTH - _SIZE / 2 ), min( self.pos[ 1 ], SCREEN_HEIGHT - _SIZE / 2 ) )

    def draw( self, surface ) :
        pg.draw.circle( surface, WHITE, self.pos, _SIZE )
