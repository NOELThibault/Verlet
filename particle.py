import pygame as pg
from utils import *

_SIZE = 10

class Particle :

    def __init__( self ) :
        self.pos = MID_SCREEN + pg.Vector2( SPAWN_OFFSET, 0 )
        self.prev_pos = self.pos
        self.acc = pg.Vector2( 0, 0 )
        self.mass = 0.1 # 100 grams

        self.addForce( pg.Vector2( 0, self.mass * g ) ) # Always apply gravity

    def update( self, deltaTime ) :
        self.solveVerlet( deltaTime )

    def solveVerlet( self, deltaTime ) :
        temp = self.pos
        self.pos = 2 * self.pos - self.prev_pos + self.acc * deltaTime * deltaTime * SCALE
        self.prev_pos = temp
        # Constraint the particle to the simulation area
        direction = self.pos - MID_SCREEN
        dist = direction.length()
        if dist > SIMULATION_AREA - _SIZE :
            self.pos = MID_SCREEN + direction.normalize() * ( SIMULATION_AREA - _SIZE )

    def collide( self, other ) :
        direction = self.pos - other.pos
        dist = direction.length()
        collisionDist = 2 * _SIZE
        if 0 < dist and dist < collisionDist :
            recoil = direction.normalize() * ( collisionDist - dist ) / 2
            self.pos += recoil
            other.pos -= recoil

    def addForce( self, force ) :
        self.acc += force / self.mass

    def draw( self, surface ) :
        pg.draw.circle( surface, WHITE, self.pos, _SIZE )
