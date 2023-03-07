import pytest

from tasks.task0028 import solution


@pytest.mark.parametrize(
    "arr, result",
    [
        (
            [-2, 3, 0, 1, 5],
            3,
        ),
        (
            [1, 1],
            None,
        ),
        (
            [7, 10, 11, 32, -2, 44],
            32,
        ),
    ],
)
def test_task0028_solution(arr, result):
    assert solution(arr) == result
