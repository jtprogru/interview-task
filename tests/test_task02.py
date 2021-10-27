import pytest

from tasks.task02 import solution


@pytest.mark.parametrize(
    "arr1, arr2, arr3, result",
    [
        (
            [1, 2, 3, 4, 5, 100],
            [6, 7, 8, 9, 100],
            [10, 20, 21, 22, 23, 24, 100],
            100,
        ),
        (
            [1, 2, 3, 4, 5, 1000],
            [6, 7, 8, 9, 100, 150, 1000],
            [10, 20, 21, 22, 23, 24, 100, 1000, 2000, 3000],
            1000,
        ),
    ],
)
def test_task02_solution(arr1, arr2, arr3, result):
    assert solution(arr1, arr2, arr3) == result
