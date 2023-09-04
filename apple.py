
import pygame as pg
from constants import SQUARE_WIDTH, SQUARE_HEIGHT


class Apple:
    def __init__(self, koord):
        self.x = koord[0]
        self.y = koord[1]
        self.eat = pg.Rect(self.x, self.y, SQUARE_WIDTH, SQUARE_HEIGHT)

    def draw(self, screen):
        pg.draw.rect(screen, "red", self.eat)
