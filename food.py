import pygame as pg
import random
import os

PATH = os.path.dirname(os.path.abspath(__file__))

class Food(pg.sprite.Sprite):
    _IMG_FOOD = pg.image.load(PATH + "/images/food.png")

    def __init__(self, game_width, game_height):
        pg.sprite.Sprite.__init__(self)
        self.image = Food._IMG_FOOD
        self.rect = self.image.get_rect()

        # calcula a posicao da comida na tela aleatoriamente
        # a diminuicao serve para arredondar pro menor multiplo de 20
        x = random.randint(0, game_width // 20 - 1)
        x *= 20
        y = random.randint(0, game_height // 20 - 1)
        y *= 20

        self.rect.x = x
        self.rect.y = y
         