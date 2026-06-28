import pytest

from tasks.task0030 import solution


@pytest.mark.parametrize(
    "a, b, result",
    [
        (
            [1, 2, 5],
            [1, 2, 3, 4, 6],
            [1, 1, 2, 2, 3, 4, 5, 6],
        ),
        (
            [],
            [1, 2, 3],
            [1, 2, 3],
        ),
        (
            [1, 2, 3],
            [],
            [1, 2, 3],
        ),
        (
            [],
            [],
            [],
        ),
        (
            [1, 4, 7],
            [2, 3, 8],
            [1, 2, 3, 4, 7, 8],
        ),
    ],
)
def test_task0030_solution(a, b, result):
    assert solution(a, b) == result
