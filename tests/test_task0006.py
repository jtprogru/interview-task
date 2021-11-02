import pytest

from tasks.task0006 import solution


@pytest.mark.parametrize(
    "digits, result",
    [
        ([1, 2, 3], [1, 2, 4]),
        ([4, 3, 2, 1], [4, 3, 2, 2]),
        ([0], [1]),
        ([9], [1, 0]),
    ],
)
def test_task06_solution(digits, result):
    assert solution(digits) == result
