import pytest

from tasks.task05 import solution


@pytest.mark.parametrize(
    "nums, k, result",
    [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([3, 99, -1, -100], 2, [-1, -100, 3, 99]),
        ([1, 4, 2, 5, 7, 9, 6], 13, [4, 2, 5, 7, 9, 6, 1]),
    ],
)
def test_task05_solution(nums, k, result):
    solution(nums, k)
    assert nums == result
