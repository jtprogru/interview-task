import pytest

from tasks.task0001 import solution


@pytest.mark.parametrize(
    "arr, result",
    [
        ([0, 1, 2, 3, 5], 4),
        ([1, 2, 3, 4, 5], 0),
        ([0, 1, 2, 3, 4, 5, 6, 7, 9], 8),
        ([0, 1, 2, 3, 4, 5], 6),
    ],
)
def test_task01_solution(arr, result):
    assert solution(arr) == result
