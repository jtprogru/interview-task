import pytest

from tasks.task03 import solution


@pytest.mark.parametrize(
    "nums, result",
    [
        ([1, 1, 2], 2),
        ([1, 2, 3, 4, 5, 100, 100], 6),
        ([1, 2, 2, 2, 3, 4, 5], 5),
        ([10, 12, 13, 14, 14, 15, 15, 16, 16, 16], 6),
    ],
)
def test_task03_solution(nums, result):
    assert solution(nums) == result
