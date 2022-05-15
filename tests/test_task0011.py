import pytest

from tasks.task0011 import solution


@pytest.mark.parametrize(
    "m, n, result",
    [
        (7, 3, 28),
        (3, 2, 3),
        (4, 4, 20),
        (2, 2, 2),
        (10, 10, 48620),
        (8, 6, 792),
    ],
)
def test_task0011_solution(m, n, result):
    assert solution(m=m, n=n) == result
