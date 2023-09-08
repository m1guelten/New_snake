import pytest
from snake import Snake
from apple import Apple

from snake_collision import wall_collision, apple_collision


@pytest.fixture(scope="function")
def snake(request):
    return Snake(request.param)


@pytest.fixture(scope="function")
def apple(request):
    return Apple(request.param)


@pytest.mark.parametrize(
    ("snake", "result"),
    [
        ((120, 120), True),
        ((120, 1200), False),
        ((1200, 120), False),
        ((120, -120), False),
        ((-120, 120), False),
    ],
    indirect=["snake"],
)
def test_wall_collision(snake, result):
    assert wall_collision(snake) is result


@pytest.mark.parametrize(
    ("snake", "apple", "result"),
    [
        ((120, 120), (120, 120), True),
        ((120, 120), (140, 120), False),
        ((120, 120), (120, 140), False),
    ],
    indirect=["snake", "apple"],
)
def test_apple_collision(snake, apple, result):
    assert apple_collision(snake, apple) is result
