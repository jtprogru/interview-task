import pytest

from tasks.task0013 import solution


@pytest.mark.parametrize(
    "nums1, nums2, result",
    [
        ([1, 2, 2, 1], [2, 2], [2, 2]),
        ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9]),
    ],
)
def test_task0013_solution(nums1, nums2, result):
    assert solution(nums1, nums2) == result
