"""
Example file showing a basic pygame game loop
"""

import pygame

from apple import Apple
from constants import HEIGHT, START_SNAKE_X, START_SNAKE_Y, WIDTH
from snake import Snake
from snake_collision import apple_collision, wall_collision
from utils import generate_position

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
RUNNING = True

snake = Snake((START_SNAKE_X, START_SNAKE_Y))
apple = Apple(generate_position())

SNAKE_SPEED = 0
snake_vector = pygame.K_RIGHT
SNAKE_SPEED_LIMIT = 40
#
while RUNNING and snake.alive:
    #     # poll for events
    #     # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP and snake.vector != "DOWN":
                snake.vector = "UP"
            if event.key == pygame.K_DOWN and snake.vector != "UP":
                snake.vector = "DOWN"
            if event.key == pygame.K_LEFT and snake.vector != "RIGHT":
                snake.vector = "LEFT"
            if event.key == pygame.K_RIGHT and snake.vector != "LEFT":
                snake.vector = "RIGHT"

    SNAKE_SPEED += 1

    if apple_collision(snake, apple):
        snake.tail.append({"x": snake.coord_x, "y": snake.coord_y})
        GENERATE = True
        ran_x, ran_y = None, None
        while GENERATE:
            GENERATE = False
            ran_x, ran_y = generate_position()
            for item in snake.tail:
                if item == {"x": ran_x, "y": ran_y}:
                    GENERATE = True
            apple = Apple((ran_x, ran_y))

        apple = Apple(generate_position())

    if SNAKE_SPEED > SNAKE_SPEED_LIMIT:
        snake.move()
        snake.alive = wall_collision(snake)
        SNAKE_SPEED = 0

    if len(snake.tail) == 4:
        SNAKE_SPEED_LIMIT = 30
    elif len(snake.tail) == 9:
        SNAKE_SPEED_LIMIT = 20
    elif len(snake.tail) == 19:
        SNAKE_SPEED_LIMIT = 15
    elif len(snake.tail) > 28:
        SNAKE_SPEED_LIMIT = 10

    screen.fill("purple")

    snake.draw(screen)
    apple.draw(screen)
    pygame.display.flip()

    clock.tick(60)


pygame.quit()
