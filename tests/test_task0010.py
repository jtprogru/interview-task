import pytest

from tasks.task0010 import solution


@pytest.mark.parametrize(
    "a, result",
    [
        ([13, 12, 15, 11, 9, 12, 16], [2, 1, 4, 2, 1, 1, 0]),
        ([11, 12, 15, 10, 9, 12, 16, 20], [1, 1, 4, 2, 1, 1, 1, 0]),
    ],
)
def test_task0010_solution(a, result):
    assert solution(a) == result
