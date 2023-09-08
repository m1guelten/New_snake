"""
This module is for Snake template class
"""

import pygame as pg

from constants import SQUARE_HEIGHT, SQUARE_WIDTH


class Snake:
    """
    class Snake
    """

    def __init__(self, coord, tail=[]):
        self.coord_x = coord[0]
        self.coord_y = coord[1]
        self.head = pg.Rect(
            self.coord_x, self.coord_y, SQUARE_WIDTH - 1, SQUARE_HEIGHT - 1
        )
        self.tail = tail
        self.alive = True
        self.vector = "RIGHT"

    def draw(self, screen):
        """
        This func is a draw
        """
        pg.draw.rect(screen, "green", self.head)
        if len(self.tail) > 0:
            for one_tail in self.tail:
                pg.draw.rect(
                    screen,
                    "green",
                    pg.Rect(
                        one_tail["x"],
                        one_tail["y"],
                        SQUARE_WIDTH - 1,
                        SQUARE_HEIGHT - 1,
                    ),
                )

    def collision_myself(self):
        """
        func collision_myself
        """
        for item in self.tail:
            if item["x"] == self.coord_x and item["y"] == self.coord_y:
                return False
        return True

    def move(self):
        """
        func move
        """
        if len(self.tail) > 0:
            self.rewrite_tail()

        if self.vector == "UP":
            self.coord_y -= SQUARE_HEIGHT

        if self.vector == "DOWN":
            self.coord_y += SQUARE_HEIGHT

        if self.vector == "LEFT":
            self.coord_x -= SQUARE_WIDTH

        if self.vector == "RIGHT":
            self.coord_x += SQUARE_WIDTH
        self.alive = self.collision_myself()
        self.head = pg.Rect(
            self.coord_x, self.coord_y, SQUARE_WIDTH - 1, SQUARE_HEIGHT - 1
        )

    def rewrite_tail(self):
        """
        func rewrite_tail
        """
        for inx in range(0, len(self.tail)):
            if (inx + 1) == len(self.tail):
                self.tail[inx] = {"x": self.coord_x, "y": self.coord_y}
            else:
                self.tail[inx] = self.tail[inx + 1]
