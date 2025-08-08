import random, pygame as pg
from .settings import HEIGHT, PIPE_GAP, PIPE_WIDTH, PIPE_SPEED

class PipePair:
    COLOR = (20, 20, 20)

    def __init__(self, x):
        self.x      = x
        self.top_h  = random.randint(40, HEIGHT - PIPE_GAP - 40)
        self.bottom_y = self.top_h + PIPE_GAP
        self.passed = False   # has the bird flown past this pair?

    def update(self):
        self.x -= PIPE_SPEED

    def draw(self, surf):
        # top pipe
        pg.draw.rect(surf, self.COLOR, (self.x, 0, PIPE_WIDTH, self.top_h))
        # bottom pipe
        pg.draw.rect(surf, self.COLOR, (self.x, self.bottom_y,
                                        PIPE_WIDTH, HEIGHT - self.bottom_y))

    @property
    def offscreen(self):
        return self.x + PIPE_WIDTH < 0

    @property
    def rects(self):
        top_rect    = pg.Rect(self.x, 0, PIPE_WIDTH, self.top_h)
        bottom_rect = pg.Rect(self.x, self.bottom_y, PIPE_WIDTH,
                              HEIGHT - self.bottom_y)
        return top_rect, bottom_rect
