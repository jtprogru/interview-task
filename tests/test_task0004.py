import pytest

from tasks.task0004 import solution


@pytest.mark.parametrize(
    "nums, result",
    [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 3, 3, 4, 3, 2, 4, 2], True),
    ],
)
def test_task04_solution(nums, result):
    assert solution(nums) == result
