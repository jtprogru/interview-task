import pytest

from tasks.task0019 import solution


@pytest.mark.parametrize(
    "x, result",
    [(123, 321), (-123, -321), (120, 21)],
)
def test_task0019_solution(x, result):
    assert solution(x) == result
