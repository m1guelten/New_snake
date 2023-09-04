from snake import Snake

from constants import WIDTH, HEIGHT


def wall_collision(snake: Snake) -> bool:
    x, y = snake.head.x, snake.head.y
    if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
        return False
    return True