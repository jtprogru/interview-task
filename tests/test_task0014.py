import pytest

from tasks.task0014 import solution


@pytest.mark.parametrize(
    "nums, result",
    [([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]), ([0], [0]), ([0, 1], [1, 0]), ([1, 0], [1, 0])],
)
def test_task0014_solution(nums, result):
    solution(nums)
    assert nums == result
