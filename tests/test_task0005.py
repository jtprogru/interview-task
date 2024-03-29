import pytest

from tasks.task0005 import solution


@pytest.mark.parametrize(
    "nums, k, result",
    [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([3, 99, -1, -100], 2, [-1, -100, 3, 99]),
        ([1, 4, 2, 5, 7, 9, 6], 13, [4, 2, 5, 7, 9, 6, 1]),
        ([1, 5, 2, 8, 234], 24, [5, 2, 8, 234, 1]),
    ],
)
def test_task0005_solution(nums, k, result):
    solution(nums, k)
    assert nums == result
