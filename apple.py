
import pygame as pg
from constants import SQUARE_WIDTH, SQUARE_HEIGHT


class Apple:
    def __init__(self, koord_x, koord_y):
        self.x = koord_x
        self.y = koord_y
        self.eat = pg.Rect(self.x, self.y, SQUARE_WIDTH, SQUARE_HEIGHT)

    def draw(self, screen):
        pg.draw.rect(screen, "red", self.eat)
