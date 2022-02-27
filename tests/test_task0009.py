import pytest

from tasks.task0009 import solution


@pytest.mark.parametrize(
    "a, k, result",
    [
        ([-1, 2, 5, 8], 7, [-1, 8]),
        ([-3, -1, 0, 2, 6], 6, [0, 6]),
        ([2, 4, 5], 8, []),
        ([-2, -1, 1, 2], 0, [-2, 2]),
        ([-7, 0, 2, 3, 6, 8, 10, 15, 18, 20], 10, [0, 10]),
    ],
)
def test_task0009_solution(a, k, result):
    assert solution(a=a, k=k) == result
