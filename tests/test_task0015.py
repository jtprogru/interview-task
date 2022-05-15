import pytest

from tasks.task0015 import solution


@pytest.mark.parametrize(
    "nums, target, result",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_task0015_solution(nums, target, result):
    assert solution(nums, target) == result
