import pytest

from tasks.task0008 import solution


@pytest.mark.parametrize(
    "a, idx, k, result",
    [
        ([10, 15, 20, 50, 55, 78, 91], 2, 3, [10, 15, 50]),
        ([0, 1, 2, 3, 4, 5, 6], 2, 3, [0, 1, 3]),
        ([1, 2, 3, 4, 5, 6], 0, 1, [2]),
        ([1, 2, 3, 4, 5], 4, 3, [2, 3, 4]),
    ],
)
def test_task0008_solution(a, idx, k, result):
    assert solution(a=a, idx=idx, k=k) == result
