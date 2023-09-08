"""
snake_collision
"""

from apple import Apple
from constants import HEIGHT, WIDTH
from snake import Snake


def wall_collision(snake: Snake) -> bool:
    """
    func wall_collision
    """
    coord_x, coord_y = snake.head.x, snake.head.y
    if coord_x >= WIDTH or coord_x < 0 or coord_y >= HEIGHT or coord_y < 0:
        return False
    return True


def apple_collision(snake: Snake, apple: Apple) -> bool:
    """
    func apple_collision
    """
    snake_x, snake_y = snake.head.x, snake.head.y
    apple_x, apple_y = apple.coord_x, apple.coord_y
    if apple_x == snake_x and apple_y == snake_y:
        return True
    return False
