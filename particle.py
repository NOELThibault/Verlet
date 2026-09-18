import pygame as pg
from utils import *

_SIZE = 1

class Particle :

    def __init__( self ) :
        self.pos = pg.Vector2( 0, 0 )
        self.prev_pos = pg.Vector2( 0, 0 )
        self.acc = pg.Vector2( 0, 0 )

    def update( self, deltaTime ) :
        self.pos = 2 * self.pos - self.prev_pos + self.acc * deltaTime * deltaTime

    def addForce( self, force ) :
        self.acc += force

    def draw( self, surface ) :
        pg.draw.circle( surface, WHITE, self.pos, _SIZE )
