import pytest

from tasks.task0012 import solution


@pytest.mark.parametrize(
    "nums, result",
    [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
    ],
)
def test_task0010_solution(nums, result):
    assert solution(nums) == result
