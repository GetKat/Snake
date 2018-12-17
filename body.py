import pygame as pg
import os

path = os.path.dirname(os.path.abspath(__file__))

class Body(pg.sprite.Sprite):
    # sprite sheets da cobrinha

    # cabeca
    _IMG_HEAD_UP = pg.image.load(path + "/images/head_up.png")
    _IMG_HEAD_DOWN = pg.image.load(path + "/images/head_down.png")
    _IMG_HEAD_LEFT = pg.image.load(path + "/images/head_left.png")
    _IMG_HEAD_RIGHT = pg.image.load(path + "/images/head_right.png")

    # corpo
    _IMG_BODY_VERTICAL = pg.image.load(path + "/images/body_vertical.png")
    _IMG_BODY_HORIZONTAL = pg.image.load(path + "/images/body_horizontal.png")
    # corpo com curva
    _IMG_BODY_TOP_LEFT = pg.image.load(path + "/images/body_top_left.png")
    _IMG_BODY_TOP_RIGHT = pg.image.load(path + "/images/body_top_right.png")
    _IMG_BODY_RIGHT_BOTTOM = pg.image.load(path + "/images/body_right_bottom.png")
    _IMG_BODY_LEFT_BOTTOM = pg.image.load(path + "/images/body_left_bottom.png")

    # rabo
    _IMG_TAIL_UP = pg.image.load(path + "/images/tail_up.png")
    _IMG_TAIL_DOWN = pg.image.load(path + "/images/tail_down.png")
    _IMG_TAIL_LEFT = pg.image.load(path + "/images/tail_left.png")
    _IMG_TAIL_RIGHT = pg.image.load(path + "/images/tail_right.png")

    def __init__(self, x = 0, y = 0):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([20, 20])
        self.image.fill([0, 0, 255])
        self.rect = self.image.get_rect()
        self.rect.y = 20 * y
        self.rect.x = 20 * x