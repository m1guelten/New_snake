
"""
Example file showing a basic pygame game loop
"""

import random

import pygame

from apple import Apple
from constants import (
    HEIGHT,
    NUM_X,
    NUM_Y,
    SQUARE_HEIGHT,
    SQUARE_WIDTH,
    START_SNAKE_X,
    START_SNAKE_Y,
    WIDTH,
)
from snake import Snake
from snake_collision import wall_collision

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
running = True

snake = Snake(START_SNAKE_X, START_SNAKE_Y)
apple = Apple(
    SQUARE_WIDTH * random.choice(range(NUM_X)),
    SQUARE_HEIGHT * random.choice(range(NUM_Y)),
)


while running and snake.alive:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP and snake.vector != "DOWN":
                snake.vector = "UP"
            if event.key == pygame.K_DOWN and snake.vector != "UP":
                snake.vector = "DOWN"
            if event.key == pygame.K_LEFT and snake.vector != "RIGHT":
                snake.vector = "LEFT"
            if event.key == pygame.K_RIGHT and snake.vector != "LEFT":
                snake.vector = "RIGHT"
            snake.move()
        wall_collision(snake)

    if snake.x == apple.x and snake.y == apple.y:
        snake.tail.append({"x": snake.x, "y": snake.y})
        apple = Apple(
            SQUARE_WIDTH * random.choice(range(NUM_X)),
            SQUARE_HEIGHT * random.choice(range(NUM_Y)),
        )
    screen.fill("purple")
    snake.draw(screen)
    apple.draw(screen)
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60


pygame.quit()