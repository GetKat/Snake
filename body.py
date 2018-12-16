import pygame as pg
import os

path = os.path.dirname(os.path.abspath(__file__))

class Body(pg.sprite.Sprite):
    # sprite sheets da cobrinha
    _IMG_HEAD = pg.image.load(path + "/images/head_left.png")
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([20, 20])
        self.image.fill([0, 0, 255])
        self.rect = self.image.get_rect()
