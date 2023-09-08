"""
this module is class apple
"""
import pygame as pg

from constants import SQUARE_HEIGHT, SQUARE_WIDTH


class Apple:
    """
    coord (coord_x - координата по х, coord_y - координата по у)
    """

    def __init__(self, coord):
        self.coord_x = coord[0]
        self.coord_y = coord[1]
        self.eat = pg.Rect(self.coord_x, self.coord_y, SQUARE_WIDTH, SQUARE_HEIGHT)

    def draw(self, screen):
        """
        func draw (де саме)
        """
        pg.draw.rect(screen, "red", self.eat)
