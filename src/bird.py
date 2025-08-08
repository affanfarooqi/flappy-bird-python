import pygame as pg
from .settings import FLAP_STRENGTH, GRAVITY

class Bird:
    RADIUS = 14
    COLOR  = (40, 40, 40)

    def __init__(self, x, y):
        self.pos      = pg.Vector2(x, y)
        self.velocity = 0

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.pos.y    += self.velocity

    def draw(self, surf):
        pg.draw.circle(surf, self.COLOR, self.pos, self.RADIUS)

    @property
    def rect(self):
        return pg.Rect(self.pos.x - self.RADIUS,
                       self.pos.y - self.RADIUS,
                       self.RADIUS * 2,
                       self.RADIUS * 2)
