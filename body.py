import pygame as pg

class Body(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([20, 20])
        self.image.fill([0, 0, 255])
        self.rect = self.image.get_rect()
