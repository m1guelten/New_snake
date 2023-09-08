import pytest
from snake import Snake
from runner import speed_game


@pytest.fixture(scope="function")
def snake(request):
    return Snake(request.param)


@pytest.mark.parametrize(
    ("snake", "tail", "result"),
    [
        (
            (120, 120),
            [{"x": 120, "y": 150}, {"x": 120, "y": 180}, {"x": 150, "y": 180}],
            40,
        ),
        (
            (120, 120),
            [
                {"x": 120, "y": 150},
                {"x": 120, "y": 150},
                {"x": 120, "y": 180},
                {"x": 150, "y": 180},
            ],
            30,
        ),
    ],
    indirect=["snake"],
)
def test_speed_game(snake, tail, result):
    snake.tail = tail

    assert speed_game(snake) == result
