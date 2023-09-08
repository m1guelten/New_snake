import pytest
from snake import Snake


@pytest.fixture(scope="function")
def snake(request):
    return Snake(request.param)


@pytest.mark.parametrize(
    ("snake", "result"), [((120, 120), True), ((150, 120), False)], indirect=["snake"],)
def test_collision_myself(snake, result):
    snake.tail = [
        {"x": 120, "y": 150},
        {"x": 120, "y": 180},
        {"x": 150, "y": 180},
        {"x": 150, "y": 150},
        {"x": 150, "y": 120}
    ]
    assert snake.collision_myself() is result


@pytest.mark.parametrize(
    ("snake", "vector", "result"), [
        ((120, 120), "DOWN", (120, 150)),
        ((120, 120), "UP", (120, 90)),
        ((120, 120), "LEFT", (90, 120)),
        ((120, 120), "RIGHT", (150, 120))
    ], indirect=["snake"],)
def test_move(snake, vector, result):
    snake.vector = vector
    snake.move()
    assert snake.coord_x == result[0] and snake.coord_y == result[1]

@pytest.mark.parametrize(
    ("snake", "tail", "result"), [
        ((180, 180), [{"x": 120, "y": 150}, {"x": 120, "y": 180}, {"x": 150, "y": 180}],
        [{"x": 120, "y": 180}, {"x": 150, "y": 180}, {"x": 180, "y": 180}]),
        ((210, 180), [{"x": 120, "y": 150}, {"x": 120, "y": 180}, {"x": 150, "y": 180}, {"x": 180, "y": 180}],
        [{"x": 120, "y": 180}, {"x": 150, "y": 180}, {"x": 180, "y": 180}, {"x": 210, "y": 180},])
        ], indirect=["snake"])
def test_rewrite_tail(snake, tail, result):
    snake.tail = tail
    snake.rewrite_tail()
    assert snake.tail == result
